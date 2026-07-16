# Test harness for 3672_sum_of_weighted_modes_in_subarrays

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language python
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language javascript
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language typescript
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language java
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language cpp
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language c
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language go
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language rust
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language kotlin
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language swift
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language ruby
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language csharp
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language scala
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language php
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm java java 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm c c 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm go go 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm rust rust 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm swift swift 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm scala scala 3672_sum_of_weighted_modes_in_subarrays
docker compose -f docker/docker-compose.yml run --rm php php 3672_sum_of_weighted_modes_in_subarrays
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3672_sum_of_weighted_modes_in_subarrays` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3672_sum_of_weighted_modes_in_subarrays` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3672_sum_of_weighted_modes_in_subarrays` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3672_sum_of_weighted_modes_in_subarrays` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3672_sum_of_weighted_modes_in_subarrays` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3672_sum_of_weighted_modes_in_subarrays` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3672_sum_of_weighted_modes_in_subarrays` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3672_sum_of_weighted_modes_in_subarrays` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3672_sum_of_weighted_modes_in_subarrays` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3672_sum_of_weighted_modes_in_subarrays` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3672_sum_of_weighted_modes_in_subarrays` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3672_sum_of_weighted_modes_in_subarrays` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3672_sum_of_weighted_modes_in_subarrays` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3672_sum_of_weighted_modes_in_subarrays` |

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
.\scripts\test.ps1 -Folder 3672_sum_of_weighted_modes_in_subarrays -AllLanguages
```

```bash
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --all-languages
```

```zsh
./scripts/test.sh --folder 3672_sum_of_weighted_modes_in_subarrays --all-languages
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
