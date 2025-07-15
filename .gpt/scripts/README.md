# Issue Files Verification

The `verify-hashes.py` script checks that each issue Markdown file under `.gpt/issues/phase*`
has a `content_hash` field in its YAML front-matter that matches the actual SHA-256 hash of
the file content (excluding the front-matter). This helps ensure that the metadata stays
in sync with the file body.

## Metadata Structure

Each issue file (`.md`) in `.gpt/issues/phaseX/` includes YAML front-matter with fields:

- `issue_id`: Numeric ID of the issue (unique).
- `title`: A brief title for the issue.
- `phase`: The phase number (e.g. 1, 2, ...).
- `status`: Current status (e.g. `open` or `closed`).
- `tags`: A list of relevant tags/labels.
- `created_at`: ISO 8601 timestamp of issue creation.
- `content_hash`: SHA-256 hash of the file content (excluding front-matter).

For example:

```yaml
---
issue_id: 1
title: "Example issue title"
phase: 1
status: open
tags: ["tag1", "tag2"]
created_at: "2025-07-08T12:00:00Z"
content_hash: e3b0c44298fc1c149afbf4c8996fb924...
---
Issue body starts here...
