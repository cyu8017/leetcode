# Test harness for 1347_minimum_number_of_steps_to_make_two_strings_anagram

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language python
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language javascript
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language typescript
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language java
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language cpp
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language c
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language go
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language rust
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language kotlin
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language swift
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language ruby
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language csharp
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language scala
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language php
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm java java 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm c c 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm go go 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm rust rust 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm swift swift 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm scala scala 1347_minimum_number_of_steps_to_make_two_strings_anagram
docker compose -f docker/docker-compose.yml run --rm php php 1347_minimum_number_of_steps_to_make_two_strings_anagram
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1347_minimum_number_of_steps_to_make_two_strings_anagram` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1347_minimum_number_of_steps_to_make_two_strings_anagram` |

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
.\scripts\test.ps1 -Folder 1347_minimum_number_of_steps_to_make_two_strings_anagram -AllLanguages
```

```bash
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --all-languages
```

```zsh
./scripts/test.sh --folder 1347_minimum_number_of_steps_to_make_two_strings_anagram --all-languages
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
