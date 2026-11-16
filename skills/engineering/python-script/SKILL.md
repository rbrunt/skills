---
name: python-script
description: "Python scripts: apply these conventions when creating or changing standalone Python utility, automation, data, or API scripts."
---

# Python Scripts

## Process

1. Before creating a script, ask the user for its destination path. Do not choose a location on their behalf.
2. Declare every third-party dependency in the script's PEP 723 metadata block. Invoke the script with `uv run <script-path> [args]`.
3. Add only dependencies the script uses. Prefer these libraries for their respective jobs:
   - `rich` for user-facing formatted output, tables, and progress.
   - `click` for command-line interfaces.
   - `requests` for synchronous HTTP API calls.
   - `pydantic` for validation of untrusted inputs, configuration, and API payloads.
   - `polars` for new dataframe, CSV, and Parquet processing.
4. Use the standard library for paths, JSON, CSV, logging, and ordinary date/time handling. Keep reusable logic outside Click command functions so it can be tested independently.
5. For every request whose hostname is `*.auroraer.com`, load the target environment's credential file, strip its contents, and send that value in both headers:
   - `EOS-Cookie`
   - `Private-Token`

## Aurora Credentials

Select the credential file by target environment:

| Environment | File |
| --- | --- |
| production | `~/.aurora-api-key` |
| development | `~/.aurora-api-key.development` |
| staging | `~/.aurora-api-key.staging` |

Establish the target environment before making Aurora requests. If it is not clear from the request, URL, or existing project configuration, ask the user. Read the file at runtime; never embed, print, log, or write its value.

Fail clearly if the credential file is missing or empty. Do not send an Aurora request until both headers contain the loaded credential.

## Script Metadata

Use this PEP 723 form at the top of every standalone script with third-party dependencies:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "click",
#   "requests",
#   "rich",
# ]
# ///
```

The metadata exactly accounts for the script's third-party imports, and the finished script runs through `uv run`.
