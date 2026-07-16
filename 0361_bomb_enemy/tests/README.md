# Test harness for 0361_bomb_enemy

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0361_bomb_enemy -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0361_bomb_enemy --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0361_bomb_enemy --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0361_bomb_enemy --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0361_bomb_enemy --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0361_bomb_enemy --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0361_bomb_enemy --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0361_bomb_enemy --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0361_bomb_enemy --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0361_bomb_enemy --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0361_bomb_enemy --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0361_bomb_enemy --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0361_bomb_enemy --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0361_bomb_enemy --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0361_bomb_enemy --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0361_bomb_enemy --language python
./scripts/test.sh --folder 0361_bomb_enemy --language javascript
./scripts/test.sh --folder 0361_bomb_enemy --language typescript
./scripts/test.sh --folder 0361_bomb_enemy --language java
./scripts/test.sh --folder 0361_bomb_enemy --language cpp
./scripts/test.sh --folder 0361_bomb_enemy --language c
./scripts/test.sh --folder 0361_bomb_enemy --language go
./scripts/test.sh --folder 0361_bomb_enemy --language rust
./scripts/test.sh --folder 0361_bomb_enemy --language kotlin
./scripts/test.sh --folder 0361_bomb_enemy --language swift
./scripts/test.sh --folder 0361_bomb_enemy --language ruby
./scripts/test.sh --folder 0361_bomb_enemy --language csharp
./scripts/test.sh --folder 0361_bomb_enemy --language scala
./scripts/test.sh --folder 0361_bomb_enemy --language php
./scripts/test.sh --folder 0361_bomb_enemy --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0361_bomb_enemy --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0361_bomb_enemy --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0361_bomb_enemy --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0361_bomb_enemy --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0361_bomb_enemy --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0361_bomb_enemy --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0361_bomb_enemy --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0361_bomb_enemy --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0361_bomb_enemy --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0361_bomb_enemy --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0361_bomb_enemy --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0361_bomb_enemy --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0361_bomb_enemy --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0361_bomb_enemy --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm java java 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm c c 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm go go 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm rust rust 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm swift swift 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm scala scala 0361_bomb_enemy
docker compose -f docker/docker-compose.yml run --rm php php 0361_bomb_enemy
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0361_bomb_enemy` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0361_bomb_enemy` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0361_bomb_enemy` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0361_bomb_enemy` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0361_bomb_enemy` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0361_bomb_enemy` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0361_bomb_enemy` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0361_bomb_enemy` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0361_bomb_enemy` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0361_bomb_enemy` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0361_bomb_enemy` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0361_bomb_enemy` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0361_bomb_enemy` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0361_bomb_enemy` |

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
.\scripts\test.ps1 -Folder 0361_bomb_enemy -AllLanguages
```

```bash
./scripts/test.sh --folder 0361_bomb_enemy --all-languages
```

```zsh
./scripts/test.sh --folder 0361_bomb_enemy --all-languages
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
