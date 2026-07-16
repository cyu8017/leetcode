# Test harness for 1801_number_of_orders_in_the_backlog

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language python
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language javascript
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language typescript
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language java
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language cpp
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language c
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language go
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language rust
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language kotlin
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language swift
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language ruby
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language csharp
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language scala
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language php
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm java java 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm c c 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm go go 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm rust rust 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm swift swift 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm scala scala 1801_number_of_orders_in_the_backlog
docker compose -f docker/docker-compose.yml run --rm php php 1801_number_of_orders_in_the_backlog
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1801_number_of_orders_in_the_backlog` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1801_number_of_orders_in_the_backlog` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1801_number_of_orders_in_the_backlog` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1801_number_of_orders_in_the_backlog` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1801_number_of_orders_in_the_backlog` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1801_number_of_orders_in_the_backlog` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1801_number_of_orders_in_the_backlog` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1801_number_of_orders_in_the_backlog` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1801_number_of_orders_in_the_backlog` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1801_number_of_orders_in_the_backlog` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1801_number_of_orders_in_the_backlog` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1801_number_of_orders_in_the_backlog` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1801_number_of_orders_in_the_backlog` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1801_number_of_orders_in_the_backlog` |

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
.\scripts\test.ps1 -Folder 1801_number_of_orders_in_the_backlog -AllLanguages
```

```bash
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --all-languages
```

```zsh
./scripts/test.sh --folder 1801_number_of_orders_in_the_backlog --all-languages
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
