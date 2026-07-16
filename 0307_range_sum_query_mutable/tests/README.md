# Test harness for 0307_range_sum_query_mutable

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0307_range_sum_query_mutable --language python
./scripts/test.sh --folder 0307_range_sum_query_mutable --language javascript
./scripts/test.sh --folder 0307_range_sum_query_mutable --language typescript
./scripts/test.sh --folder 0307_range_sum_query_mutable --language java
./scripts/test.sh --folder 0307_range_sum_query_mutable --language cpp
./scripts/test.sh --folder 0307_range_sum_query_mutable --language c
./scripts/test.sh --folder 0307_range_sum_query_mutable --language go
./scripts/test.sh --folder 0307_range_sum_query_mutable --language rust
./scripts/test.sh --folder 0307_range_sum_query_mutable --language kotlin
./scripts/test.sh --folder 0307_range_sum_query_mutable --language swift
./scripts/test.sh --folder 0307_range_sum_query_mutable --language ruby
./scripts/test.sh --folder 0307_range_sum_query_mutable --language csharp
./scripts/test.sh --folder 0307_range_sum_query_mutable --language scala
./scripts/test.sh --folder 0307_range_sum_query_mutable --language php
./scripts/test.sh --folder 0307_range_sum_query_mutable --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0307_range_sum_query_mutable --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm java java 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm c c 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm go go 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm rust rust 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm swift swift 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm scala scala 0307_range_sum_query_mutable
docker compose -f docker/docker-compose.yml run --rm php php 0307_range_sum_query_mutable
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0307_range_sum_query_mutable` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0307_range_sum_query_mutable` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0307_range_sum_query_mutable` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0307_range_sum_query_mutable` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0307_range_sum_query_mutable` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0307_range_sum_query_mutable` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0307_range_sum_query_mutable` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0307_range_sum_query_mutable` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0307_range_sum_query_mutable` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0307_range_sum_query_mutable` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0307_range_sum_query_mutable` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0307_range_sum_query_mutable` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0307_range_sum_query_mutable` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0307_range_sum_query_mutable` |

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
.\scripts\test.ps1 -Folder 0307_range_sum_query_mutable -AllLanguages
```

```bash
./scripts/test.sh --folder 0307_range_sum_query_mutable --all-languages
```

```zsh
./scripts/test.sh --folder 0307_range_sum_query_mutable --all-languages
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
