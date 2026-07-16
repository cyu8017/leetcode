# Test harness for 0159_longest_substring_with_at_most_two_distinct_characters

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language python
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language javascript
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language typescript
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language java
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language cpp
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language c
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language go
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language rust
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language kotlin
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language swift
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language ruby
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language csharp
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language scala
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language php
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm java java 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm c c 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm go go 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm rust rust 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm swift swift 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm scala scala 0159_longest_substring_with_at_most_two_distinct_characters
docker compose -f docker/docker-compose.yml run --rm php php 0159_longest_substring_with_at_most_two_distinct_characters
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0159_longest_substring_with_at_most_two_distinct_characters` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0159_longest_substring_with_at_most_two_distinct_characters` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0159_longest_substring_with_at_most_two_distinct_characters` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0159_longest_substring_with_at_most_two_distinct_characters` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0159_longest_substring_with_at_most_two_distinct_characters` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0159_longest_substring_with_at_most_two_distinct_characters` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0159_longest_substring_with_at_most_two_distinct_characters` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0159_longest_substring_with_at_most_two_distinct_characters` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0159_longest_substring_with_at_most_two_distinct_characters` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0159_longest_substring_with_at_most_two_distinct_characters` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0159_longest_substring_with_at_most_two_distinct_characters` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0159_longest_substring_with_at_most_two_distinct_characters` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0159_longest_substring_with_at_most_two_distinct_characters` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0159_longest_substring_with_at_most_two_distinct_characters` |

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
.\scripts\test.ps1 -Folder 0159_longest_substring_with_at_most_two_distinct_characters -AllLanguages
```

```bash
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --all-languages
```

```zsh
./scripts/test.sh --folder 0159_longest_substring_with_at_most_two_distinct_characters --all-languages
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
