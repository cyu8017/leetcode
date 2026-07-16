# Test harness for 3212_count_submatrices_with_equal_frequency_of_x_and_y

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language python
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language javascript
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language typescript
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language java
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language cpp
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language c
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language go
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language rust
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language kotlin
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language swift
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language ruby
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language csharp
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language scala
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language php
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm java java 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm c c 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm go go 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm rust rust 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm swift swift 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm scala scala 3212_count_submatrices_with_equal_frequency_of_x_and_y
docker compose -f docker/docker-compose.yml run --rm php php 3212_count_submatrices_with_equal_frequency_of_x_and_y
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3212_count_submatrices_with_equal_frequency_of_x_and_y` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3212_count_submatrices_with_equal_frequency_of_x_and_y` |

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
.\scripts\test.ps1 -Folder 3212_count_submatrices_with_equal_frequency_of_x_and_y -AllLanguages
```

```bash
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --all-languages
```

```zsh
./scripts/test.sh --folder 3212_count_submatrices_with_equal_frequency_of_x_and_y --all-languages
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
