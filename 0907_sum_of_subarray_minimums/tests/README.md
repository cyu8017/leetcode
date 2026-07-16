# Test harness for 0907_sum_of_subarray_minimums

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language python
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language javascript
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language typescript
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language java
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language cpp
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language c
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language go
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language rust
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language kotlin
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language swift
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language ruby
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language csharp
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language scala
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language php
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0907_sum_of_subarray_minimums --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm java java 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm c c 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm go go 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm rust rust 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm swift swift 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm scala scala 0907_sum_of_subarray_minimums
docker compose -f docker/docker-compose.yml run --rm php php 0907_sum_of_subarray_minimums
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0907_sum_of_subarray_minimums` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0907_sum_of_subarray_minimums` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0907_sum_of_subarray_minimums` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0907_sum_of_subarray_minimums` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0907_sum_of_subarray_minimums` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0907_sum_of_subarray_minimums` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0907_sum_of_subarray_minimums` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0907_sum_of_subarray_minimums` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0907_sum_of_subarray_minimums` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0907_sum_of_subarray_minimums` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0907_sum_of_subarray_minimums` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0907_sum_of_subarray_minimums` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0907_sum_of_subarray_minimums` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0907_sum_of_subarray_minimums` |

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
.\scripts\test.ps1 -Folder 0907_sum_of_subarray_minimums -AllLanguages
```

```bash
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --all-languages
```

```zsh
./scripts/test.sh --folder 0907_sum_of_subarray_minimums --all-languages
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
