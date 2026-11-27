# Critique a model

Review how well the diagrams communicate, as a reader who has never seen the system. The model and its README are the only inputs: whether the model matches the code is `update`'s job, and whether the architecture is good is the user's.

## 1. Load

1. Run `c4docs check DIR`. If it fails, show the user why and agree whether to render first.
2. Read every `.c4` file and the README.

## 2. Review

Apply every item below to every view. `c4docs` already supplies each diagram's title, key and element types, so the checklist covers what the model controls.

**View**
1. The title and description say what the view shows and for which system.
2. It stays at one level: a context view shows people and software systems; a container view shows one system's containers and its neighbours; a component view shows one container's components and its neighbours.
3. It is readable at a glance. Past about 20 elements, propose which to split out into another view.

**Elements**
4. Each has a name a newcomer could find in the code or hear from the team.
5. Each has a description of what it does, not a restatement of its name.
6. Each container and component has a technology.
7. Each is the right abstraction per [format.md](format.md): flag a Docker image, a library, a team or a whole AWS account modelled as a container, and a separately deployed service modelled as a component.
8. Each person and system outside the documented system is tagged `#external`, and nothing inside it is.
9. No element sits unconnected.

**Relationships**
10. Each has a label.
11. The label reads as a sentence in the arrow's direction. Flag bare `uses`, `calls`, `data` and any label that describes the reply.
12. Each one that crosses a container boundary has a technology.
13. One arrow carries one intent. Flag a two-way dependency drawn as a single arrow, and two arrows that say the same thing.

**Language**
14. Every acronym and abbreviation is spelled out somewhere a reader of that view will see it.
15. One thing has one name across all views and the README's prose.

Mark each finding **major** (a reader would be misled or stuck) or **minor**, and give it a proposed fix: the exact new text where the fix is wording.

**Gate:** you have applied all 15 items to every view.

## 3. Report

Send findings grouped by view, majors first, each as: item number, what is wrong, proposed fix. Above them, a one-line verdict per view.

Some fixes need facts the model doesn't hold, such as a missing technology. Mark those **needs evidence**; applying them means reading the code as `update` does.

## 4. Walk

Ask one multi-select question per view, each major finding as an option with its fix, all pre-selected. Then offer the minor findings as one batch.

## 5. Write

1. Apply the accepted fixes to the `.c4` files.
2. Run `c4docs render DIR`, then `c4docs check DIR`.
3. Send a short changelog and the README path.
