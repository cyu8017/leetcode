# Test harness for 1244_design_a_leaderboard

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1244_design_a_leaderboard --language python
./scripts/test.sh --folder 1244_design_a_leaderboard --language javascript
./scripts/test.sh --folder 1244_design_a_leaderboard --language typescript
./scripts/test.sh --folder 1244_design_a_leaderboard --language java
./scripts/test.sh --folder 1244_design_a_leaderboard --language cpp
./scripts/test.sh --folder 1244_design_a_leaderboard --language c
./scripts/test.sh --folder 1244_design_a_leaderboard --language go
./scripts/test.sh --folder 1244_design_a_leaderboard --language rust
./scripts/test.sh --folder 1244_design_a_leaderboard --language kotlin
./scripts/test.sh --folder 1244_design_a_leaderboard --language swift
./scripts/test.sh --folder 1244_design_a_leaderboard --language ruby
./scripts/test.sh --folder 1244_design_a_leaderboard --language csharp
./scripts/test.sh --folder 1244_design_a_leaderboard --language scala
./scripts/test.sh --folder 1244_design_a_leaderboard --language php
./scripts/test.sh --folder 1244_design_a_leaderboard --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1244_design_a_leaderboard --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm java java 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm c c 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm go go 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm rust rust 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm swift swift 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm scala scala 1244_design_a_leaderboard
docker compose -f docker/docker-compose.yml run --rm php php 1244_design_a_leaderboard
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1244_design_a_leaderboard` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1244_design_a_leaderboard` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1244_design_a_leaderboard` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1244_design_a_leaderboard` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1244_design_a_leaderboard` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1244_design_a_leaderboard` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1244_design_a_leaderboard` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1244_design_a_leaderboard` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1244_design_a_leaderboard` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1244_design_a_leaderboard` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1244_design_a_leaderboard` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1244_design_a_leaderboard` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1244_design_a_leaderboard` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1244_design_a_leaderboard` |

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
.\scripts\test.ps1 -Folder 1244_design_a_leaderboard -AllLanguages
```

```bash
./scripts/test.sh --folder 1244_design_a_leaderboard --all-languages
```

```zsh
./scripts/test.sh --folder 1244_design_a_leaderboard --all-languages
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
