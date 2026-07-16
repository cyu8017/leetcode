# Test harness for 1595_minimum_cost_to_connect_two_groups_of_points

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language python
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language javascript
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language typescript
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language java
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language cpp
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language c
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language go
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language rust
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language kotlin
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language swift
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language ruby
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language csharp
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language scala
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language php
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm java java 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm c c 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm go go 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm rust rust 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm swift swift 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm scala scala 1595_minimum_cost_to_connect_two_groups_of_points
docker compose -f docker/docker-compose.yml run --rm php php 1595_minimum_cost_to_connect_two_groups_of_points
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1595_minimum_cost_to_connect_two_groups_of_points` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1595_minimum_cost_to_connect_two_groups_of_points` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1595_minimum_cost_to_connect_two_groups_of_points` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1595_minimum_cost_to_connect_two_groups_of_points` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1595_minimum_cost_to_connect_two_groups_of_points` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1595_minimum_cost_to_connect_two_groups_of_points` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1595_minimum_cost_to_connect_two_groups_of_points` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1595_minimum_cost_to_connect_two_groups_of_points` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1595_minimum_cost_to_connect_two_groups_of_points` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1595_minimum_cost_to_connect_two_groups_of_points` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1595_minimum_cost_to_connect_two_groups_of_points` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1595_minimum_cost_to_connect_two_groups_of_points` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1595_minimum_cost_to_connect_two_groups_of_points` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1595_minimum_cost_to_connect_two_groups_of_points` |

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
.\scripts\test.ps1 -Folder 1595_minimum_cost_to_connect_two_groups_of_points -AllLanguages
```

```bash
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --all-languages
```

```zsh
./scripts/test.sh --folder 1595_minimum_cost_to_connect_two_groups_of_points --all-languages
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
