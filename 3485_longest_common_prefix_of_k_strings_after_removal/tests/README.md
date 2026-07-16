# Test harness for 3485_longest_common_prefix_of_k_strings_after_removal

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language python
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language javascript
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language typescript
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language java
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language cpp
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language c
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language go
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language rust
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language kotlin
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language swift
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language ruby
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language csharp
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language scala
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language php
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm java java 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm c c 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm go go 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm rust rust 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm swift swift 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm scala scala 3485_longest_common_prefix_of_k_strings_after_removal
docker compose -f docker/docker-compose.yml run --rm php php 3485_longest_common_prefix_of_k_strings_after_removal
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3485_longest_common_prefix_of_k_strings_after_removal` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3485_longest_common_prefix_of_k_strings_after_removal` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3485_longest_common_prefix_of_k_strings_after_removal` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3485_longest_common_prefix_of_k_strings_after_removal` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3485_longest_common_prefix_of_k_strings_after_removal` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3485_longest_common_prefix_of_k_strings_after_removal` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3485_longest_common_prefix_of_k_strings_after_removal` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3485_longest_common_prefix_of_k_strings_after_removal` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3485_longest_common_prefix_of_k_strings_after_removal` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3485_longest_common_prefix_of_k_strings_after_removal` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3485_longest_common_prefix_of_k_strings_after_removal` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3485_longest_common_prefix_of_k_strings_after_removal` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3485_longest_common_prefix_of_k_strings_after_removal` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3485_longest_common_prefix_of_k_strings_after_removal` |

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
.\scripts\test.ps1 -Folder 3485_longest_common_prefix_of_k_strings_after_removal -AllLanguages
```

```bash
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --all-languages
```

```zsh
./scripts/test.sh --folder 3485_longest_common_prefix_of_k_strings_after_removal --all-languages
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
