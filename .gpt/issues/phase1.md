### Accept exactly one input file argument (CLI invocation)
The utility must accept exactly one positional argument (`<input.vipb>`).  
If no argument or more than one is provided, it should display a usage error
message to **stderr** and exit with a non‑zero status.

**Acceptance Criteria**
- Exactly one `<input.vipb>` argument is accepted.
- On missing or extra arguments, print a usage error to **stderr** and exit non‑zero.

<!-- seed-trace: phase1.feature1 -->

---

### Default JSON output to standard output (stdout)
By default, the utility should write the JSON output to standard output
(`stdout`) without creating any output file.

**Acceptance Criteria**
- JSON output is written to `stdout` when no `--output` flag is specified.
- No output file is created unless explicitly requested.

<!-- seed-trace: phase1.feature2 -->
