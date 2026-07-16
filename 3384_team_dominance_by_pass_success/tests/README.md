# Test harness for 3384_team_dominance_by_pass_success

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language python
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language javascript
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language typescript
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language java
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language cpp
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language c
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language go
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language rust
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language kotlin
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language swift
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language ruby
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language csharp
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language scala
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language php
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3384_team_dominance_by_pass_success --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm java java 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm c c 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm go go 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm rust rust 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm swift swift 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm scala scala 3384_team_dominance_by_pass_success
docker compose -f docker/docker-compose.yml run --rm php php 3384_team_dominance_by_pass_success
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3384_team_dominance_by_pass_success` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3384_team_dominance_by_pass_success` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3384_team_dominance_by_pass_success` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3384_team_dominance_by_pass_success` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3384_team_dominance_by_pass_success` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3384_team_dominance_by_pass_success` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3384_team_dominance_by_pass_success` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3384_team_dominance_by_pass_success` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3384_team_dominance_by_pass_success` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3384_team_dominance_by_pass_success` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3384_team_dominance_by_pass_success` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3384_team_dominance_by_pass_success` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3384_team_dominance_by_pass_success` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3384_team_dominance_by_pass_success` |

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
.\scripts\test.ps1 -Folder 3384_team_dominance_by_pass_success -AllLanguages
```

```bash
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --all-languages
```

```zsh
./scripts/test.sh --folder 3384_team_dominance_by_pass_success --all-languages
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
