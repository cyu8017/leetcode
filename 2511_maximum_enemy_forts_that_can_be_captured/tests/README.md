# Test harness for 2511_maximum_enemy_forts_that_can_be_captured

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language python
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language javascript
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language typescript
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language java
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language cpp
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language c
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language go
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language rust
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language kotlin
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language swift
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language ruby
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language csharp
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language scala
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language php
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm java java 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm c c 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm go go 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm rust rust 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm swift swift 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm scala scala 2511_maximum_enemy_forts_that_can_be_captured
docker compose -f docker/docker-compose.yml run --rm php php 2511_maximum_enemy_forts_that_can_be_captured
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2511_maximum_enemy_forts_that_can_be_captured` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2511_maximum_enemy_forts_that_can_be_captured` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2511_maximum_enemy_forts_that_can_be_captured` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2511_maximum_enemy_forts_that_can_be_captured` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2511_maximum_enemy_forts_that_can_be_captured` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2511_maximum_enemy_forts_that_can_be_captured` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2511_maximum_enemy_forts_that_can_be_captured` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2511_maximum_enemy_forts_that_can_be_captured` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2511_maximum_enemy_forts_that_can_be_captured` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2511_maximum_enemy_forts_that_can_be_captured` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2511_maximum_enemy_forts_that_can_be_captured` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2511_maximum_enemy_forts_that_can_be_captured` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2511_maximum_enemy_forts_that_can_be_captured` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2511_maximum_enemy_forts_that_can_be_captured` |

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
.\scripts\test.ps1 -Folder 2511_maximum_enemy_forts_that_can_be_captured -AllLanguages
```

```bash
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --all-languages
```

```zsh
./scripts/test.sh --folder 2511_maximum_enemy_forts_that_can_be_captured --all-languages
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
