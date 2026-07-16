# Test harness for 3310_remove_methods_from_project

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3310_remove_methods_from_project --language python
./scripts/test.sh --folder 3310_remove_methods_from_project --language javascript
./scripts/test.sh --folder 3310_remove_methods_from_project --language typescript
./scripts/test.sh --folder 3310_remove_methods_from_project --language java
./scripts/test.sh --folder 3310_remove_methods_from_project --language cpp
./scripts/test.sh --folder 3310_remove_methods_from_project --language c
./scripts/test.sh --folder 3310_remove_methods_from_project --language go
./scripts/test.sh --folder 3310_remove_methods_from_project --language rust
./scripts/test.sh --folder 3310_remove_methods_from_project --language kotlin
./scripts/test.sh --folder 3310_remove_methods_from_project --language swift
./scripts/test.sh --folder 3310_remove_methods_from_project --language ruby
./scripts/test.sh --folder 3310_remove_methods_from_project --language csharp
./scripts/test.sh --folder 3310_remove_methods_from_project --language scala
./scripts/test.sh --folder 3310_remove_methods_from_project --language php
./scripts/test.sh --folder 3310_remove_methods_from_project --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3310_remove_methods_from_project --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm java java 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm c c 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm go go 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm rust rust 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm swift swift 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm scala scala 3310_remove_methods_from_project
docker compose -f docker/docker-compose.yml run --rm php php 3310_remove_methods_from_project
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3310_remove_methods_from_project` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3310_remove_methods_from_project` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3310_remove_methods_from_project` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3310_remove_methods_from_project` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3310_remove_methods_from_project` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3310_remove_methods_from_project` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3310_remove_methods_from_project` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3310_remove_methods_from_project` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3310_remove_methods_from_project` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3310_remove_methods_from_project` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3310_remove_methods_from_project` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3310_remove_methods_from_project` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3310_remove_methods_from_project` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3310_remove_methods_from_project` |

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
.\scripts\test.ps1 -Folder 3310_remove_methods_from_project -AllLanguages
```

```bash
./scripts/test.sh --folder 3310_remove_methods_from_project --all-languages
```

```zsh
./scripts/test.sh --folder 3310_remove_methods_from_project --all-languages
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
