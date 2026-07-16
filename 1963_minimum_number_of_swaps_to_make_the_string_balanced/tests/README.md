# Test harness for 1963_minimum_number_of_swaps_to_make_the_string_balanced

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language python
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language javascript
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language typescript
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language java
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language cpp
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language c
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language go
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language rust
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language kotlin
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language swift
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language ruby
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language csharp
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language scala
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language php
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm java java 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm c c 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm go go 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm rust rust 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm swift swift 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm scala scala 1963_minimum_number_of_swaps_to_make_the_string_balanced
docker compose -f docker/docker-compose.yml run --rm php php 1963_minimum_number_of_swaps_to_make_the_string_balanced
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1963_minimum_number_of_swaps_to_make_the_string_balanced` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1963_minimum_number_of_swaps_to_make_the_string_balanced` |

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
.\scripts\test.ps1 -Folder 1963_minimum_number_of_swaps_to_make_the_string_balanced -AllLanguages
```

```bash
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --all-languages
```

```zsh
./scripts/test.sh --folder 1963_minimum_number_of_swaps_to_make_the_string_balanced --all-languages
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
