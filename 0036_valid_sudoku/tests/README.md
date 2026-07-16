# Test harness for 0036_valid_sudoku

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0036_valid_sudoku -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0036_valid_sudoku --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0036_valid_sudoku --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0036_valid_sudoku --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0036_valid_sudoku --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0036_valid_sudoku --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0036_valid_sudoku --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0036_valid_sudoku --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0036_valid_sudoku --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0036_valid_sudoku --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0036_valid_sudoku --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0036_valid_sudoku --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0036_valid_sudoku --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0036_valid_sudoku --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0036_valid_sudoku --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0036_valid_sudoku --language python
./scripts/test.sh --folder 0036_valid_sudoku --language javascript
./scripts/test.sh --folder 0036_valid_sudoku --language typescript
./scripts/test.sh --folder 0036_valid_sudoku --language java
./scripts/test.sh --folder 0036_valid_sudoku --language cpp
./scripts/test.sh --folder 0036_valid_sudoku --language c
./scripts/test.sh --folder 0036_valid_sudoku --language go
./scripts/test.sh --folder 0036_valid_sudoku --language rust
./scripts/test.sh --folder 0036_valid_sudoku --language kotlin
./scripts/test.sh --folder 0036_valid_sudoku --language swift
./scripts/test.sh --folder 0036_valid_sudoku --language ruby
./scripts/test.sh --folder 0036_valid_sudoku --language csharp
./scripts/test.sh --folder 0036_valid_sudoku --language scala
./scripts/test.sh --folder 0036_valid_sudoku --language php
./scripts/test.sh --folder 0036_valid_sudoku --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0036_valid_sudoku --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0036_valid_sudoku --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0036_valid_sudoku --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0036_valid_sudoku --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0036_valid_sudoku --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0036_valid_sudoku --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0036_valid_sudoku --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0036_valid_sudoku --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0036_valid_sudoku --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0036_valid_sudoku --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0036_valid_sudoku --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0036_valid_sudoku --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0036_valid_sudoku --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0036_valid_sudoku --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm java java 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm c c 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm go go 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm rust rust 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm swift swift 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm scala scala 0036_valid_sudoku
docker compose -f docker/docker-compose.yml run --rm php php 0036_valid_sudoku
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0036_valid_sudoku` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0036_valid_sudoku` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0036_valid_sudoku` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0036_valid_sudoku` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0036_valid_sudoku` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0036_valid_sudoku` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0036_valid_sudoku` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0036_valid_sudoku` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0036_valid_sudoku` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0036_valid_sudoku` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0036_valid_sudoku` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0036_valid_sudoku` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0036_valid_sudoku` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0036_valid_sudoku` |

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
.\scripts\test.ps1 -Folder 0036_valid_sudoku -AllLanguages
```

```bash
./scripts/test.sh --folder 0036_valid_sudoku --all-languages
```

```zsh
./scripts/test.sh --folder 0036_valid_sudoku --all-languages
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
