# Test harness for 1893_check_if_all_the_integers_in_a_range_are_covered

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language python
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language javascript
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language typescript
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language java
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language cpp
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language c
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language go
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language rust
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language kotlin
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language swift
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language ruby
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language csharp
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language scala
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language php
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm java java 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm c c 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm go go 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm rust rust 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm swift swift 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm scala scala 1893_check_if_all_the_integers_in_a_range_are_covered
docker compose -f docker/docker-compose.yml run --rm php php 1893_check_if_all_the_integers_in_a_range_are_covered
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1893_check_if_all_the_integers_in_a_range_are_covered` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1893_check_if_all_the_integers_in_a_range_are_covered` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1893_check_if_all_the_integers_in_a_range_are_covered` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1893_check_if_all_the_integers_in_a_range_are_covered` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1893_check_if_all_the_integers_in_a_range_are_covered` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1893_check_if_all_the_integers_in_a_range_are_covered` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1893_check_if_all_the_integers_in_a_range_are_covered` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1893_check_if_all_the_integers_in_a_range_are_covered` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1893_check_if_all_the_integers_in_a_range_are_covered` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1893_check_if_all_the_integers_in_a_range_are_covered` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1893_check_if_all_the_integers_in_a_range_are_covered` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1893_check_if_all_the_integers_in_a_range_are_covered` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1893_check_if_all_the_integers_in_a_range_are_covered` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1893_check_if_all_the_integers_in_a_range_are_covered` |

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
.\scripts\test.ps1 -Folder 1893_check_if_all_the_integers_in_a_range_are_covered -AllLanguages
```

```bash
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --all-languages
```

```zsh
./scripts/test.sh --folder 1893_check_if_all_the_integers_in_a_range_are_covered --all-languages
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
