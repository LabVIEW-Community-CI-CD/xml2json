
# Software Requirements Specification (SRS) – **xml2json**
**Version 1.0 – 14 Jul 2025**

## 1  Introduction
The **xml2json** utility is a stand‑alone command‑line program that converts a single VI Package Build (`.vipb`) file (an XML document) into an equivalent JSON representation.  
It will be used in CI pipelines and by developers, runs on .NET 8 without any NI/LabVIEW dependencies, and produces deterministic, RFC 8259‑compliant JSON.

## 2  System Overview
### 2.1  Product Perspective  
* Stand‑alone .NET CLI, invoked by scripts or terminals  
* Reads one `.vipb` file (opaque XML) ➜ writes JSON  
* No GUI; interacts only via command‑line args + stdout/stderr  
* Existing CI workflows will call it; interface must remain stable

### 2.2  Product Functions  
| ID | Function | Brief Description |
|----|----------|-------------------|
| F‑1 | Input processing | Accept exactly one positional path to a `.vipb`. Validate existence/readability. |
| F‑2 | XML→JSON conversion | Parse the XML using built‑in .NET libraries and build a JSON object containing **all** data. |
| F‑3 | Output routing | Write JSON to **stdout** by default, or to a file when `--output <file>` is supplied. No duplication. |
| F‑4 | Help / usage | `-h / --help` prints usage text and exits. |
| F‑5 | Error handling | On any error (missing file, invalid XML, runtime failure) print message to **stderr**, produce **no JSON**, exit non‑zero. |
| F‑6 | Exit codes | `0` = success; non‑zero = any failure. |

### 2.3  Users  
* **CI systems** – need non‑interactive operation and reliable exit codes  
* **Developers** – expect concise usage & error messages (English only)

### 2.4  Constraints & Assumptions  
* .NET 8 runtime only; zero NI/LabVIEW dependencies  
* Reads **one** file per run; never mutates input  
* Outputs JSON only; format must be deterministic  
* Runs fully offline; no network or external services

## 3  Functional Requirements
1. **CLI invocation** accepts one positional `<input.vipb>`; missing ⇒ usage error.  
2. **Default output**: JSON → stdout.  
3. `--output <file>` flag writes JSON exclusively to that file.  
4. **File not found** ⇒ stderr *“Input file not found”*, exit ≠ 0, no JSON.  
5. **Invalid XML** ⇒ stderr *“Invalid VIPB format”*, exit ≠ 0.  
6. **Other runtime errors** handled similarly; never crash.  
7. **Help flag** prints usage and exits (code 0).  

## 4  Non‑Functional Requirements
* **Correctness:** JSON fully represents input; deterministic byte‑for‑byte for same input/tool version.  
* **Usability:** Familiar flags, clear English messages; minimal setup.  
* **Reliability:** No hangs; catches exceptions; leaves no partial files.  
* **Performance:** Convert ~200 KB file in ≤ 2 s on typical CI runner; < 128 MB RAM.  
* **Portability:** Works on Windows, Linux, macOS with .NET 8; headless operation.  
* **Maintainability:** Modular (CLI, converter, output); documented; open‑source dependencies only.

## 5  Glossary
* **`.vipb`** – VI Package Build file (XML)  
* **CLI** – Command‑Line Interface  
* **JSON** – JavaScript Object Notation  
* **stdout / stderr** – Standard output / error streams  
* **Deterministic** – Same input → identical output every run
