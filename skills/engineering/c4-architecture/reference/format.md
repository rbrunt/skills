# Model format

A model is one directory (default `docs/architecture/`) documenting one software system:

| File | Holds |
|---|---|
| `spec.c4` | The C4 vocabulary. Copy `<skill-dir>/templates/spec.c4` and leave it as is. |
| `model.c4` | People, software systems, the documented system's containers, and every relationship between them. |
| `views.c4` | The views. |
| `components/<container-id>.c4` | One container's components. Exists only for containers the user asked to take to component level. |
| `README.md` | The user's prose, plus one generated region per view. |

## The four abstractions

- **Person**: a human role that uses the system.
- **Software system**: something that delivers value to its users, owned by one team. The documented system is one; everything else it talks to is another.
- **Container**: something that must be running, or must exist, for the system to work, and is deployed on its own: a web app, a Lambda, a batch job, a database, a bucket, a queue. A Docker image is packaging; the thing it runs is the container. A shared library is part of each container that imports it.
- **Component**: a group of code behind one interface inside a single container. It ships with its container.

Tag every person and software system outside the documented system `#external`; `c4docs` draws those grey.

## Writing the model

```
// model.c4
model {
  courier = person 'Courier' {
    #external
    description 'Scans each parcel at every stop'
  }
  customer = person 'Customer' {
    #external
    description 'Waits for a parcel'
  }
  sms = system 'SMS Gateway' {
    #external
    description 'Delivers text messages to phones'
  }
  tracker = system 'Parcel Tracker' {
    description 'Records where each parcel is and tells its customer'

    api = container 'Scan API' {
      description 'Receives scans and stores each parcel\'s location'
      technology 'Python, AWS Lambda'
    }
    worker = container 'Notification worker' {
      description 'Decides which scans a customer hears about'
      technology 'Python, AWS Batch'
    }
    api -> worker 'Queues each scan for'
  }
  courier -> tracker.api 'Submits scans to' {
    technology 'HTTPS'
  }
  tracker.worker -> sms 'Sends delivery texts through' {
    technology 'HTTPS'
  }
  sms -> customer 'Texts delivery updates to'
}

// components/worker.c4
model {
  extend tracker.worker {
    rules = component 'Notification rules' {
      description 'Chooses which scans warrant a text'
      technology 'Python package'
    }
  }
}

// views.c4
views {
  view context {
    title 'System context'
    description 'Who and what Parcel Tracker talks to'
    include tracker, * -> tracker, tracker -> *, customer
  }
  view containers of tracker {
    title 'Containers'
    include *
  }
  view components-worker of tracker.worker {
    title 'Components of Notification worker'
    include *
  }
}
```

- Every element has a `description` of what it does. Every container and component has a `technology`.
- Every relationship has a label that reads as a sentence with its two ends: *Scan API* **queues each scan for** *Notification worker*. Give it a `technology` wherever it crosses a container boundary.
- Draw each relationship from the most specific element you have evidence for (`tracker.worker -> sms`, not `tracker -> sms`). Higher-level views roll it up automatically.
- Ids are short, stable and lower-case (`api`, `sms`). Keep an id when you rename its element, so diffs stay readable.
- `include tracker, * -> tracker, tracker -> *` shows the system and its direct neighbours. Add by name anyone who matters but reaches the system through another one, as `customer` does above.

## Views

The standard set is `context`, `containers`, and `components-<container-id>` per requested container. Any other view exists because the user asked for it.

## README regions

`c4docs render DIR` writes each view between `<!-- c4:view <id> -->` and `<!-- /c4:view -->`: heading, description, Mermaid diagram, key. Text outside the regions belongs to the user. A new view's region is appended to the end; tell the user they can move it. A removed view's region is deleted.

`c4docs check DIR` validates the model and fails with a diff when any region differs from a fresh render. A failed validation prints LikeC4's errors with file and line.
