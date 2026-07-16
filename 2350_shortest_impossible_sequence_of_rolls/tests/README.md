# Test harness for 2350_shortest_impossible_sequence_of_rolls

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language python
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language javascript
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language typescript
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language java
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language cpp
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language c
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language go
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language rust
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language kotlin
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language swift
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language ruby
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language csharp
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language scala
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language php
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm java java 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm c c 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm go go 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm rust rust 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm swift swift 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm scala scala 2350_shortest_impossible_sequence_of_rolls
docker compose -f docker/docker-compose.yml run --rm php php 2350_shortest_impossible_sequence_of_rolls
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2350_shortest_impossible_sequence_of_rolls` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2350_shortest_impossible_sequence_of_rolls` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2350_shortest_impossible_sequence_of_rolls` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2350_shortest_impossible_sequence_of_rolls` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2350_shortest_impossible_sequence_of_rolls` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2350_shortest_impossible_sequence_of_rolls` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2350_shortest_impossible_sequence_of_rolls` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2350_shortest_impossible_sequence_of_rolls` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2350_shortest_impossible_sequence_of_rolls` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2350_shortest_impossible_sequence_of_rolls` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2350_shortest_impossible_sequence_of_rolls` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2350_shortest_impossible_sequence_of_rolls` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2350_shortest_impossible_sequence_of_rolls` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2350_shortest_impossible_sequence_of_rolls` |

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
.\scripts\test.ps1 -Folder 2350_shortest_impossible_sequence_of_rolls -AllLanguages
```

```bash
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --all-languages
```

```zsh
./scripts/test.sh --folder 2350_shortest_impossible_sequence_of_rolls --all-languages
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
