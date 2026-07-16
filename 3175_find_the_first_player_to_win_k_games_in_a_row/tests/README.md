# Test harness for 3175_find_the_first_player_to_win_k_games_in_a_row

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language python
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language javascript
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language typescript
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language java
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language cpp
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language c
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language go
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language rust
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language kotlin
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language swift
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language ruby
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language csharp
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language scala
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language php
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm java java 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm c c 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm go go 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm rust rust 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm swift swift 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm scala scala 3175_find_the_first_player_to_win_k_games_in_a_row
docker compose -f docker/docker-compose.yml run --rm php php 3175_find_the_first_player_to_win_k_games_in_a_row
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3175_find_the_first_player_to_win_k_games_in_a_row` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3175_find_the_first_player_to_win_k_games_in_a_row` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3175_find_the_first_player_to_win_k_games_in_a_row` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3175_find_the_first_player_to_win_k_games_in_a_row` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3175_find_the_first_player_to_win_k_games_in_a_row` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3175_find_the_first_player_to_win_k_games_in_a_row` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3175_find_the_first_player_to_win_k_games_in_a_row` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3175_find_the_first_player_to_win_k_games_in_a_row` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3175_find_the_first_player_to_win_k_games_in_a_row` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3175_find_the_first_player_to_win_k_games_in_a_row` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3175_find_the_first_player_to_win_k_games_in_a_row` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3175_find_the_first_player_to_win_k_games_in_a_row` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3175_find_the_first_player_to_win_k_games_in_a_row` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3175_find_the_first_player_to_win_k_games_in_a_row` |

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
.\scripts\test.ps1 -Folder 3175_find_the_first_player_to_win_k_games_in_a_row -AllLanguages
```

```bash
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --all-languages
```

```zsh
./scripts/test.sh --folder 3175_find_the_first_player_to_win_k_games_in_a_row --all-languages
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
