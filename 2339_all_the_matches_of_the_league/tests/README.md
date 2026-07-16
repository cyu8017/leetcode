# Test harness for 2339_all_the_matches_of_the_league

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language python
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language javascript
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language typescript
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language java
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language cpp
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language c
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language go
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language rust
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language kotlin
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language swift
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language ruby
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language csharp
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language scala
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language php
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2339_all_the_matches_of_the_league --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm java java 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm c c 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm go go 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm rust rust 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm swift swift 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm scala scala 2339_all_the_matches_of_the_league
docker compose -f docker/docker-compose.yml run --rm php php 2339_all_the_matches_of_the_league
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2339_all_the_matches_of_the_league` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2339_all_the_matches_of_the_league` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2339_all_the_matches_of_the_league` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2339_all_the_matches_of_the_league` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2339_all_the_matches_of_the_league` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2339_all_the_matches_of_the_league` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2339_all_the_matches_of_the_league` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2339_all_the_matches_of_the_league` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2339_all_the_matches_of_the_league` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2339_all_the_matches_of_the_league` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2339_all_the_matches_of_the_league` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2339_all_the_matches_of_the_league` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2339_all_the_matches_of_the_league` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2339_all_the_matches_of_the_league` |

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
.\scripts\test.ps1 -Folder 2339_all_the_matches_of_the_league -AllLanguages
```

```bash
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --all-languages
```

```zsh
./scripts/test.sh --folder 2339_all_the_matches_of_the_league --all-languages
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
