# Test harness for 0618_students_report_by_geography

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0618_students_report_by_geography -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0618_students_report_by_geography --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0618_students_report_by_geography --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0618_students_report_by_geography --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0618_students_report_by_geography --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0618_students_report_by_geography --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0618_students_report_by_geography --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0618_students_report_by_geography --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0618_students_report_by_geography --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0618_students_report_by_geography --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0618_students_report_by_geography --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0618_students_report_by_geography --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0618_students_report_by_geography --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0618_students_report_by_geography --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0618_students_report_by_geography --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0618_students_report_by_geography --language python
./scripts/test.sh --folder 0618_students_report_by_geography --language javascript
./scripts/test.sh --folder 0618_students_report_by_geography --language typescript
./scripts/test.sh --folder 0618_students_report_by_geography --language java
./scripts/test.sh --folder 0618_students_report_by_geography --language cpp
./scripts/test.sh --folder 0618_students_report_by_geography --language c
./scripts/test.sh --folder 0618_students_report_by_geography --language go
./scripts/test.sh --folder 0618_students_report_by_geography --language rust
./scripts/test.sh --folder 0618_students_report_by_geography --language kotlin
./scripts/test.sh --folder 0618_students_report_by_geography --language swift
./scripts/test.sh --folder 0618_students_report_by_geography --language ruby
./scripts/test.sh --folder 0618_students_report_by_geography --language csharp
./scripts/test.sh --folder 0618_students_report_by_geography --language scala
./scripts/test.sh --folder 0618_students_report_by_geography --language php
./scripts/test.sh --folder 0618_students_report_by_geography --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0618_students_report_by_geography --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0618_students_report_by_geography --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0618_students_report_by_geography --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0618_students_report_by_geography --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0618_students_report_by_geography --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0618_students_report_by_geography --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0618_students_report_by_geography --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0618_students_report_by_geography --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0618_students_report_by_geography --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0618_students_report_by_geography --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0618_students_report_by_geography --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0618_students_report_by_geography --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0618_students_report_by_geography --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0618_students_report_by_geography --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm java java 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm c c 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm go go 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm rust rust 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm swift swift 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm scala scala 0618_students_report_by_geography
docker compose -f docker/docker-compose.yml run --rm php php 0618_students_report_by_geography
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0618_students_report_by_geography` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0618_students_report_by_geography` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0618_students_report_by_geography` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0618_students_report_by_geography` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0618_students_report_by_geography` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0618_students_report_by_geography` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0618_students_report_by_geography` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0618_students_report_by_geography` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0618_students_report_by_geography` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0618_students_report_by_geography` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0618_students_report_by_geography` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0618_students_report_by_geography` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0618_students_report_by_geography` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0618_students_report_by_geography` |

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
.\scripts\test.ps1 -Folder 0618_students_report_by_geography -AllLanguages
```

```bash
./scripts/test.sh --folder 0618_students_report_by_geography --all-languages
```

```zsh
./scripts/test.sh --folder 0618_students_report_by_geography --all-languages
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
