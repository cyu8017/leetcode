# Test harness for 2531_make_number_of_distinct_characters_equal

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language python
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language javascript
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language typescript
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language java
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language cpp
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language c
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language go
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language rust
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language kotlin
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language swift
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language ruby
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language csharp
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language scala
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language php
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm java java 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm c c 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm go go 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm rust rust 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm swift swift 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm scala scala 2531_make_number_of_distinct_characters_equal
docker compose -f docker/docker-compose.yml run --rm php php 2531_make_number_of_distinct_characters_equal
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2531_make_number_of_distinct_characters_equal` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2531_make_number_of_distinct_characters_equal` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2531_make_number_of_distinct_characters_equal` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2531_make_number_of_distinct_characters_equal` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2531_make_number_of_distinct_characters_equal` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2531_make_number_of_distinct_characters_equal` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2531_make_number_of_distinct_characters_equal` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2531_make_number_of_distinct_characters_equal` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2531_make_number_of_distinct_characters_equal` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2531_make_number_of_distinct_characters_equal` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2531_make_number_of_distinct_characters_equal` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2531_make_number_of_distinct_characters_equal` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2531_make_number_of_distinct_characters_equal` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2531_make_number_of_distinct_characters_equal` |

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
.\scripts\test.ps1 -Folder 2531_make_number_of_distinct_characters_equal -AllLanguages
```

```bash
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --all-languages
```

```zsh
./scripts/test.sh --folder 2531_make_number_of_distinct_characters_equal --all-languages
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
