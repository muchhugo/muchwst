"""Offline tests with synthetic records only; no target, credentials or network."""
from __future__ import annotations
import copy
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from render_report import (ReportError, _summary_counts, load_report, render_html,
                           render_markdown, validate_report, write_report)
from validate_pack import validate

BASE=json.loads((ROOT/'examples/synthetic-assessment/findings.json').read_text(encoding='utf-8'))


class ReportValidationTests(unittest.TestCase):
    def setUp(self):
        self.report=copy.deepcopy(BASE)
        self.finding=self.report['findings'][0]

    def test_valid_synthetic_code_proof_format(self):
        validate_report(self.report)

    def test_empty_findings_report_is_valid(self):
        self.report['findings']=[]
        self.report['summary']='No confirmed vulnerabilities in reviewed scope; no actual app reviewed in this synthetic example.'
        validate_report(self.report)

    def test_missing_required_field(self):
        del self.finding['root_cause']
        with self.assertRaises(ReportError): validate_report(self.report)

    def test_unknown_field_does_not_echo_sensitive_value(self):
        self.finding['PRIVATE_CONTENT_SENTINEL']='NEVER_ECHO_VALUE'
        with self.assertRaises(ReportError) as caught: validate_report(self.report)
        self.assertNotIn('PRIVATE_CONTENT_SENTINEL',str(caught.exception))
        self.assertNotIn('NEVER_ECHO_VALUE',str(caught.exception))

    def test_invalid_severity(self):
        self.finding['severity']='ultra-critical'
        with self.assertRaises(ReportError): validate_report(self.report)

    def test_duplicate_finding_id(self):
        self.report['findings'].append(copy.deepcopy(self.finding))
        with self.assertRaises(ReportError): validate_report(self.report)

    def test_conflicting_example_flags(self):
        self.report['example_only']=False
        with self.assertRaises(ReportError): validate_report(self.report)

    def test_confirmed_reproduction_cannot_be_unexecuted(self):
        self.finding['evidence_level']='confirmed-reproduction'
        with self.assertRaises(ReportError): validate_report(self.report)

    def test_confirmed_reproduction_needs_steps(self):
        self.finding['evidence_level']='confirmed-reproduction'
        self.finding['reproduction']['status']='executed'
        self.finding['reproduction']['steps']=[]
        with self.assertRaises(ReportError): validate_report(self.report)

    def test_confirmed_evidence_cannot_be_empty(self):
        self.finding['evidence']=[]
        with self.assertRaises(ReportError): validate_report(self.report)

    def test_observation_is_not_a_confirmed_vulnerability(self):
        self.finding['evidence_level']='observation'
        with self.assertRaises(ReportError): validate_report(self.report)

    def test_accepted_risk_requires_owner_record(self):
        self.finding['status']='accepted-risk'
        with self.assertRaises(ReportError): validate_report(self.report)
        self.finding['risk_acceptance']={'owner':'fictional owner','reason':'synthetic decision only','revisit_date':'2026-11-30'}
        validate_report(self.report)
        self.finding['risk_acceptance']['revisit_date']='whenever'
        with self.assertRaises(ReportError): validate_report(self.report)

    def test_false_positive_requires_counterevidence(self):
        self.finding['status']='false-positive'
        with self.assertRaises(ReportError): validate_report(self.report)
        self.finding['closure_reason']='Synthetic premise changed; real closure would need concrete counterevidence.'
        validate_report(self.report)

    def test_retest_requires_passing_record_at_target_revision(self):
        self.finding['status']='retest-passed'
        with self.assertRaises(ReportError): validate_report(self.report)
        test={'revision':'fictional-before','configuration_revision':'fictional-config',
              'environment':'synthetic','case':'fake case, no app test','method':'format-only',
              'expected':'synthetic expected','observed':'synthetic outcome','result':'passed'}
        self.finding['retests']=[test]
        validate_report(self.report)
        test['revision']='a-different-head'
        with self.assertRaises(ReportError): validate_report(self.report)

    def test_mitigated_does_not_require_claim_of_source_fix(self):
        self.finding['status']='mitigated'
        validate_report(self.report)

    def test_unverified_mapping_is_rejected(self):
        self.finding['mappings']=[{'system':'Example taxonomy','identifier':'EXAMPLE',
                                  'edition':'fictional','source':'not retrieved','verified':False}]
        with self.assertRaises(ReportError): validate_report(self.report)

    def test_cvss_boolean_score_and_mismatched_version_rejected(self):
        self.finding['cvss']={'version':'3.1','vector':'CVSS:4.0/FAKE', 'score':True,
                             'source':'synthetic','assumptions':'not a real score','validated':True}
        with self.assertRaises(ReportError): validate_report(self.report)
        self.finding['cvss']['score']=5.0
        with self.assertRaises(ReportError): validate_report(self.report)

    def test_suspected_not_counted_as_confirmed(self):
        self.finding['evidence_level']='suspected'
        counts=_summary_counts(self.report)
        self.assertIn('Confirmed vulnerability records (including remediated history): 0',counts)
        self.assertIn('Suspected vulnerability records: 1',counts)


