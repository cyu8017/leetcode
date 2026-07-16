# Test harness for 0921_minimum_add_to_make_parentheses_valid

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language python
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language javascript
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language typescript
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language java
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language cpp
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language c
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language go
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language rust
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language kotlin
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language swift
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language ruby
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language csharp
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language scala
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language php
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm java java 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm c c 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm go go 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm rust rust 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm swift swift 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm scala scala 0921_minimum_add_to_make_parentheses_valid
docker compose -f docker/docker-compose.yml run --rm php php 0921_minimum_add_to_make_parentheses_valid
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0921_minimum_add_to_make_parentheses_valid` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0921_minimum_add_to_make_parentheses_valid` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0921_minimum_add_to_make_parentheses_valid` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0921_minimum_add_to_make_parentheses_valid` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0921_minimum_add_to_make_parentheses_valid` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0921_minimum_add_to_make_parentheses_valid` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0921_minimum_add_to_make_parentheses_valid` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0921_minimum_add_to_make_parentheses_valid` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0921_minimum_add_to_make_parentheses_valid` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0921_minimum_add_to_make_parentheses_valid` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0921_minimum_add_to_make_parentheses_valid` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0921_minimum_add_to_make_parentheses_valid` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0921_minimum_add_to_make_parentheses_valid` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0921_minimum_add_to_make_parentheses_valid` |

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
.\scripts\test.ps1 -Folder 0921_minimum_add_to_make_parentheses_valid -AllLanguages
```

```bash
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --all-languages
```

```zsh
./scripts/test.sh --folder 0921_minimum_add_to_make_parentheses_valid --all-languages
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
