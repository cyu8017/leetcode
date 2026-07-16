# Test harness for 1900_the_earliest_and_latest_rounds_where_players_compete

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language python
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language javascript
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language typescript
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language java
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language cpp
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language c
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language go
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language rust
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language kotlin
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language swift
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language ruby
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language csharp
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language scala
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language php
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm java java 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm c c 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm go go 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm rust rust 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm swift swift 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm scala scala 1900_the_earliest_and_latest_rounds_where_players_compete
docker compose -f docker/docker-compose.yml run --rm php php 1900_the_earliest_and_latest_rounds_where_players_compete
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1900_the_earliest_and_latest_rounds_where_players_compete` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1900_the_earliest_and_latest_rounds_where_players_compete` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1900_the_earliest_and_latest_rounds_where_players_compete` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1900_the_earliest_and_latest_rounds_where_players_compete` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1900_the_earliest_and_latest_rounds_where_players_compete` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1900_the_earliest_and_latest_rounds_where_players_compete` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1900_the_earliest_and_latest_rounds_where_players_compete` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1900_the_earliest_and_latest_rounds_where_players_compete` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1900_the_earliest_and_latest_rounds_where_players_compete` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1900_the_earliest_and_latest_rounds_where_players_compete` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1900_the_earliest_and_latest_rounds_where_players_compete` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1900_the_earliest_and_latest_rounds_where_players_compete` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1900_the_earliest_and_latest_rounds_where_players_compete` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1900_the_earliest_and_latest_rounds_where_players_compete` |

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
.\scripts\test.ps1 -Folder 1900_the_earliest_and_latest_rounds_where_players_compete -AllLanguages
```

```bash
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --all-languages
```

```zsh
./scripts/test.sh --folder 1900_the_earliest_and_latest_rounds_where_players_compete --all-languages
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