class RenderingAndOutputTests(unittest.TestCase):
    def setUp(self):
        self.report=copy.deepcopy(BASE)

    def test_html_escapes_hostile_evidence_and_title(self):
        self.report['title']='<script>not executable</script>'
        self.report['findings'][0]['evidence']=['<img src="https://example.invalid/x" onerror="alert(1)">']
        content=render_html(self.report)
        self.assertNotIn('<script',content.lower())
        self.assertNotIn('<img',content.lower())
        self.assertIn('&lt;script&gt;',content)
        self.assertIn('default-src',content)
        self.assertIn('SYNTHETIC EXAMPLE',content)

    def test_markdown_evidence_cannot_close_fence(self):
        self.report['findings'][0]['evidence']=['````\n![remote](https://example.invalid/image)\n<script>text</script>']
        content=render_markdown(self.report)
        self.assertIn('`````text',content)
        self.assertIn('SYNTHETIC EXAMPLE',content)

    def test_markdown_heading_is_plain_text(self):
        self.report['title']='Title\n![remote](https://example.invalid/image)<script>'
        first=render_markdown(self.report).splitlines()[0]
        self.assertNotIn('![remote]',first)
        self.assertNotIn('<script>',first)

    def test_output_new_private_directory_and_readback(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'report'
            paths=write_report(self.report,dest)
            self.assertEqual({p.name for p in paths},{'findings.json','REPORT.md','REPORT.html'})
            self.assertEqual(load_report(dest/'findings.json'),self.report)
            if os.name=='posix':
                self.assertEqual(stat.S_IMODE(dest.stat().st_mode),0o700)
                for path in paths: self.assertEqual(stat.S_IMODE(path.stat().st_mode),0o600)

    def test_existing_output_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'report'; dest.mkdir()
            marker=dest/'REPORT.md'; marker.write_text('keep original',encoding='utf-8')
            with self.assertRaises(ReportError): write_report(self.report,dest)
            self.assertEqual(marker.read_text(encoding='utf-8'),'keep original')

    @unittest.skipUnless(os.name=='posix','Symlink case uses POSIX test facilities')
    def test_symlink_output_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp)/'original'; target.mkdir()
            dest=Path(tmp)/'output'; dest.symlink_to(target,target_is_directory=True)
            with self.assertRaises(ReportError): write_report(self.report,dest)
            self.assertEqual(list(target.iterdir()),[])

    def test_missing_output_parent_not_created(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'absent-parent'/'report'
            with self.assertRaises(ReportError): write_report(self.report,dest)
            self.assertFalse(dest.parent.exists())

    def test_bad_json_does_not_echo_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'input.json'; path.write_text('{PRIVATE_SENTINEL}',encoding='utf-8')
            with self.assertRaises(ReportError) as caught: load_report(path)
            self.assertNotIn('PRIVATE_SENTINEL',str(caught.exception))


class PackTests(unittest.TestCase):
    def test_complete_portable_pack(self):
        results=validate()
        self.assertEqual(results['skills'],8)
        self.assertEqual(results['topics'],250)
        self.assertGreater(results['relative_links'],300)


if __name__=='__main__':
    unittest.main()
