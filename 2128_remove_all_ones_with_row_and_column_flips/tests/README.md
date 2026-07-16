# Test harness for 2128_remove_all_ones_with_row_and_column_flips

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language python
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language javascript
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language typescript
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language java
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language cpp
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language c
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language go
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language rust
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language kotlin
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language swift
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language ruby
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language csharp
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language scala
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language php
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm java java 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm c c 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm go go 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm rust rust 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm swift swift 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm scala scala 2128_remove_all_ones_with_row_and_column_flips
docker compose -f docker/docker-compose.yml run --rm php php 2128_remove_all_ones_with_row_and_column_flips
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2128_remove_all_ones_with_row_and_column_flips` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2128_remove_all_ones_with_row_and_column_flips` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2128_remove_all_ones_with_row_and_column_flips` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2128_remove_all_ones_with_row_and_column_flips` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2128_remove_all_ones_with_row_and_column_flips` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2128_remove_all_ones_with_row_and_column_flips` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2128_remove_all_ones_with_row_and_column_flips` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2128_remove_all_ones_with_row_and_column_flips` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2128_remove_all_ones_with_row_and_column_flips` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2128_remove_all_ones_with_row_and_column_flips` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2128_remove_all_ones_with_row_and_column_flips` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2128_remove_all_ones_with_row_and_column_flips` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2128_remove_all_ones_with_row_and_column_flips` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2128_remove_all_ones_with_row_and_column_flips` |

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
.\scripts\test.ps1 -Folder 2128_remove_all_ones_with_row_and_column_flips -AllLanguages
```

```bash
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --all-languages
```

```zsh
./scripts/test.sh --folder 2128_remove_all_ones_with_row_and_column_flips --all-languages
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
