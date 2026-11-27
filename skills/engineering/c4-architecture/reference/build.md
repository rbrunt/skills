# Build a model

One level per stage. Each stage ends at a review gate: stop there and wait for the user before starting the next, because a wrong boundary at one level invalidates everything below it.

## 1. Intake

Ask all of these in one round:

- **System**: which software system is being documented, in the user's words for where it starts and stops?
- **Code**: which repos and directories make it up?
- **Existing docs**: are there diagrams, architecture docs or decision records to read as secondary evidence?
- **Directory**: where should the model go? Default: `docs/architecture/` in the system's main repo.
- **Levels**: context and containers only, or components for named containers too?
- **Existing model**: is there one already? If there is, offer `update` or `critique` instead.

**Gate:** you have the answers.

## 2. Context

1. Read for the system's edges: entry points, API clients, SDK and queue clients, IAM policies, environment variables naming other services, infrastructure-as-code, CI deploy targets.
2. Draft the documented system, each external software system it talks to, and each relationship between them.
3. Present three lists, every row with its evidence:
   - **Systems**: name, one-line description, external or not.
   - **Relationships**: source, label, target, technology.
   - **People**: the roles you found evidence for. Then ask who else uses the system, since code rarely shows them.
4. Ask whether the user wants any view at this level beyond the single context view. Ask it open, with no examples.

**Gate:** the user approves the lists. Then copy `spec.c4`, write `model.c4` and `views.c4`, create `README.md` with a title and one line of scope, and run `c4docs render`. Send the README path.

## 3. Containers

1. Find every deployable unit and data store the system owns: read the infrastructure-as-code, Dockerfiles, deploy manifests, package entry points and CI pipelines end to end.
2. For each, record its name, what it does, its technology, and what it calls or is called by. Re-point each context-level relationship at the container that actually holds it.
3. Present **Containers** and **Relationships** as lists with evidence. List separately anything deployable you found and left out, with the reason.
4. Ask the open question about further views at this level.

**Gate:** every deployable unit and data store in the code is either a container in the list or in the left-out list, and the user approves. Then write, render, and send the README path.

## 4. Components

Only for containers the user named, one container per round.

1. Read the container's code for its major groupings: top-level packages, modules behind an interface, handlers, adapters to other containers.
2. Present 3–10 components with evidence, and the relationships among them and out to other containers.

**Gate:** the user approves this container's list. Then write `components/<container-id>.c4`, add its view, and render.

## 5. Hand-off

1. Run `c4docs check DIR`.
2. Send the model directory, the README path, and the `check` command, which the user can run in CI to keep the README matching the model.
3. Offer to run `critique`.
