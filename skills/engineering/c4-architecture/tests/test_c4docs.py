"""Renderer and README-region tests; likec4 itself is not run.

Run with: uv run --with click python -m unittest discover -s skills/engineering/c4-architecture/tests -v
"""

import importlib.machinery
import importlib.util
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

from click.testing import CliRunner

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "c4docs"
LOADER = importlib.machinery.SourceFileLoader("c4docs_under_test", str(SCRIPT))
SPEC = importlib.util.spec_from_loader(LOADER.name, LOADER)
c4docs = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = c4docs
LOADER.exec_module(c4docs)


def node(id, kind, title, **extra):
    return {"id": id, "kind": kind, "title": title, "parent": None, "children": [], "tags": [], **extra}


def containers_view():
    return {
        "id": "containers",
        "title": "Containers",
        "description": {"txt": "Inside Parcel Tracker"},
        "sourcePath": "views.c4",
        "autoLayout": {"direction": "LR"},
        "nodes": [
            node("courier", "person", "Courier"),
            node("tracker", "system", "Parcel Tracker", children=["tracker.api"]),
            node("tracker.api", "container", "Scan API", parent="tracker", technology="Python", description={"txt": 'Stores "scans"'}),
            node("sms", "system", "SMS Gateway", tags=["external"]),
        ],
        "edges": [
            {"source": "courier", "target": "tracker.api", "label": "Submits scans to", "technology": None},
            {"source": "tracker.api", "target": "sms", "label": "Sends texts through", "technology": "HTTPS"},
            {"source": "courier", "target": "sms", "label": None, "technology": None},
        ],
    }


class MermaidTest(unittest.TestCase):
    def setUp(self):
        self.out = c4docs.mermaid(containers_view())

    def test_direction_comes_from_the_view(self):
        self.assertTrue(self.out.startswith("flowchart LR\n"))

    def test_leaf_shows_name_type_technology_and_description(self):
        self.assertIn('tracker_api["`**Scan API**\n[Container: Python]\n\nStores #quot;scans#quot;`"]', self.out)

    def test_person_is_a_stadium_without_technology(self):
        self.assertIn('courier(["`**Courier**\n[Person]`"])', self.out)

    def test_parent_becomes_a_boundary_around_its_children(self):
        lines = self.out.splitlines()
        start = lines.index('  subgraph tracker["Parcel Tracker [Software System]"]')
        self.assertTrue(lines[start + 1].startswith("    tracker_api["))
        self.assertEqual(lines[lines.index("  end") - 1], 'Stores #quot;scans#quot;`"]')

    def test_edges_carry_label_and_technology(self):
        self.assertIn('  courier -- "`Submits scans to`" --> tracker_api', self.out)
        self.assertIn('  tracker_api -- "`Sends texts through [HTTPS]`" --> sms', self.out)
        self.assertIn("  courier --> sms", self.out)

    def test_external_tag_wins_over_kind_for_styling(self):
        self.assertIn("  class sms external", self.out)
        self.assertNotIn("classDef system", self.out)
        self.assertIn("  class tracker_api container", self.out)


class MergeTest(unittest.TestCase):
    def setUp(self):
        self.view = containers_view()
        self.region = c4docs.region(self.view)

    def test_empty_readme_becomes_the_region(self):
        self.assertEqual(c4docs.merge("", [self.view]), self.region)

    def test_new_view_is_appended_after_hand_written_text(self):
        self.assertEqual(c4docs.merge("# Title\n\nIntro.\n", [self.view]), "# Title\n\nIntro.\n\n" + self.region)

    def test_stale_region_is_replaced_in_place_and_surroundings_kept(self):
        readme = "# Title\n\n<!-- c4:view containers -->\nold\n<!-- /c4:view -->\n\nFooter.\n"
        self.assertEqual(c4docs.merge(readme, [self.view]), "# Title\n\n" + self.region + "\nFooter.\n")

    def test_orphan_region_is_dropped(self):
        readme = "# Title\n\n<!-- c4:view gone -->\nold\n<!-- /c4:view -->\n"
        self.assertEqual(c4docs.merge(readme, []), "# Title\n\n")

    def test_merge_is_idempotent(self):
        once = c4docs.merge("# Title\n", [self.view])
        self.assertEqual(c4docs.merge(once, [self.view]), once)

    def test_region_has_heading_description_diagram_and_key(self):
        self.assertIn("## Containers\n\nInside Parcel Tracker\n\n```mermaid\nflowchart LR\n", self.region)
        self.assertTrue(self.region.endswith("```\n\n" + c4docs.KEY + "\n<!-- /c4:view -->\n"))


class ViewsOfTest(unittest.TestCase):
    def test_keeps_source_order_and_skips_the_auto_index_view(self):
        dump = {"views": {"index": {"id": "index", "sourcePath": None}, "b": {"id": "b", "sourcePath": "v.c4"}, "a": {"id": "a", "sourcePath": "v.c4"}}}
        self.assertEqual([v["id"] for v in c4docs.views_of(dump)], ["b", "a"])


class CliTest(unittest.TestCase):
    def run_cli(self, command, readme=None):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "README.md"
            if readme is not None:
                path.write_text(readme, encoding="utf-8")
            with mock.patch.object(c4docs, "load_views", return_value=[containers_view()]):
                result = CliRunner().invoke(c4docs.cli, [command, tmp])
            return result, path.read_text(encoding="utf-8") if path.exists() else None

    def test_render_then_check_passes(self):
        _, rendered = self.run_cli("render", "# Title\n")
        result, after = self.run_cli("check", rendered)
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertEqual(after, rendered)

    def test_check_fails_with_a_diff_and_leaves_the_readme_alone(self):
        stale = "<!-- c4:view containers -->\nold\n<!-- /c4:view -->\n"
        result, after = self.run_cli("check", stale)
        self.assertEqual(result.exit_code, 1)
        self.assertIn("-old", result.output)
        self.assertEqual(after, stale)

    def test_check_fails_when_readme_is_missing(self):
        result, after = self.run_cli("check")
        self.assertEqual(result.exit_code, 1)
        self.assertIsNone(after)

    def test_view_serves_the_model_with_the_pinned_likec4(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(c4docs, "serve", return_value=0) as call:
            result = CliRunner().invoke(c4docs.cli, ["view", tmp, "--port", "6001"])
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertEqual(call.call_args.args[0], [*c4docs.LIKEC4, "start", "--port", "6001", tmp])
        self.assertIn("http://localhost:6001/", result.output)

    def test_serve_stops_the_whole_process_group_when_terminated(self):
        with tempfile.TemporaryDirectory() as tmp:
            pidfile = Path(tmp) / "pid"
            grandchild = f"sleep 60 & echo $! > {pidfile}; wait"
            runner = (
                "import importlib.machinery, importlib.util, os, signal, sys, threading\n"
                f"l = importlib.machinery.SourceFileLoader('c', {str(SCRIPT)!r})\n"
                "m = importlib.util.module_from_spec(importlib.util.spec_from_loader('c', l)); l.exec_module(m)\n"
                "threading.Timer(1, lambda: os.kill(os.getpid(), signal.SIGTERM)).start()\n"
                f"sys.exit(m.serve(['sh', '-c', {grandchild!r}]))\n"
            )
            subprocess.run([sys.executable, "-c", runner], timeout=20)
            pid = int(pidfile.read_text())
            for _ in range(20):
                if not Path(f"/proc/{pid}").exists():
                    break
                time.sleep(0.1)
            self.assertFalse(Path(f"/proc/{pid}").exists(), "grandchild outlived serve()")


if __name__ == "__main__":
    unittest.main()
