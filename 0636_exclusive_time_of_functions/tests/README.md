# Test harness for 0636_exclusive_time_of_functions

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language python
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language javascript
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language typescript
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language java
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language cpp
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language c
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language go
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language rust
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language kotlin
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language swift
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language ruby
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language csharp
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language scala
./scripts/test.sh --folder 0636_exclusive_time_of_functions --language php
./scripts/test.sh --folder 0636_exclusive_time_of_functions --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0636_exclusive_time_of_functions --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm java java 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm c c 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm go go 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm rust rust 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm swift swift 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm scala scala 0636_exclusive_time_of_functions
docker compose -f docker/docker-compose.yml run --rm php php 0636_exclusive_time_of_functions
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0636_exclusive_time_of_functions` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0636_exclusive_time_of_functions` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0636_exclusive_time_of_functions` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0636_exclusive_time_of_functions` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0636_exclusive_time_of_functions` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0636_exclusive_time_of_functions` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0636_exclusive_time_of_functions` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0636_exclusive_time_of_functions` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0636_exclusive_time_of_functions` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0636_exclusive_time_of_functions` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0636_exclusive_time_of_functions` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0636_exclusive_time_of_functions` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0636_exclusive_time_of_functions` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0636_exclusive_time_of_functions` |

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
.\scripts\test.ps1 -Folder 0636_exclusive_time_of_functions -AllLanguages
```

```bash
./scripts/test.sh --folder 0636_exclusive_time_of_functions --all-languages
```

```zsh
./scripts/test.sh --folder 0636_exclusive_time_of_functions --all-languages
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
