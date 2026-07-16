# Test harness for 1105_filling_bookcase_shelves

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language python
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language javascript
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language typescript
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language java
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language cpp
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language c
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language go
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language rust
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language kotlin
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language swift
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language ruby
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language csharp
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language scala
./scripts/test.sh --folder 1105_filling_bookcase_shelves --language php
./scripts/test.sh --folder 1105_filling_bookcase_shelves --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1105_filling_bookcase_shelves --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm java java 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm c c 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm go go 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm rust rust 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm swift swift 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm scala scala 1105_filling_bookcase_shelves
docker compose -f docker/docker-compose.yml run --rm php php 1105_filling_bookcase_shelves
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1105_filling_bookcase_shelves` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1105_filling_bookcase_shelves` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1105_filling_bookcase_shelves` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1105_filling_bookcase_shelves` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1105_filling_bookcase_shelves` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1105_filling_bookcase_shelves` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1105_filling_bookcase_shelves` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1105_filling_bookcase_shelves` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1105_filling_bookcase_shelves` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1105_filling_bookcase_shelves` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1105_filling_bookcase_shelves` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1105_filling_bookcase_shelves` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1105_filling_bookcase_shelves` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1105_filling_bookcase_shelves` |

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
.\scripts\test.ps1 -Folder 1105_filling_bookcase_shelves -AllLanguages
```

```bash
./scripts/test.sh --folder 1105_filling_bookcase_shelves --all-languages
```

```zsh
./scripts/test.sh --folder 1105_filling_bookcase_shelves --all-languages
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
