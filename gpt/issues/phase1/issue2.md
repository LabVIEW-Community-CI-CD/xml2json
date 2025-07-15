---
issue_id: 2
title: "Create automated test cases (xUnit) for VipbJsonTool"
phase: 1
status: open
tags: ["testing", "xunit", "vipbjsontool"]
created_at: "2025-07-08T12:05:00Z"
content_hash: 35de07580c387b9ba236b7852c634d28e8376d8041f27789823533711eb0c81c
---
Implement unit and integration tests using xUnit to ensure the VipbJsonTool works correctly. Test cases should cover:

- **vipb2json Conversion:** Verify that valid .vipb files are correctly converted to JSON. Include tests for edge cases (missing elements, optional fields).
- **json2vipb Conversion:** Confirm that JSON files (including those patched) convert back to equivalent .vipb XML.
- **patch2vipb Functionality:** Test applying YAML patches to JSON and regenerating the .vipb, ensuring only intended changes occur.
- **Error Handling:** Ensure invalid inputs or modes produce the expected error codes (as per SRS UI-2), and error messages are informative.
- **Sample Fixtures:** Provide sample .vipb and JSON files in a `tests/fixtures` directory for use in these tests.
