# Test harness for 2792_count_nodes_that_are_great_enough

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language python
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language javascript
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language typescript
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language java
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language cpp
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language c
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language go
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language rust
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language kotlin
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language swift
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language ruby
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language csharp
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language scala
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language php
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm java java 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm c c 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm go go 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm rust rust 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm swift swift 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm scala scala 2792_count_nodes_that_are_great_enough
docker compose -f docker/docker-compose.yml run --rm php php 2792_count_nodes_that_are_great_enough
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2792_count_nodes_that_are_great_enough` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2792_count_nodes_that_are_great_enough` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2792_count_nodes_that_are_great_enough` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2792_count_nodes_that_are_great_enough` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2792_count_nodes_that_are_great_enough` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2792_count_nodes_that_are_great_enough` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2792_count_nodes_that_are_great_enough` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2792_count_nodes_that_are_great_enough` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2792_count_nodes_that_are_great_enough` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2792_count_nodes_that_are_great_enough` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2792_count_nodes_that_are_great_enough` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2792_count_nodes_that_are_great_enough` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2792_count_nodes_that_are_great_enough` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2792_count_nodes_that_are_great_enough` |

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
.\scripts\test.ps1 -Folder 2792_count_nodes_that_are_great_enough -AllLanguages
```

```bash
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --all-languages
```

```zsh
./scripts/test.sh --folder 2792_count_nodes_that_are_great_enough --all-languages
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
