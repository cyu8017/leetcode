# Test harness for 1575_count_all_possible_routes

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1575_count_all_possible_routes --language python
./scripts/test.sh --folder 1575_count_all_possible_routes --language javascript
./scripts/test.sh --folder 1575_count_all_possible_routes --language typescript
./scripts/test.sh --folder 1575_count_all_possible_routes --language java
./scripts/test.sh --folder 1575_count_all_possible_routes --language cpp
./scripts/test.sh --folder 1575_count_all_possible_routes --language c
./scripts/test.sh --folder 1575_count_all_possible_routes --language go
./scripts/test.sh --folder 1575_count_all_possible_routes --language rust
./scripts/test.sh --folder 1575_count_all_possible_routes --language kotlin
./scripts/test.sh --folder 1575_count_all_possible_routes --language swift
./scripts/test.sh --folder 1575_count_all_possible_routes --language ruby
./scripts/test.sh --folder 1575_count_all_possible_routes --language csharp
./scripts/test.sh --folder 1575_count_all_possible_routes --language scala
./scripts/test.sh --folder 1575_count_all_possible_routes --language php
./scripts/test.sh --folder 1575_count_all_possible_routes --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1575_count_all_possible_routes --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm java java 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm c c 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm go go 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm rust rust 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm swift swift 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm scala scala 1575_count_all_possible_routes
docker compose -f docker/docker-compose.yml run --rm php php 1575_count_all_possible_routes
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1575_count_all_possible_routes` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1575_count_all_possible_routes` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1575_count_all_possible_routes` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1575_count_all_possible_routes` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1575_count_all_possible_routes` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1575_count_all_possible_routes` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1575_count_all_possible_routes` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1575_count_all_possible_routes` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1575_count_all_possible_routes` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1575_count_all_possible_routes` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1575_count_all_possible_routes` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1575_count_all_possible_routes` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1575_count_all_possible_routes` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1575_count_all_possible_routes` |

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
.\scripts\test.ps1 -Folder 1575_count_all_possible_routes -AllLanguages
```

```bash
./scripts/test.sh --folder 1575_count_all_possible_routes --all-languages
```

```zsh
./scripts/test.sh --folder 1575_count_all_possible_routes --all-languages
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
