# Test harness for 2385_amount_of_time_for_binary_tree_to_be_infected

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language python
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language javascript
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language typescript
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language java
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language cpp
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language c
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language go
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language rust
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language kotlin
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language swift
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language ruby
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language csharp
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language scala
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language php
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm java java 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm c c 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm go go 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm rust rust 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm swift swift 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm scala scala 2385_amount_of_time_for_binary_tree_to_be_infected
docker compose -f docker/docker-compose.yml run --rm php php 2385_amount_of_time_for_binary_tree_to_be_infected
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2385_amount_of_time_for_binary_tree_to_be_infected` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2385_amount_of_time_for_binary_tree_to_be_infected` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2385_amount_of_time_for_binary_tree_to_be_infected` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2385_amount_of_time_for_binary_tree_to_be_infected` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2385_amount_of_time_for_binary_tree_to_be_infected` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2385_amount_of_time_for_binary_tree_to_be_infected` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2385_amount_of_time_for_binary_tree_to_be_infected` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2385_amount_of_time_for_binary_tree_to_be_infected` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2385_amount_of_time_for_binary_tree_to_be_infected` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2385_amount_of_time_for_binary_tree_to_be_infected` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2385_amount_of_time_for_binary_tree_to_be_infected` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2385_amount_of_time_for_binary_tree_to_be_infected` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2385_amount_of_time_for_binary_tree_to_be_infected` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2385_amount_of_time_for_binary_tree_to_be_infected` |

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
.\scripts\test.ps1 -Folder 2385_amount_of_time_for_binary_tree_to_be_infected -AllLanguages
```

```bash
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --all-languages
```

```zsh
./scripts/test.sh --folder 2385_amount_of_time_for_binary_tree_to_be_infected --all-languages
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
