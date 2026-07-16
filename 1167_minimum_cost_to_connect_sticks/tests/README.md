# Test harness for 1167_minimum_cost_to_connect_sticks

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language python
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language javascript
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language typescript
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language java
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language cpp
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language c
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language go
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language rust
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language kotlin
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language swift
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language ruby
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language csharp
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language scala
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language php
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm java java 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm c c 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm go go 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm rust rust 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm swift swift 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm scala scala 1167_minimum_cost_to_connect_sticks
docker compose -f docker/docker-compose.yml run --rm php php 1167_minimum_cost_to_connect_sticks
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1167_minimum_cost_to_connect_sticks` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1167_minimum_cost_to_connect_sticks` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1167_minimum_cost_to_connect_sticks` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1167_minimum_cost_to_connect_sticks` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1167_minimum_cost_to_connect_sticks` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1167_minimum_cost_to_connect_sticks` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1167_minimum_cost_to_connect_sticks` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1167_minimum_cost_to_connect_sticks` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1167_minimum_cost_to_connect_sticks` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1167_minimum_cost_to_connect_sticks` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1167_minimum_cost_to_connect_sticks` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1167_minimum_cost_to_connect_sticks` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1167_minimum_cost_to_connect_sticks` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1167_minimum_cost_to_connect_sticks` |

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
.\scripts\test.ps1 -Folder 1167_minimum_cost_to_connect_sticks -AllLanguages
```

```bash
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --all-languages
```

```zsh
./scripts/test.sh --folder 1167_minimum_cost_to_connect_sticks --all-languages
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
