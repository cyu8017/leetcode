# Test harness for 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language python
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language javascript
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language typescript
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language java
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language cpp
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language c
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language go
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language rust
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language kotlin
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language swift
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language ruby
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language csharp
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language scala
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language php
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm java java 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm c c 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm go go 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm rust rust 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm swift swift 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm scala scala 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
docker compose -f docker/docker-compose.yml run --rm php php 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating` |

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
.\scripts\test.ps1 -Folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating -AllLanguages
```

```bash
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --all-languages
```

```zsh
./scripts/test.sh --folder 1864_minimum_number_of_swaps_to_make_the_binary_string_alternating --all-languages
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
