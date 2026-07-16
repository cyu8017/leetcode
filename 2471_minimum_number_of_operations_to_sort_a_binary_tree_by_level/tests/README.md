# Test harness for 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language python
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language javascript
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language typescript
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language java
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language cpp
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language c
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language go
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language rust
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language kotlin
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language swift
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language ruby
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language csharp
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language scala
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language php
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm java java 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm c c 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm go go 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm rust rust 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm swift swift 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm scala scala 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
docker compose -f docker/docker-compose.yml run --rm php php 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level` |

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
.\scripts\test.ps1 -Folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level -AllLanguages
```

```bash
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --all-languages
```

```zsh
./scripts/test.sh --folder 2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level --all-languages
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
