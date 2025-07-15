---
issue_id: 5
title: "Change pre-commit hook to validate-only (no editor spawn)"
phase: 2
status: open
tags: ["insight-synch", "srs", "hook"]
created_at: "2025-07-10T09:00:00Z"
content_hash: 44b754a85054e2dac52d16de240e16c9b7530fef1a45d1ea57fec5f75322c58d
---
The SRS currently describes the pre-commit hook as spawning an interactive editor to insert the insight payload. According to SRS §3.1 FR-2, the hook should instead validate an already-inserted payload and not open an editor. Update the requirements to:

- Remove or change wording that suggests opening an editor (e.g., replace “spawns editor / interactive prompt”).
- Clarify that the hook is validate-only: it checks the payload written by the developer and aborts on mismatch.
