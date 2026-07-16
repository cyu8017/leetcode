# Test harness for 0289_game_of_life

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0289_game_of_life -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0289_game_of_life --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0289_game_of_life --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0289_game_of_life --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0289_game_of_life --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0289_game_of_life --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0289_game_of_life --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0289_game_of_life --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0289_game_of_life --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0289_game_of_life --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0289_game_of_life --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0289_game_of_life --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0289_game_of_life --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0289_game_of_life --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0289_game_of_life --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0289_game_of_life --language python
./scripts/test.sh --folder 0289_game_of_life --language javascript
./scripts/test.sh --folder 0289_game_of_life --language typescript
./scripts/test.sh --folder 0289_game_of_life --language java
./scripts/test.sh --folder 0289_game_of_life --language cpp
./scripts/test.sh --folder 0289_game_of_life --language c
./scripts/test.sh --folder 0289_game_of_life --language go
./scripts/test.sh --folder 0289_game_of_life --language rust
./scripts/test.sh --folder 0289_game_of_life --language kotlin
./scripts/test.sh --folder 0289_game_of_life --language swift
./scripts/test.sh --folder 0289_game_of_life --language ruby
./scripts/test.sh --folder 0289_game_of_life --language csharp
./scripts/test.sh --folder 0289_game_of_life --language scala
./scripts/test.sh --folder 0289_game_of_life --language php
./scripts/test.sh --folder 0289_game_of_life --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0289_game_of_life --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0289_game_of_life --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0289_game_of_life --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0289_game_of_life --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0289_game_of_life --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0289_game_of_life --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0289_game_of_life --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0289_game_of_life --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0289_game_of_life --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0289_game_of_life --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0289_game_of_life --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0289_game_of_life --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0289_game_of_life --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0289_game_of_life --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm java java 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm c c 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm go go 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm rust rust 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm swift swift 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm scala scala 0289_game_of_life
docker compose -f docker/docker-compose.yml run --rm php php 0289_game_of_life
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0289_game_of_life` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0289_game_of_life` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0289_game_of_life` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0289_game_of_life` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0289_game_of_life` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0289_game_of_life` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0289_game_of_life` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0289_game_of_life` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0289_game_of_life` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0289_game_of_life` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0289_game_of_life` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0289_game_of_life` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0289_game_of_life` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0289_game_of_life` |

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
.\scripts\test.ps1 -Folder 0289_game_of_life -AllLanguages
```

```bash
./scripts/test.sh --folder 0289_game_of_life --all-languages
```

```zsh
./scripts/test.sh --folder 0289_game_of_life --all-languages
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
