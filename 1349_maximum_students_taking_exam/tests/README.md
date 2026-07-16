# Test harness for 1349_maximum_students_taking_exam

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language python
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language javascript
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language typescript
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language java
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language cpp
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language c
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language go
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language rust
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language kotlin
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language swift
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language ruby
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language csharp
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language scala
./scripts/test.sh --folder 1349_maximum_students_taking_exam --language php
./scripts/test.sh --folder 1349_maximum_students_taking_exam --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1349_maximum_students_taking_exam --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm java java 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm c c 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm go go 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm rust rust 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm swift swift 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm scala scala 1349_maximum_students_taking_exam
docker compose -f docker/docker-compose.yml run --rm php php 1349_maximum_students_taking_exam
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1349_maximum_students_taking_exam` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1349_maximum_students_taking_exam` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1349_maximum_students_taking_exam` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1349_maximum_students_taking_exam` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1349_maximum_students_taking_exam` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1349_maximum_students_taking_exam` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1349_maximum_students_taking_exam` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1349_maximum_students_taking_exam` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1349_maximum_students_taking_exam` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1349_maximum_students_taking_exam` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1349_maximum_students_taking_exam` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1349_maximum_students_taking_exam` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1349_maximum_students_taking_exam` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1349_maximum_students_taking_exam` |

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
.\scripts\test.ps1 -Folder 1349_maximum_students_taking_exam -AllLanguages
```

```bash
./scripts/test.sh --folder 1349_maximum_students_taking_exam --all-languages
```

```zsh
./scripts/test.sh --folder 1349_maximum_students_taking_exam --all-languages
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
