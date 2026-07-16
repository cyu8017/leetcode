# Test harness for 1746_maximum_subarray_sum_after_one_operation

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language python
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language javascript
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language typescript
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language java
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language cpp
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language c
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language go
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language rust
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language kotlin
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language swift
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language ruby
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language csharp
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language scala
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language php
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm java java 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm c c 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm go go 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm rust rust 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm swift swift 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm scala scala 1746_maximum_subarray_sum_after_one_operation
docker compose -f docker/docker-compose.yml run --rm php php 1746_maximum_subarray_sum_after_one_operation
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1746_maximum_subarray_sum_after_one_operation` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1746_maximum_subarray_sum_after_one_operation` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1746_maximum_subarray_sum_after_one_operation` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1746_maximum_subarray_sum_after_one_operation` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1746_maximum_subarray_sum_after_one_operation` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1746_maximum_subarray_sum_after_one_operation` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1746_maximum_subarray_sum_after_one_operation` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1746_maximum_subarray_sum_after_one_operation` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1746_maximum_subarray_sum_after_one_operation` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1746_maximum_subarray_sum_after_one_operation` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1746_maximum_subarray_sum_after_one_operation` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1746_maximum_subarray_sum_after_one_operation` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1746_maximum_subarray_sum_after_one_operation` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1746_maximum_subarray_sum_after_one_operation` |

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
.\scripts\test.ps1 -Folder 1746_maximum_subarray_sum_after_one_operation -AllLanguages
```

```bash
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --all-languages
```

```zsh
./scripts/test.sh --folder 1746_maximum_subarray_sum_after_one_operation --all-languages
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
