# Skills

My agent skills, grouped under `skills/engineering/` and `skills/productivity/`.

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

`skills/productivity/unslop` preserves the locally installed version of
[Lauren Tan's pstack skill](https://github.com/cursor/plugins/tree/main/pstack/skills/unslop).
It differs from current upstream and is redistributed under its MIT license;
its license notice is kept alongside it.
