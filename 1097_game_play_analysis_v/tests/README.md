# Test harness for 1097_game_play_analysis_v

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1097_game_play_analysis_v --language python
./scripts/test.sh --folder 1097_game_play_analysis_v --language javascript
./scripts/test.sh --folder 1097_game_play_analysis_v --language typescript
./scripts/test.sh --folder 1097_game_play_analysis_v --language java
./scripts/test.sh --folder 1097_game_play_analysis_v --language cpp
./scripts/test.sh --folder 1097_game_play_analysis_v --language c
./scripts/test.sh --folder 1097_game_play_analysis_v --language go
./scripts/test.sh --folder 1097_game_play_analysis_v --language rust
./scripts/test.sh --folder 1097_game_play_analysis_v --language kotlin
./scripts/test.sh --folder 1097_game_play_analysis_v --language swift
./scripts/test.sh --folder 1097_game_play_analysis_v --language ruby
./scripts/test.sh --folder 1097_game_play_analysis_v --language csharp
./scripts/test.sh --folder 1097_game_play_analysis_v --language scala
./scripts/test.sh --folder 1097_game_play_analysis_v --language php
./scripts/test.sh --folder 1097_game_play_analysis_v --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1097_game_play_analysis_v --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm java java 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm c c 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm go go 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm rust rust 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm swift swift 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm scala scala 1097_game_play_analysis_v
docker compose -f docker/docker-compose.yml run --rm php php 1097_game_play_analysis_v
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1097_game_play_analysis_v` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1097_game_play_analysis_v` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1097_game_play_analysis_v` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1097_game_play_analysis_v` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1097_game_play_analysis_v` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1097_game_play_analysis_v` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1097_game_play_analysis_v` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1097_game_play_analysis_v` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1097_game_play_analysis_v` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1097_game_play_analysis_v` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1097_game_play_analysis_v` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1097_game_play_analysis_v` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1097_game_play_analysis_v` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1097_game_play_analysis_v` |

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
.\scripts\test.ps1 -Folder 1097_game_play_analysis_v -AllLanguages
```

```bash
./scripts/test.sh --folder 1097_game_play_analysis_v --all-languages
```

```zsh
./scripts/test.sh --folder 1097_game_play_analysis_v --all-languages
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
