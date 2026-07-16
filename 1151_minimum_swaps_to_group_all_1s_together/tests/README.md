# Test harness for 1151_minimum_swaps_to_group_all_1s_together

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language python
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language javascript
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language typescript
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language java
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language cpp
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language c
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language go
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language rust
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language kotlin
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language swift
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language ruby
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language csharp
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language scala
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language php
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm java java 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm c c 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm go go 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm rust rust 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm swift swift 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm scala scala 1151_minimum_swaps_to_group_all_1s_together
docker compose -f docker/docker-compose.yml run --rm php php 1151_minimum_swaps_to_group_all_1s_together
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1151_minimum_swaps_to_group_all_1s_together` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1151_minimum_swaps_to_group_all_1s_together` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1151_minimum_swaps_to_group_all_1s_together` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1151_minimum_swaps_to_group_all_1s_together` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1151_minimum_swaps_to_group_all_1s_together` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1151_minimum_swaps_to_group_all_1s_together` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1151_minimum_swaps_to_group_all_1s_together` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1151_minimum_swaps_to_group_all_1s_together` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1151_minimum_swaps_to_group_all_1s_together` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1151_minimum_swaps_to_group_all_1s_together` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1151_minimum_swaps_to_group_all_1s_together` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1151_minimum_swaps_to_group_all_1s_together` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1151_minimum_swaps_to_group_all_1s_together` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1151_minimum_swaps_to_group_all_1s_together` |

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
.\scripts\test.ps1 -Folder 1151_minimum_swaps_to_group_all_1s_together -AllLanguages
```

```bash
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --all-languages
```

```zsh
./scripts/test.sh --folder 1151_minimum_swaps_to_group_all_1s_together --all-languages
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
