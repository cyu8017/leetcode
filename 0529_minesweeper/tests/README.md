# Test harness for 0529_minesweeper

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0529_minesweeper -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0529_minesweeper --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0529_minesweeper --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0529_minesweeper --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0529_minesweeper --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0529_minesweeper --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0529_minesweeper --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0529_minesweeper --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0529_minesweeper --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0529_minesweeper --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0529_minesweeper --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0529_minesweeper --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0529_minesweeper --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0529_minesweeper --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0529_minesweeper --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0529_minesweeper --language python
./scripts/test.sh --folder 0529_minesweeper --language javascript
./scripts/test.sh --folder 0529_minesweeper --language typescript
./scripts/test.sh --folder 0529_minesweeper --language java
./scripts/test.sh --folder 0529_minesweeper --language cpp
./scripts/test.sh --folder 0529_minesweeper --language c
./scripts/test.sh --folder 0529_minesweeper --language go
./scripts/test.sh --folder 0529_minesweeper --language rust
./scripts/test.sh --folder 0529_minesweeper --language kotlin
./scripts/test.sh --folder 0529_minesweeper --language swift
./scripts/test.sh --folder 0529_minesweeper --language ruby
./scripts/test.sh --folder 0529_minesweeper --language csharp
./scripts/test.sh --folder 0529_minesweeper --language scala
./scripts/test.sh --folder 0529_minesweeper --language php
./scripts/test.sh --folder 0529_minesweeper --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0529_minesweeper --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0529_minesweeper --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0529_minesweeper --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0529_minesweeper --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0529_minesweeper --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0529_minesweeper --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0529_minesweeper --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0529_minesweeper --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0529_minesweeper --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0529_minesweeper --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0529_minesweeper --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0529_minesweeper --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0529_minesweeper --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0529_minesweeper --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm java java 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm c c 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm go go 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm rust rust 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm swift swift 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm scala scala 0529_minesweeper
docker compose -f docker/docker-compose.yml run --rm php php 0529_minesweeper
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0529_minesweeper` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0529_minesweeper` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0529_minesweeper` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0529_minesweeper` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0529_minesweeper` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0529_minesweeper` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0529_minesweeper` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0529_minesweeper` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0529_minesweeper` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0529_minesweeper` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0529_minesweeper` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0529_minesweeper` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0529_minesweeper` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0529_minesweeper` |

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
.\scripts\test.ps1 -Folder 0529_minesweeper -AllLanguages
```

```bash
./scripts/test.sh --folder 0529_minesweeper --all-languages
```

```zsh
./scripts/test.sh --folder 0529_minesweeper --all-languages
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
