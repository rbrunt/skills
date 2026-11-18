"""CLI contract tests. Run with: uv run --with click --with pydantic python -m unittest discover -s skills/productivity/user-story-map/tests -v"""

import copy
import importlib.machinery
import importlib.util
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
import unittest
from unittest import mock

from click.testing import CliRunner


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "storymap"
LOADER = importlib.machinery.SourceFileLoader("storymap_under_test", str(SCRIPT))
SPEC = importlib.util.spec_from_loader(LOADER.name, LOADER)
storymap = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = storymap
LOADER.exec_module(storymap)


def fixture():
    # Deliberately omit defaults on some cards, but retain an explicit null ref.
    return {
        "version": 1,
        "title": "Café journey",
        "description": "Découvrir → commander",
        "steps": [
            {"id": "browse", "title": "Browse"},
            {"id": "order", "title": "Order"},
        ],
        "milestones": [
            {"id": "mvp", "title": "First release"},
            {"id": "later", "title": "Later"},
        ],
        "cards": {
            "a": {"id": "a", "kind": "story", "title": "Find café", "description": None},
            "b": {
                "id": "b", "kind": "story", "title": "Choose coffee",
                "description": "No milk", "referenceId": "CAFE-2", "status": "in-progress",
            },
            "c": {
                "id": "c", "kind": "question", "title": "Pay now?",
                "description": None, "referenceId": None, "status": "done",
            },
            "d": {"id": "d", "kind": "story", "title": "Collect", "description": "À emporter"},
        },
        "cells": {"browse|mvp": ["a", "b"], "order|mvp": ["c"], "order|later": ["d"]},
    }


class StorymapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / "map.json"
        self.runner = CliRunner()
        self.original = fixture()
        self.reset()

    def reset(self):
        self.path.write_text(json.dumps(self.original, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def invoke(self, *args):
        return self.runner.invoke(storymap.cli, list(map(str, args)))

    def edit(self, *args, path=None):
        return self.invoke("edit", path or self.path, *args)

    def assert_success(self, result, expected):
        self.assertEqual(result.exit_code, 0, f"{result.output}\n{result.exception!r}")
        self.assertTrue(result.output.strip(), "an edit should acknowledge success")
        self.assertLessEqual(len(result.output.strip().splitlines()), 3, result.output)
        actual = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertEqual(actual, expected)
        self.assertIn("Café", self.path.read_text(encoding="utf-8"))
        checked = self.invoke("check", self.path)
        self.assertEqual(checked.exit_code, 0, checked.output)
        self.assertEqual(set(self.root.iterdir()), {self.path})

    def assert_failure(self, *args):
        before = self.path.read_bytes()
        entries = set(self.root.rglob("*"))
        result = self.edit(*args)
        self.assertNotEqual(result.exit_code, 0, result.output)
        self.assertTrue(result.output.strip(), "failures should explain the problem")
        self.assertNotIn("Traceback", result.output)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(set(self.root.rglob("*")), entries, "temporary files must be cleaned up")
        return result

    def test_set_card_fields_individually(self):
        cases = [
            ("--title", "Thé glacé", "title"),
            ("--description", "Avec crème", "description"),
            ("--reference", "CAFE-42", "referenceId"),
            ("--kind", "question", "kind"),
            ("--status", "done", "status"),
            ("--status", "in-progress", "status"),
            ("--status", "todo", "status"),
            ("--title", "", "title"),
            ("--description", "", "description"),
            ("--reference", "", "referenceId"),
        ]
        for option, value, key in cases:
            with self.subTest(option=option, value=value):
                self.reset()
                expected = copy.deepcopy(self.original)
                expected["cards"]["a"][key] = value
                self.assert_success(self.edit("set-card", "a", option, value), expected)

    def test_set_card_multiple_fields_and_clear(self):
        expected = copy.deepcopy(self.original)
        expected["cards"]["b"].update(
            title="Décider", description=None, kind="question", status="todo"
        )
        del expected["cards"]["b"]["referenceId"]
        self.assert_success(self.edit(
            "set-card", "b", "--title", "Décider", "--clear-description",
            "--clear-reference", "--kind", "question", "--status", "todo",
        ), expected)

    def test_clear_already_empty_fields(self):
        for card_id in ("a", "c"):
            with self.subTest(card_id=card_id):
                self.reset()
                expected = copy.deepcopy(self.original)
                expected["cards"][card_id].pop("referenceId", None)
                self.assert_success(self.edit(
                    "set-card", card_id, "--clear-description", "--clear-reference"
                ), expected)

    def test_add_card_defaults_to_end(self):
        expected = copy.deepcopy(self.original)
        expected["cards"]["new"] = {
            "id": "new", "title": "Goûter", "description": None,
            "kind": "story", "status": "todo",
        }
        expected["cells"]["browse|mvp"].append("new")
        self.assert_success(self.edit(
            "add-card", "new", "--title", "Goûter", "--step", "browse", "--milestone", "mvp"
        ), expected)

    def test_add_card_explicit_fields_and_indices(self):
        for step, milestone, index in (("browse", "mvp", 0), ("browse", "mvp", 2), ("browse", "later", 0)):
            with self.subTest(step=step, milestone=milestone, index=index):
                self.reset()
                expected = copy.deepcopy(self.original)
                expected["cards"]["new"] = {
                    "id": "new", "title": "Pourquoi?", "description": "Très important",
                    "referenceId": "CAFE-3", "kind": "question", "status": "in-progress",
                }
                expected["cells"].setdefault(f"{step}|{milestone}", []).insert(index, "new")
                self.assert_success(self.edit(
                    "add-card", "new", "--title", "Pourquoi?", "--step", step,
                    "--milestone", milestone, "--index", index, "--description", "Très important",
                    "--reference", "CAFE-3", "--kind", "question", "--status", "in-progress",
                ), expected)

    def test_move_card(self):
        # Destination indices are evaluated after removing the moving card.
        cases = [
            ("a", "browse", "mvp", None),
            ("a", "browse", "mvp", 1),
            ("b", "browse", "mvp", 0),
            ("a", "browse", "mvp", 0),
            ("a", "order", "mvp", 0),
            ("a", "order", "mvp", None),
            ("c", "browse", "later", None),
            ("c", "browse", "mvp", 2),
            ("c", "order", "mvp", 0),
        ]
        for card_id, step, milestone, index in cases:
            with self.subTest(card_id=card_id, step=step, milestone=milestone, index=index):
                self.reset()
                expected = copy.deepcopy(self.original)
                source = next(key for key, ids in expected["cells"].items() if card_id in ids)
                destination = f"{step}|{milestone}"
                expected["cells"][source].remove(card_id)
                # Preserve an existing destination's position even for a singleton move to itself.
                if not expected["cells"][source] and source != destination:
                    del expected["cells"][source]
                ids = expected["cells"].setdefault(destination, [])
                ids.insert(len(ids) if index is None else index, card_id)
                args = ["move-card", card_id, "--step", step, "--milestone", milestone]
                if index is not None:
                    args += ["--index", index]
                self.assert_success(self.edit(*args), expected)

    def test_remove_card_and_empty_source(self):
        for card_id, source in (("a", "browse|mvp"), ("c", "order|mvp")):
            with self.subTest(card_id=card_id):
                self.reset()
                expected = copy.deepcopy(self.original)
                del expected["cards"][card_id]
                expected["cells"][source].remove(card_id)
                if not expected["cells"][source]:
                    del expected["cells"][source]
                self.assert_success(self.edit("remove-card", card_id), expected)

    def test_rename_step(self):
        expected = copy.deepcopy(self.original)
        expected["steps"][0]["title"] = "Découvrir"
        self.assert_success(self.edit("rename-step", "browse", "--title", "Découvrir"), expected)

    def test_rejects_missing_fields_and_conflicting_flags(self):
        cases = [
            ("set-card", "a"),
            ("set-card", "a", "--description", "x", "--clear-description"),
            ("set-card", "a", "--reference", "x", "--clear-reference"),
            ("add-card", "new", "--step", "browse", "--milestone", "mvp"),
            ("add-card", "new", "--title", "New", "--milestone", "mvp"),
            ("add-card", "new", "--title", "New", "--step", "browse"),
            ("move-card", "a", "--step", "browse"),
            ("move-card", "a", "--milestone", "mvp"),
            ("rename-step", "browse"),
        ]
        for args in cases:
            with self.subTest(args=args):
                self.assert_failure(*args)

    def test_rejects_unknown_and_duplicate_ids(self):
        cases = [
            ("set-card", "missing", "--title", "New"),
            ("move-card", "missing", "--step", "browse", "--milestone", "mvp"),
            ("remove-card", "missing"),
            ("rename-step", "missing", "--title", "New"),
            ("add-card", "a", "--title", "Duplicate", "--step", "browse", "--milestone", "mvp"),
        ]
        for command, card_id, prefix in (("add-card", "new", ["--title", "New"]), ("move-card", "a", [])):
            for step, milestone in (("missing", "mvp"), ("browse", "missing")):
                cases.append((command, card_id, *prefix, "--step", step, "--milestone", milestone))
        for args in cases:
            with self.subTest(args=args):
                self.assert_failure(*args)

    def test_rejects_invalid_indices_and_enums(self):
        for command, card_id, prefix in (("add-card", "new", ["--title", "New"]), ("move-card", "a", [])):
            # Moving a within its own two-card cell leaves only one valid slot before append.
            too_large = "3" if command == "add-card" else "2"
            for index in ("-1", too_large, "1.5", "abc"):
                with self.subTest(command=command, index=index):
                    self.assert_failure(command, card_id, *prefix, "--step", "browse", "--milestone", "mvp", "--index", index)
        for command, prefix in (("set-card", ["a"]), ("add-card", ["new", "--title", "New", "--step", "browse", "--milestone", "mvp"])):
            for option, value in (("--kind", "task"), ("--status", "finished")):
                with self.subTest(command=command, option=option):
                    self.assert_failure(command, *prefix, option, value)
        for index in ("-1", "1"):
            with self.subTest(empty_destination_index=index):
                self.assert_failure("move-card", "a", "--step", "browse", "--milestone", "later", "--index", index)

    def test_rejects_invalid_new_card_ids(self):
        for card_id in ("", "bad|id"):
            with self.subTest(card_id=card_id):
                self.assert_failure("add-card", card_id, "--title", "New", "--step", "browse", "--milestone", "mvp")

    def test_every_command_validates_input_before_writing(self):
        invalid = copy.deepcopy(self.original)
        invalid["cells"]["browse|mvp"].append("unknown")
        for text in ("{broken json", json.dumps(invalid), "[]"):
            for args in (
                ("set-card", "a", "--title", "New"),
                ("add-card", "new", "--title", "New", "--step", "browse", "--milestone", "mvp"),
                ("move-card", "a", "--step", "order", "--milestone", "mvp"),
                ("remove-card", "a"),
                ("rename-step", "browse", "--title", "New"),
            ):
                with self.subTest(text=text[:20], command=args[0]):
                    self.path.write_text(text, encoding="utf-8")
                    self.assert_failure(*args)

    def test_missing_file_is_not_created(self):
        self.path.unlink()
        result = self.edit("set-card", "a", "--title", "New")
        self.assertNotEqual(result.exit_code, 0)
        self.assertTrue(result.output.strip())
        self.assertEqual(list(self.root.iterdir()), [])

    def test_atomic_replace_failure_preserves_bytes_and_cleans_temp(self):
        with mock.patch.object(Path, "replace", side_effect=OSError("replacement denied")) as replace:
            self.assert_failure("set-card", "a", "--title", "New")
        replace.assert_called_once()

    def test_success_uses_atomic_replace(self):
        calls = []
        original_path_replace = Path.replace

        def path_replace(path, target):
            calls.append((path, target))
            return original_path_replace(path, target)

        expected = copy.deepcopy(self.original)
        expected["cards"]["a"]["title"] = "New"
        with mock.patch.object(Path, "replace", new=path_replace):
            self.assert_success(self.edit("set-card", "a", "--title", "New"), expected)
        self.assertTrue(calls, "writes must use atomic replacement")

    @unittest.skipUnless(os.name == "posix", "POSIX file modes and symlinks")
    def test_preserves_permissions_and_follows_symlink(self):
        self.path.chmod(0o640)
        link = self.root / "linked-map.json"
        link.symlink_to(self.path.name)
        result = self.edit("set-card", "a", "--title", "Thé", path=link)
        self.assertEqual(result.exit_code, 0, f"{result.output}\n{result.exception!r}")
        self.assertTrue(link.is_symlink())
        self.assertEqual(os.readlink(link), self.path.name)
        self.assertEqual(stat.S_IMODE(self.path.stat().st_mode), 0o640)
        expected = copy.deepcopy(self.original)
        expected["cards"]["a"]["title"] = "Thé"
        self.assertEqual(json.loads(self.path.read_text(encoding="utf-8")), expected)
        self.assertEqual(link.read_bytes(), self.path.read_bytes())
        self.assertEqual(set(self.root.iterdir()), {self.path, link})

    def test_check_and_show_regression(self):
        before = self.path.read_bytes()
        checked = self.invoke("check", self.path)
        self.assertEqual(checked.exit_code, 0, checked.output)
        self.assertIn("2 steps, 2 milestones, 4 cards", checked.output)
        shown = self.invoke("show", self.path)
        self.assertEqual(shown.exit_code, 0, shown.output)
        for text in ("# Café journey", "## First release", "## Later", "[~] Choose coffee", "[x] ? Pay now?", "(CAFE-2)"):
            self.assertIn(text, shown.output)
        self.assertLess(shown.output.index("Find café"), shown.output.index("Choose coffee"))
        for milestone in ("mvp", "First release"):
            with self.subTest(milestone=milestone):
                shown = self.invoke("show", self.path, "--milestone", milestone)
                self.assertEqual(shown.exit_code, 0, shown.output)
                self.assertIn("## First release", shown.output)
                self.assertNotIn("## Later", shown.output)
        self.assertNotEqual(self.invoke("show", self.path, "--milestone", "missing").exit_code, 0)
        self.assertEqual(self.path.read_bytes(), before)

    def test_link_open_link_regression(self):
        before = self.path.read_bytes()
        linked = self.invoke("link", self.path)
        self.assertEqual(linked.exit_code, 0, linked.output)
        url = linked.output.strip()
        self.assertTrue(url.startswith("https://user-story-map.richardbrunt.co.uk/#map="))
        expected = copy.deepcopy(self.original)
        for card in expected["cards"].values():
            card.setdefault("status", "todo")
            if card.get("referenceId") is None:
                card.pop("referenceId", None)
        opened = self.invoke("open-link", url)
        self.assertEqual(opened.exit_code, 0, opened.output)
        self.assertEqual(json.loads(opened.output), expected)
        output = self.root / "decoded.json"
        opened = self.invoke("open-link", url, "-o", output)
        self.assertEqual(opened.exit_code, 0, opened.output)
        self.assertEqual(json.loads(output.read_text(encoding="utf-8")), expected)
        self.assertEqual(self.invoke("check", output).exit_code, 0)
        self.assertEqual(self.path.read_bytes(), before)
        for bad_url in ("https://example.com", "https://example.com/#map=not-valid"):
            with self.subTest(url=bad_url):
                self.assertNotEqual(self.invoke("open-link", bad_url).exit_code, 0)


if __name__ == "__main__":
    unittest.main()
