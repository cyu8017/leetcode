# Test harness for 1690_stone_game_vii

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1690_stone_game_vii -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1690_stone_game_vii --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1690_stone_game_vii --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1690_stone_game_vii --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1690_stone_game_vii --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1690_stone_game_vii --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1690_stone_game_vii --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1690_stone_game_vii --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1690_stone_game_vii --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1690_stone_game_vii --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1690_stone_game_vii --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1690_stone_game_vii --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1690_stone_game_vii --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1690_stone_game_vii --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1690_stone_game_vii --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1690_stone_game_vii --language python
./scripts/test.sh --folder 1690_stone_game_vii --language javascript
./scripts/test.sh --folder 1690_stone_game_vii --language typescript
./scripts/test.sh --folder 1690_stone_game_vii --language java
./scripts/test.sh --folder 1690_stone_game_vii --language cpp
./scripts/test.sh --folder 1690_stone_game_vii --language c
./scripts/test.sh --folder 1690_stone_game_vii --language go
./scripts/test.sh --folder 1690_stone_game_vii --language rust
./scripts/test.sh --folder 1690_stone_game_vii --language kotlin
./scripts/test.sh --folder 1690_stone_game_vii --language swift
./scripts/test.sh --folder 1690_stone_game_vii --language ruby
./scripts/test.sh --folder 1690_stone_game_vii --language csharp
./scripts/test.sh --folder 1690_stone_game_vii --language scala
./scripts/test.sh --folder 1690_stone_game_vii --language php
./scripts/test.sh --folder 1690_stone_game_vii --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1690_stone_game_vii --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1690_stone_game_vii --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1690_stone_game_vii --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1690_stone_game_vii --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1690_stone_game_vii --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1690_stone_game_vii --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1690_stone_game_vii --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1690_stone_game_vii --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1690_stone_game_vii --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1690_stone_game_vii --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1690_stone_game_vii --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1690_stone_game_vii --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1690_stone_game_vii --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1690_stone_game_vii --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm java java 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm c c 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm go go 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm rust rust 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm swift swift 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm scala scala 1690_stone_game_vii
docker compose -f docker/docker-compose.yml run --rm php php 1690_stone_game_vii
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1690_stone_game_vii` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1690_stone_game_vii` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1690_stone_game_vii` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1690_stone_game_vii` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1690_stone_game_vii` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1690_stone_game_vii` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1690_stone_game_vii` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1690_stone_game_vii` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1690_stone_game_vii` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1690_stone_game_vii` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1690_stone_game_vii` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1690_stone_game_vii` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1690_stone_game_vii` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1690_stone_game_vii` |

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
.\scripts\test.ps1 -Folder 1690_stone_game_vii -AllLanguages
```

```bash
./scripts/test.sh --folder 1690_stone_game_vii --all-languages
```

```zsh
./scripts/test.sh --folder 1690_stone_game_vii --all-languages
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
