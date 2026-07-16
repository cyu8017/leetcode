# Test harness for 1366_rank_teams_by_votes

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1366_rank_teams_by_votes --language python
./scripts/test.sh --folder 1366_rank_teams_by_votes --language javascript
./scripts/test.sh --folder 1366_rank_teams_by_votes --language typescript
./scripts/test.sh --folder 1366_rank_teams_by_votes --language java
./scripts/test.sh --folder 1366_rank_teams_by_votes --language cpp
./scripts/test.sh --folder 1366_rank_teams_by_votes --language c
./scripts/test.sh --folder 1366_rank_teams_by_votes --language go
./scripts/test.sh --folder 1366_rank_teams_by_votes --language rust
./scripts/test.sh --folder 1366_rank_teams_by_votes --language kotlin
./scripts/test.sh --folder 1366_rank_teams_by_votes --language swift
./scripts/test.sh --folder 1366_rank_teams_by_votes --language ruby
./scripts/test.sh --folder 1366_rank_teams_by_votes --language csharp
./scripts/test.sh --folder 1366_rank_teams_by_votes --language scala
./scripts/test.sh --folder 1366_rank_teams_by_votes --language php
./scripts/test.sh --folder 1366_rank_teams_by_votes --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1366_rank_teams_by_votes --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm java java 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm c c 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm go go 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm rust rust 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm swift swift 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm scala scala 1366_rank_teams_by_votes
docker compose -f docker/docker-compose.yml run --rm php php 1366_rank_teams_by_votes
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1366_rank_teams_by_votes` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1366_rank_teams_by_votes` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1366_rank_teams_by_votes` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1366_rank_teams_by_votes` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1366_rank_teams_by_votes` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1366_rank_teams_by_votes` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1366_rank_teams_by_votes` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1366_rank_teams_by_votes` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1366_rank_teams_by_votes` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1366_rank_teams_by_votes` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1366_rank_teams_by_votes` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1366_rank_teams_by_votes` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1366_rank_teams_by_votes` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1366_rank_teams_by_votes` |

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
.\scripts\test.ps1 -Folder 1366_rank_teams_by_votes -AllLanguages
```

```bash
./scripts/test.sh --folder 1366_rank_teams_by_votes --all-languages
```

```zsh
./scripts/test.sh --folder 1366_rank_teams_by_votes --all-languages
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
