# Test harness for 3800_minimum_cost_to_make_two_binary_strings_equal

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language python
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language javascript
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language typescript
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language java
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language cpp
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language c
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language go
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language rust
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language kotlin
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language swift
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language ruby
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language csharp
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language scala
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language php
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm java java 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm c c 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm go go 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm rust rust 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm swift swift 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm scala scala 3800_minimum_cost_to_make_two_binary_strings_equal
docker compose -f docker/docker-compose.yml run --rm php php 3800_minimum_cost_to_make_two_binary_strings_equal
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3800_minimum_cost_to_make_two_binary_strings_equal` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3800_minimum_cost_to_make_two_binary_strings_equal` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3800_minimum_cost_to_make_two_binary_strings_equal` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3800_minimum_cost_to_make_two_binary_strings_equal` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3800_minimum_cost_to_make_two_binary_strings_equal` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3800_minimum_cost_to_make_two_binary_strings_equal` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3800_minimum_cost_to_make_two_binary_strings_equal` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3800_minimum_cost_to_make_two_binary_strings_equal` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3800_minimum_cost_to_make_two_binary_strings_equal` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3800_minimum_cost_to_make_two_binary_strings_equal` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3800_minimum_cost_to_make_two_binary_strings_equal` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3800_minimum_cost_to_make_two_binary_strings_equal` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3800_minimum_cost_to_make_two_binary_strings_equal` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3800_minimum_cost_to_make_two_binary_strings_equal` |

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
.\scripts\test.ps1 -Folder 3800_minimum_cost_to_make_two_binary_strings_equal -AllLanguages
```

```bash
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --all-languages
```

```zsh
./scripts/test.sh --folder 3800_minimum_cost_to_make_two_binary_strings_equal --all-languages
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
