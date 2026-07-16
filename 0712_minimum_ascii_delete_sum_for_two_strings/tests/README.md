# Test harness for 0712_minimum_ascii_delete_sum_for_two_strings

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language python
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language javascript
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language typescript
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language java
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language cpp
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language c
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language go
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language rust
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language kotlin
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language swift
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language ruby
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language csharp
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language scala
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language php
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm java java 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm c c 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm go go 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm rust rust 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm swift swift 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm scala scala 0712_minimum_ascii_delete_sum_for_two_strings
docker compose -f docker/docker-compose.yml run --rm php php 0712_minimum_ascii_delete_sum_for_two_strings
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0712_minimum_ascii_delete_sum_for_two_strings` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0712_minimum_ascii_delete_sum_for_two_strings` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0712_minimum_ascii_delete_sum_for_two_strings` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0712_minimum_ascii_delete_sum_for_two_strings` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0712_minimum_ascii_delete_sum_for_two_strings` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0712_minimum_ascii_delete_sum_for_two_strings` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0712_minimum_ascii_delete_sum_for_two_strings` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0712_minimum_ascii_delete_sum_for_two_strings` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0712_minimum_ascii_delete_sum_for_two_strings` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0712_minimum_ascii_delete_sum_for_two_strings` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0712_minimum_ascii_delete_sum_for_two_strings` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0712_minimum_ascii_delete_sum_for_two_strings` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0712_minimum_ascii_delete_sum_for_two_strings` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0712_minimum_ascii_delete_sum_for_two_strings` |

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
.\scripts\test.ps1 -Folder 0712_minimum_ascii_delete_sum_for_two_strings -AllLanguages
```

```bash
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --all-languages
```

```zsh
./scripts/test.sh --folder 0712_minimum_ascii_delete_sum_for_two_strings --all-languages
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
