# Test harness for 1217_minimum_cost_to_move_chips_to_the_same_position

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language python
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language javascript
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language typescript
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language java
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language cpp
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language c
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language go
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language rust
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language kotlin
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language swift
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language ruby
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language csharp
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language scala
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language php
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm java java 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm c c 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm go go 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm rust rust 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm swift swift 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm scala scala 1217_minimum_cost_to_move_chips_to_the_same_position
docker compose -f docker/docker-compose.yml run --rm php php 1217_minimum_cost_to_move_chips_to_the_same_position
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1217_minimum_cost_to_move_chips_to_the_same_position` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1217_minimum_cost_to_move_chips_to_the_same_position` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1217_minimum_cost_to_move_chips_to_the_same_position` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1217_minimum_cost_to_move_chips_to_the_same_position` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1217_minimum_cost_to_move_chips_to_the_same_position` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1217_minimum_cost_to_move_chips_to_the_same_position` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1217_minimum_cost_to_move_chips_to_the_same_position` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1217_minimum_cost_to_move_chips_to_the_same_position` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1217_minimum_cost_to_move_chips_to_the_same_position` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1217_minimum_cost_to_move_chips_to_the_same_position` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1217_minimum_cost_to_move_chips_to_the_same_position` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1217_minimum_cost_to_move_chips_to_the_same_position` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1217_minimum_cost_to_move_chips_to_the_same_position` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1217_minimum_cost_to_move_chips_to_the_same_position` |

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
.\scripts\test.ps1 -Folder 1217_minimum_cost_to_move_chips_to_the_same_position -AllLanguages
```

```bash
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --all-languages
```

```zsh
./scripts/test.sh --folder 1217_minimum_cost_to_move_chips_to_the_same_position --all-languages
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
