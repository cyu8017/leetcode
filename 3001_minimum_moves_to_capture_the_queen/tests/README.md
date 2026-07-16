# Test harness for 3001_minimum_moves_to_capture_the_queen

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language python
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language javascript
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language typescript
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language java
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language cpp
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language c
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language go
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language rust
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language kotlin
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language swift
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language ruby
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language csharp
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language scala
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language php
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm java java 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm c c 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm go go 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm rust rust 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm swift swift 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm scala scala 3001_minimum_moves_to_capture_the_queen
docker compose -f docker/docker-compose.yml run --rm php php 3001_minimum_moves_to_capture_the_queen
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3001_minimum_moves_to_capture_the_queen` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3001_minimum_moves_to_capture_the_queen` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3001_minimum_moves_to_capture_the_queen` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3001_minimum_moves_to_capture_the_queen` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3001_minimum_moves_to_capture_the_queen` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3001_minimum_moves_to_capture_the_queen` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3001_minimum_moves_to_capture_the_queen` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3001_minimum_moves_to_capture_the_queen` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3001_minimum_moves_to_capture_the_queen` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3001_minimum_moves_to_capture_the_queen` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3001_minimum_moves_to_capture_the_queen` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3001_minimum_moves_to_capture_the_queen` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3001_minimum_moves_to_capture_the_queen` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3001_minimum_moves_to_capture_the_queen` |

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
.\scripts\test.ps1 -Folder 3001_minimum_moves_to_capture_the_queen -AllLanguages
```

```bash
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --all-languages
```

```zsh
./scripts/test.sh --folder 3001_minimum_moves_to_capture_the_queen --all-languages
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
