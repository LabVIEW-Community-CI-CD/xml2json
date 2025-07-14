### Handle missing input file error
If the input file does not exist or cannot be opened, print
“Input file not found” to **stderr**, exit non‑zero, and produce no JSON.

**Acceptance Criteria**
- On missing/unreadable file, print “Input file not found” to **stderr**.
- Exit with a non‑zero code and produce no JSON output.

<!-- seed-trace: phase3.feature1 -->

---

### Handle invalid VIPB/XML format error
If the input file is found but contains malformed XML or is not a valid
`.vipb`, print “Invalid VIPB format” to **stderr**, exit non‑zero, and
produce no JSON.

**Acceptance Criteria**
- On malformed XML, print “Invalid VIPB format” to **stderr**.
- Exit non‑zero and produce no JSON output.

<!-- seed-trace: phase3.feature2 -->

---

### Catch and handle unexpected runtime errors
Ensure any other runtime exceptions (I/O errors, out‑of‑memory, etc.) are
caught. Print a clear error to **stderr**, exit non‑zero, and do not
produce JSON.

**Acceptance Criteria**
- All unexpected exceptions are caught and logged to **stderr**.
- Exit with a non‑zero code and emit no JSON in such cases.

<!-- seed-trace: phase3.feature3 -->
