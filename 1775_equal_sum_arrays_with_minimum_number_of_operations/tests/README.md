# Test harness for 1775_equal_sum_arrays_with_minimum_number_of_operations

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language python
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language javascript
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language typescript
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language java
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language cpp
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language c
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language go
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language rust
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language kotlin
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language swift
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language ruby
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language csharp
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language scala
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language php
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm java java 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm c c 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm go go 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm rust rust 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm swift swift 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm scala scala 1775_equal_sum_arrays_with_minimum_number_of_operations
docker compose -f docker/docker-compose.yml run --rm php php 1775_equal_sum_arrays_with_minimum_number_of_operations
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1775_equal_sum_arrays_with_minimum_number_of_operations` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1775_equal_sum_arrays_with_minimum_number_of_operations` |

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
.\scripts\test.ps1 -Folder 1775_equal_sum_arrays_with_minimum_number_of_operations -AllLanguages
```

```bash
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --all-languages
```

```zsh
./scripts/test.sh --folder 1775_equal_sum_arrays_with_minimum_number_of_operations --all-languages
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
