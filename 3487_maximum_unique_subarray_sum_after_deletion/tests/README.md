# Test harness for 3487_maximum_unique_subarray_sum_after_deletion

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language python
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language javascript
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language typescript
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language java
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language cpp
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language c
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language go
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language rust
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language kotlin
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language swift
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language ruby
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language csharp
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language scala
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language php
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm java java 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm c c 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm go go 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm rust rust 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm swift swift 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm scala scala 3487_maximum_unique_subarray_sum_after_deletion
docker compose -f docker/docker-compose.yml run --rm php php 3487_maximum_unique_subarray_sum_after_deletion
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3487_maximum_unique_subarray_sum_after_deletion` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3487_maximum_unique_subarray_sum_after_deletion` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3487_maximum_unique_subarray_sum_after_deletion` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3487_maximum_unique_subarray_sum_after_deletion` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3487_maximum_unique_subarray_sum_after_deletion` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3487_maximum_unique_subarray_sum_after_deletion` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3487_maximum_unique_subarray_sum_after_deletion` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3487_maximum_unique_subarray_sum_after_deletion` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3487_maximum_unique_subarray_sum_after_deletion` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3487_maximum_unique_subarray_sum_after_deletion` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3487_maximum_unique_subarray_sum_after_deletion` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3487_maximum_unique_subarray_sum_after_deletion` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3487_maximum_unique_subarray_sum_after_deletion` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3487_maximum_unique_subarray_sum_after_deletion` |

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
.\scripts\test.ps1 -Folder 3487_maximum_unique_subarray_sum_after_deletion -AllLanguages
```

```bash
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --all-languages
```

```zsh
./scripts/test.sh --folder 3487_maximum_unique_subarray_sum_after_deletion --all-languages
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
