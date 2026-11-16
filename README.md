# Skills

Skills I maintain and a couple I vendor, grouped under `skills/engineering/`
and `skills/productivity/`.

## Install

```sh
npx skills@latest add rbrunt/skills -g -a claude-code -a opencode -a pi
```

This installs selected skills globally for Claude Code, OpenCode, and Pi. Omit
`-g` for a project-local install, or change the `-a` flags to select other
agents. The repo is private, so authenticate with GitHub first (for example,
`gh auth login`). To check for updates, use `npx skills@latest check`; to
update globally installed skills, use `npx skills@latest update -g`.

Choose skills at the prompt rather than installing duplicates. In particular,
`grilling` may already be linked from `~/.agents/skills` into Claude's skill
directory, or supplied by Matt Pocock's Claude Code plugin.

## Skills

### Engineering

- [call-graph-visualisation](skills/engineering/call-graph-visualisation/SKILL.md) — Trace a program or feature through a concise, source-checked ASCII call tree.
- [gh-stack](skills/engineering/gh-stack/SKILL.md) — Create and manage dependent pull requests with `gh stack`.
- [git-commit](skills/engineering/git-commit/SKILL.md) — Write commit messages in my preferred style, grounded in the discussion behind the change.
- [python-script](skills/engineering/python-script/SKILL.md) — Apply my conventions to standalone Python scripts, including PEP 723 dependencies and `uv`.

### Productivity

- [briefing-paper](skills/productivity/briefing-paper/SKILL.md) — Write project plans and findings reports as single-file HTML in the Briefing Paper style.
- [grilling](skills/productivity/grilling/SKILL.md) — Stress-test a plan or decision through rounds of questions. Vendored from Matt Pocock.
- [unslop](skills/productivity/unslop/SKILL.md) — Cut AI tells from prose. Vendored from Lauren Tan's pstack; set to manual invocation upstream.
- [user-story-map](skills/productivity/user-story-map/SKILL.md) — Build, update, or critique a user story map and its MVP or walking-skeleton scope.

## Third-party skills

`npx skills add` installs skills found in this repo; it does not install other
repos or CLIs on behalf of this one. Install these separately if wanted:

- [Impeccable](https://impeccable.style/): `npx impeccable install`. Its
  installer manages the skill, CLI, and hooks; follow its prompts.
- [Matt Pocock's other skills](https://github.com/mattpocock/skills):
  `npx skills@latest add mattpocock/skills -g -a opencode -a pi` and select
  the skills you want, **excluding `grilling`**, which is already included
  here. For Claude Code, upstream recommends
  `claude plugin install mattpocock-skills@claude-plugins-official` instead of
  a skills.sh install. If using the plugin, omit this repo's `grilling` for
  Claude Code as well.

`skills/productivity/grilling` is vendored from Matt Pocock's
[skills repo](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md)
under the MIT license; its license notice is kept alongside it.

`skills/productivity/unslop` is vendored from
[Lauren Tan's pstack skill at bc697d0](https://github.com/cursor/plugins/blob/bc697d0a5a16/pstack/skills/unslop/SKILL.md).
It is redistributed under its MIT license; its license notice is kept
alongside it.
