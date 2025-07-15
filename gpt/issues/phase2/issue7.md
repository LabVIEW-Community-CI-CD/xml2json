---
issue_id: 7
title: "Use Jest (not Mocha) for unit tests in VS Code extension"
phase: 2
status: open
tags: ["insight-synch", "testing", "vscode"]
created_at: "2025-07-10T09:10:00Z"
content_hash: f77568a5da6d9b96416614ca2357a7484d8ec4e6ca824895d5a3105c3f969d6c
---
The SRS specifies using Mocha for unit testing the VS Code extension, but SRS §7.2 NFR-E-4 requires Jest for unit tests (and Playwright for UI tests). Update the project accordingly:

- Change the test framework in the VS Code extension project from Mocha to Jest.
- Update any references in documentation or configuration files to reflect the use of Jest instead of Mocha.
