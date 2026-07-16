# Test harness for 3476_maximize_profit_from_task_assignment

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language python
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language javascript
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language typescript
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language java
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language cpp
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language c
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language go
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language rust
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language kotlin
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language swift
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language ruby
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language csharp
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language scala
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language php
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm java java 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm c c 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm go go 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm rust rust 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm swift swift 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm scala scala 3476_maximize_profit_from_task_assignment
docker compose -f docker/docker-compose.yml run --rm php php 3476_maximize_profit_from_task_assignment
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3476_maximize_profit_from_task_assignment` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3476_maximize_profit_from_task_assignment` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3476_maximize_profit_from_task_assignment` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3476_maximize_profit_from_task_assignment` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3476_maximize_profit_from_task_assignment` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3476_maximize_profit_from_task_assignment` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3476_maximize_profit_from_task_assignment` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3476_maximize_profit_from_task_assignment` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3476_maximize_profit_from_task_assignment` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3476_maximize_profit_from_task_assignment` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3476_maximize_profit_from_task_assignment` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3476_maximize_profit_from_task_assignment` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3476_maximize_profit_from_task_assignment` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3476_maximize_profit_from_task_assignment` |

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
.\scripts\test.ps1 -Folder 3476_maximize_profit_from_task_assignment -AllLanguages
```

```bash
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --all-languages
```

```zsh
./scripts/test.sh --folder 3476_maximize_profit_from_task_assignment --all-languages
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
