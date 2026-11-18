# Skills

Skills I maintain and a couple I vendor, 

## Install

```sh
npx skills@latest add rbrunt/skills
```

## Skills

### Engineering

- [code-flow-visualisation](skills/engineering/code-flow-visualisation/SKILL.md) — Explain code flow with a small call tree or sequence diagram when it helps more than prose.
- [gh-stack](skills/engineering/gh-stack/SKILL.md) — Create and manage dependent pull requests with `gh stack`.
- [git-commit](skills/engineering/git-commit/SKILL.md) — Write commit messages in my preferred style, grounded in the discussion behind the change.
- [jira-status-nudge](skills/engineering/jira-status-nudge/SKILL.md) — Prompt me to keep Jira issue status aligned with work as it progresses.
- [python-script](skills/engineering/python-script/SKILL.md) — Apply my conventions to standalone Python scripts, including PEP 723 dependencies and `uv`.

### Productivity

- [briefing-paper](skills/productivity/briefing-paper/SKILL.md) — Write project plans and findings reports as single-file HTML in my template.
- [grilling](skills/productivity/grilling/SKILL.md) — Stress-test a plan or decision through rounds of questions. Vendored from Matt Pocock.
- [unslop](skills/productivity/unslop/SKILL.md) — Cut AI tells from prose. Vendored from Lauren Tan's pstack; I find it makes LLM generated text a little easier to read.
- [user-story-map](skills/productivity/user-story-map/SKILL.md) — Build, update, or critique a user story map and its MVP or walking-skeleton scope.

## Third-party skills

`npx skills add` installs skills found in this repo; it does not install other
repos or CLIs on behalf of this one. Install these separately if wanted:

- [Impeccable](https://impeccable.style/): `npx impeccable install`. Its
  installer manages the skill, CLI, and hooks; follow its prompts.

<details>
<summary>Licenses for vendored skills</summary>
  
`skills/productivity/grilling` is vendored from Matt Pocock's
[skills repo](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md)
under the MIT license; its licinstallerce is kept alongside it.

`skills/productivity/unslop` is vendored from
[Lauren Tan's pstack skill at bc697d0](https://github.com/cursor/plugins/blob/bc697d0a5a16/pstack/skills/unslop/SKILL.md).
It is redistributed under its MIT license; its license notice is kept
alongside it.
</details>
