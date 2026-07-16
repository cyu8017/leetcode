# Test harness for 1225_report_contiguous_dates

Run tests with **Docker only** — no local Python, Java, Node, or compilers required. Toolchain versions are pinned in `docker/docker-compose.yml`.

## One-time setup (repository root)

```powershell
docker compose -f docker/docker-compose.yml build
```

```bash
docker compose -f docker/docker-compose.yml build
```

```zsh
docker compose -f docker/docker-compose.yml build
```

## Run by language (Docker)

### Windows (`scripts/test.ps1`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1225_report_contiguous_dates --language python
./scripts/test.sh --folder 1225_report_contiguous_dates --language javascript
./scripts/test.sh --folder 1225_report_contiguous_dates --language typescript
./scripts/test.sh --folder 1225_report_contiguous_dates --language java
./scripts/test.sh --folder 1225_report_contiguous_dates --language cpp
./scripts/test.sh --folder 1225_report_contiguous_dates --language c
./scripts/test.sh --folder 1225_report_contiguous_dates --language go
./scripts/test.sh --folder 1225_report_contiguous_dates --language rust
./scripts/test.sh --folder 1225_report_contiguous_dates --language kotlin
./scripts/test.sh --folder 1225_report_contiguous_dates --language swift
./scripts/test.sh --folder 1225_report_contiguous_dates --language ruby
./scripts/test.sh --folder 1225_report_contiguous_dates --language csharp
./scripts/test.sh --folder 1225_report_contiguous_dates --language scala
./scripts/test.sh --folder 1225_report_contiguous_dates --language php
./scripts/test.sh --folder 1225_report_contiguous_dates --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1225_report_contiguous_dates --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm java java 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm c c 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm go go 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm rust rust 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm swift swift 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm scala scala 1225_report_contiguous_dates
docker compose -f docker/docker-compose.yml run --rm php php 1225_report_contiguous_dates
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1225_report_contiguous_dates` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1225_report_contiguous_dates` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1225_report_contiguous_dates` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1225_report_contiguous_dates` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1225_report_contiguous_dates` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1225_report_contiguous_dates` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1225_report_contiguous_dates` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1225_report_contiguous_dates` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1225_report_contiguous_dates` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1225_report_contiguous_dates` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1225_report_contiguous_dates` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1225_report_contiguous_dates` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1225_report_contiguous_dates` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1225_report_contiguous_dates` |

## Run from this folder (shortcuts)

Each `run_<language>.ps1` script in this directory calls Docker for you:

```powershell
.\run_python.ps1
.\run_javascript.ps1
.\run_java.ps1
.\run_cpp.ps1
# ... run_<language>.ps1 for all 14 languages
```

Run every language:

```powershell
.\run_all.ps1
```

Or from the repository root:

```powershell
.\scripts\test.ps1 -Folder 1225_report_contiguous_dates -AllLanguages
```

```bash
./scripts/test.sh --folder 1225_report_contiguous_dates --all-languages
```

```zsh
./scripts/test.sh --folder 1225_report_contiguous_dates --all-languages
```

## Files

| File | Purpose |
|------|---------|
| `config.json` | Solution class and method name |
| `cases.json` | Input/output test cases |
| `run_<language>.ps1` | Docker test launcher for one language |

## Add test cases

Edit `cases.json`:

```json
{
  "cases": [
    {
      "args": { "nums": [2, 7, 11, 15], "target": 9 },
      "expected": [0, 1]
    }
  ]
}
```

Update `config.json` with the correct LeetCode method name:

```json
{
  "class": "Solution",
  "method": "twoSum",
  "paramOrder": ["nums", "target"]
}
```

For linked lists and trees, use array notation and set types in `config.json`:

```json
{
  "class": "Solution",
  "method": "addTwoNumbers",
  "types": {
    "l1": "listnode",
    "l2": "listnode",
    "return": "listnode"
  }
}
```
