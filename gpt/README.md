## GPT Synchronization Instructions

This repository uses a stateful multi-agent workflow governed by CoordinatorGPT.

- **Current Workflow ID**: `realrun-002`
- **Phase**: `IMPLEMENT`
- **SRS**: [`docs/SRS.md`](../docs/SRS.md)

All GPT agents must:

1. Read `.gpt/status.json` for the current phase
2. Use `.gpt/inbox/` to validate prior state transitions
3. Output replies that conform to `.gpt/schemas/intake-v1.json`

### Example Agent Startup Instruction

> You are now entering the IMPLEMENT phase of `realrun-002`, using the validated SRS at `docs/SRS.md`. Prior transitions are logged in `.gpt/inbox/`.

### DELIVER Phase Finalization Requirement

All CoordinatorGPT agents must complete the DELIVER phase with one of the following:

- Emit the final confirmation payload themselves:

```json
{
  "phase": "inbox",
  "conversation_id": "<workflow_id>",
  "timestamp": "<ISO_8601_UTC>",
  "role": "user",
  "content": "DELIVER artifacts have been applied. Patch merged, release tagged <version>."
}
```
Or explicitly instruct the user to submit it through the GitHub Action.

This confirmation is required to mark the delivery as complete and close the state machine.
