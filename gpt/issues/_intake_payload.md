**Phase 1 – Issue 1**

# Generate developer-oriented documentation for VipbJsonTool

The tool needs comprehensive developer documentation to explain its usage and design. This should include:

- **Overview and Purpose:** A high‑level description of VipbJsonTool and its role in the CI/CD pipeline.  
- **Usage Guide:** Instructions for building and running the tool, including command‑line examples for `vipb2json`, `json2vipb`, and `patch2vipb` modes.  
- **Architecture and Design:** Explanation of the code structure and key components (e.g., `JsonToXmlConverter`, `PatchApplier`).  
- **Configuration and Dependencies:** Details on required .NET runtime, libraries, and how environment variables (e.g., `GITHUB_TOKEN`) are used.  
- **Examples:** Example workflows showing how to apply patches and automate commits, with sample input and output.

<!--
issue_id: 1
title: "Generate developer-oriented documentation for VipbJsonTool"
phase: 1
status: open
tags: ["documentation", "vipbjsontool"]
created_at: "2025-07-08T12:00:00Z"
content_hash: 0f9e7e81fb132914a8aaa42456ee0bed9cc1ffb21ec64c501347e529f781d8a1
-->

---

**Phase 1 – Issue 2**

# Create automated test cases (xUnit) for VipbJsonTool

Implement unit and integration tests using xUnit to ensure the VipbJsonTool works correctly. Test cases should cover:

- **vipb2json Conversion:** Verify that valid .vipb files are correctly converted to JSON, including edge cases (missing elements, optional fields).  
- **json2vipb Conversion:** Confirm that JSON files (including patched ones) convert back to equivalent .vipb XML.  
- **patch2vipb Functionality:** Test applying YAML patches to JSON and regenerating the .vipb, ensuring only intended changes occur.  
- **Error Handling:** Ensure invalid inputs or modes produce the expected error codes (per SRS UI‑2) and informative messages.  
- **Sample Fixtures:** Provide sample .vipb and JSON files in a `tests/fixtures` directory for use in these tests.

<!--
issue_id: 2
title: "Create automated test cases (xUnit) for VipbJsonTool"
phase: 1
status: open
tags: ["testing", "xunit", "vipbjsontool"]
created_at: "2025-07-08T12:05:00Z"
content_hash: 35de07580c387b9ba236b7852c634d28e8376d8041f27789823533711eb0c81c
-->

---

**Phase 1 – Issue 3**

# Add CLI usage examples and guidance

Provide command‑line examples demonstrating VipbJsonTool in common scenarios:

- Example commands for each mode (`vipb2json`, `json2vipb`, `patch2vipb`) showing typical input/output arguments.  
- Examples of applying YAML patch files with `patch2vipb`.  
- Scenarios including optional parameters `alwaysPatch`, `branchName`, and `autoPr`.  
- Explain expected behavior and output for each example.  
- Add these examples to the README or a dedicated `docs/usage.md`.

<!--
issue_id: 3
title: "Add CLI usage examples and guidance"
phase: 1
status: open
tags: ["documentation", "cli", "examples"]
created_at: "2025-07-08T12:10:00Z"
content_hash: 9f8c54acac560e370754134a0b90bc37054e2b9c73bca9114cfc33c19e78a2ab
-->

---

**Phase 1 – Issue 4**

# Export the SRS to PDF and other formats

The Software Requirements Specification should be distributed in multiple formats:

- **PDF:** Print‑friendly version.  
- **Rich Text or reStructuredText:** (if applicable) for other doc systems.  
- Preserve table of contents, headings, and tables.  
- Ensure all links/reference URLs resolve correctly.

<!--
issue_id: 4
title: "Export the SRS to PDF and other formats"
phase: 1
status: open
tags: ["documentation", "formatting", "SRS"]
created_at: "2025-07-08T12:15:00Z"
content_hash: 1348cd2b8d530394181d9995f7526739a5dbb492578fa1af46ec988b952758ee
-->

---

**Phase 2 – Issue 5**

# Change pre‑commit hook to validate‑only (no editor spawn)

The SRS currently describes the pre‑commit hook as spawning an editor to insert the insight payload. Per SRS §3.1 FR‑2, the hook should **validate** an already‑inserted payload **without** opening an editor. Update requirements to:

- Remove wording that suggests opening an editor.  
- Clarify that the hook is validate‑only: it checks the payload and aborts on mismatch.

<!--
issue_id: 5
title: "Change pre-commit hook to validate-only (no editor spawn)"
phase: 2
status: open
tags: ["insight-synch", "srs", "hook"]
created_at: "2025-07-10T09:00:00Z"
content_hash: 44b754a85054e2dac52d16de240e16c9b7530fef1a45d1ea57fec5f75322c58d
-->

---

**Phase 2 – Issue 6**

# Update deliverable wording to remove Marketplace publication

The SRS mentions publishing the VS Code extension to the Marketplace by T+25 days. SRS §7.2 NFR‑E‑2 requires side‑loading only. Update the deliverables section:

- Remove all references to Marketplace publication.  
- State that the `.vsix` will be packaged and distributed via the internal artifact feed.

<!--
issue_id: 6
title: "Update deliverable wording to remove Marketplace publication"
phase: 2
status: open
tags: ["insight-synch", "deliverables", "vscext"]
created_at: "2025-07-10T09:05:00Z"
content_hash: 4e9e2b32d59f99b1331c8a9d009aa226295c5be85f78e87bf1f621063e6d8900
-->

---

**Phase 2 – Issue 7**

# Use Jest (not Mocha) for unit tests in VS Code extension

SRS requires Jest for unit tests (and Playwright for UI tests). Update the project:

- Replace Mocha with Jest for unit testing.  
- Update docs and configs to reflect Jest instead of Mocha.

<!--
issue_id: 7
title: "Use Jest (not Mocha) for unit tests in VS Code extension"
phase: 2
status: open
tags: ["insight-synch", "testing", "vscode"]
created_at: "2025-07-10T09:10:00Z"
content_hash: f77568a5da6d9b96416614ca2357a7484d8ec4e6ca824895d5a3105c3f969d6c
-->
