### Support `--output <file>` option to write JSON to a file
Add a `--output <file>` command‑line option. When provided, the utility
should write the JSON output exclusively to the specified file instead of
`stdout`. If writing fails (e.g., permission denied), print an error to
**stderr** and exit non‑zero.

**Acceptance Criteria**
- If `--output <file>` is given, JSON is written to that file.
- When the file cannot be written, print an error to **stderr** and exit non‑zero.
- When `--output` is absent, behavior remains as in Phase 1 (JSON to `stdout`).

<!-- seed-trace: phase2.feature1 -->

---

### Implement help flag (`-h` / `--help`)
Support a `-h` or `--help` flag. If used, display usage instructions
(command syntax and options) to **stdout** and then exit with status 0.
No conversion should occur when help is requested.

**Acceptance Criteria**
- On `-h` or `--help`, print usage to `stdout` and exit with code 0.
- No JSON conversion or file output occurs when help is requested.

<!-- seed-trace: phase2.feature2 -->
