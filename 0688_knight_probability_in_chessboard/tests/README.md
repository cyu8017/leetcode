# Test harness for 0688_knight_probability_in_chessboard

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language python
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language javascript
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language typescript
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language java
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language cpp
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language c
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language go
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language rust
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language kotlin
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language swift
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language ruby
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language csharp
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language scala
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language php
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0688_knight_probability_in_chessboard --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm java java 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm c c 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm go go 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm rust rust 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm swift swift 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm scala scala 0688_knight_probability_in_chessboard
docker compose -f docker/docker-compose.yml run --rm php php 0688_knight_probability_in_chessboard
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0688_knight_probability_in_chessboard` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0688_knight_probability_in_chessboard` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0688_knight_probability_in_chessboard` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0688_knight_probability_in_chessboard` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0688_knight_probability_in_chessboard` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0688_knight_probability_in_chessboard` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0688_knight_probability_in_chessboard` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0688_knight_probability_in_chessboard` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0688_knight_probability_in_chessboard` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0688_knight_probability_in_chessboard` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0688_knight_probability_in_chessboard` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0688_knight_probability_in_chessboard` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0688_knight_probability_in_chessboard` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0688_knight_probability_in_chessboard` |

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
.\scripts\test.ps1 -Folder 0688_knight_probability_in_chessboard -AllLanguages
```

```bash
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --all-languages
```

```zsh
./scripts/test.sh --folder 0688_knight_probability_in_chessboard --all-languages
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
