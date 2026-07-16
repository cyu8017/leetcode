# Test harness for 0856_score_of_parentheses

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0856_score_of_parentheses -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0856_score_of_parentheses --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0856_score_of_parentheses --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0856_score_of_parentheses --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0856_score_of_parentheses --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0856_score_of_parentheses --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0856_score_of_parentheses --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0856_score_of_parentheses --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0856_score_of_parentheses --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0856_score_of_parentheses --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0856_score_of_parentheses --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0856_score_of_parentheses --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0856_score_of_parentheses --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0856_score_of_parentheses --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0856_score_of_parentheses --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0856_score_of_parentheses --language python
./scripts/test.sh --folder 0856_score_of_parentheses --language javascript
./scripts/test.sh --folder 0856_score_of_parentheses --language typescript
./scripts/test.sh --folder 0856_score_of_parentheses --language java
./scripts/test.sh --folder 0856_score_of_parentheses --language cpp
./scripts/test.sh --folder 0856_score_of_parentheses --language c
./scripts/test.sh --folder 0856_score_of_parentheses --language go
./scripts/test.sh --folder 0856_score_of_parentheses --language rust
./scripts/test.sh --folder 0856_score_of_parentheses --language kotlin
./scripts/test.sh --folder 0856_score_of_parentheses --language swift
./scripts/test.sh --folder 0856_score_of_parentheses --language ruby
./scripts/test.sh --folder 0856_score_of_parentheses --language csharp
./scripts/test.sh --folder 0856_score_of_parentheses --language scala
./scripts/test.sh --folder 0856_score_of_parentheses --language php
./scripts/test.sh --folder 0856_score_of_parentheses --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0856_score_of_parentheses --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0856_score_of_parentheses --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0856_score_of_parentheses --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0856_score_of_parentheses --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0856_score_of_parentheses --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0856_score_of_parentheses --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0856_score_of_parentheses --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0856_score_of_parentheses --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0856_score_of_parentheses --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0856_score_of_parentheses --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0856_score_of_parentheses --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0856_score_of_parentheses --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0856_score_of_parentheses --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0856_score_of_parentheses --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm java java 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm c c 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm go go 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm rust rust 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm swift swift 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm scala scala 0856_score_of_parentheses
docker compose -f docker/docker-compose.yml run --rm php php 0856_score_of_parentheses
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0856_score_of_parentheses` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0856_score_of_parentheses` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0856_score_of_parentheses` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0856_score_of_parentheses` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0856_score_of_parentheses` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0856_score_of_parentheses` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0856_score_of_parentheses` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0856_score_of_parentheses` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0856_score_of_parentheses` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0856_score_of_parentheses` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0856_score_of_parentheses` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0856_score_of_parentheses` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0856_score_of_parentheses` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0856_score_of_parentheses` |

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
.\scripts\test.ps1 -Folder 0856_score_of_parentheses -AllLanguages
```

```bash
./scripts/test.sh --folder 0856_score_of_parentheses --all-languages
```

```zsh
./scripts/test.sh --folder 0856_score_of_parentheses --all-languages
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
