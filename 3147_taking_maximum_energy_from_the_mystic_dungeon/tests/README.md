# Test harness for 3147_taking_maximum_energy_from_the_mystic_dungeon

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language python
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language javascript
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language typescript
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language java
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language cpp
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language c
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language go
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language rust
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language kotlin
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language swift
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language ruby
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language csharp
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language scala
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language php
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm java java 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm c c 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm go go 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm rust rust 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm swift swift 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm scala scala 3147_taking_maximum_energy_from_the_mystic_dungeon
docker compose -f docker/docker-compose.yml run --rm php php 3147_taking_maximum_energy_from_the_mystic_dungeon
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3147_taking_maximum_energy_from_the_mystic_dungeon` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3147_taking_maximum_energy_from_the_mystic_dungeon` |

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
.\scripts\test.ps1 -Folder 3147_taking_maximum_energy_from_the_mystic_dungeon -AllLanguages
```

```bash
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --all-languages
```

```zsh
./scripts/test.sh --folder 3147_taking_maximum_energy_from_the_mystic_dungeon --all-languages
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
