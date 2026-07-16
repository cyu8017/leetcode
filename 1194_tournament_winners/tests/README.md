# Test harness for 1194_tournament_winners

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1194_tournament_winners -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1194_tournament_winners --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1194_tournament_winners --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1194_tournament_winners --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1194_tournament_winners --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1194_tournament_winners --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1194_tournament_winners --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1194_tournament_winners --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1194_tournament_winners --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1194_tournament_winners --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1194_tournament_winners --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1194_tournament_winners --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1194_tournament_winners --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1194_tournament_winners --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1194_tournament_winners --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1194_tournament_winners --language python
./scripts/test.sh --folder 1194_tournament_winners --language javascript
./scripts/test.sh --folder 1194_tournament_winners --language typescript
./scripts/test.sh --folder 1194_tournament_winners --language java
./scripts/test.sh --folder 1194_tournament_winners --language cpp
./scripts/test.sh --folder 1194_tournament_winners --language c
./scripts/test.sh --folder 1194_tournament_winners --language go
./scripts/test.sh --folder 1194_tournament_winners --language rust
./scripts/test.sh --folder 1194_tournament_winners --language kotlin
./scripts/test.sh --folder 1194_tournament_winners --language swift
./scripts/test.sh --folder 1194_tournament_winners --language ruby
./scripts/test.sh --folder 1194_tournament_winners --language csharp
./scripts/test.sh --folder 1194_tournament_winners --language scala
./scripts/test.sh --folder 1194_tournament_winners --language php
./scripts/test.sh --folder 1194_tournament_winners --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1194_tournament_winners --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1194_tournament_winners --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1194_tournament_winners --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1194_tournament_winners --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1194_tournament_winners --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1194_tournament_winners --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1194_tournament_winners --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1194_tournament_winners --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1194_tournament_winners --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1194_tournament_winners --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1194_tournament_winners --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1194_tournament_winners --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1194_tournament_winners --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1194_tournament_winners --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm java java 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm c c 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm go go 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm rust rust 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm swift swift 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm scala scala 1194_tournament_winners
docker compose -f docker/docker-compose.yml run --rm php php 1194_tournament_winners
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1194_tournament_winners` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1194_tournament_winners` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1194_tournament_winners` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1194_tournament_winners` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1194_tournament_winners` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1194_tournament_winners` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1194_tournament_winners` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1194_tournament_winners` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1194_tournament_winners` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1194_tournament_winners` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1194_tournament_winners` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1194_tournament_winners` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1194_tournament_winners` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1194_tournament_winners` |

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
.\scripts\test.ps1 -Folder 1194_tournament_winners -AllLanguages
```

```bash
./scripts/test.sh --folder 1194_tournament_winners --all-languages
```

```zsh
./scripts/test.sh --folder 1194_tournament_winners --all-languages
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
