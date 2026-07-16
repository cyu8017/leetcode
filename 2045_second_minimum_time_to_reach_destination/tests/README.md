# Test harness for 2045_second_minimum_time_to_reach_destination

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language python
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language javascript
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language typescript
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language java
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language cpp
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language c
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language go
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language rust
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language kotlin
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language swift
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language ruby
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language csharp
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language scala
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language php
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm java java 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm c c 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm go go 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm rust rust 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm swift swift 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm scala scala 2045_second_minimum_time_to_reach_destination
docker compose -f docker/docker-compose.yml run --rm php php 2045_second_minimum_time_to_reach_destination
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2045_second_minimum_time_to_reach_destination` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2045_second_minimum_time_to_reach_destination` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2045_second_minimum_time_to_reach_destination` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2045_second_minimum_time_to_reach_destination` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2045_second_minimum_time_to_reach_destination` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2045_second_minimum_time_to_reach_destination` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2045_second_minimum_time_to_reach_destination` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2045_second_minimum_time_to_reach_destination` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2045_second_minimum_time_to_reach_destination` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2045_second_minimum_time_to_reach_destination` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2045_second_minimum_time_to_reach_destination` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2045_second_minimum_time_to_reach_destination` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2045_second_minimum_time_to_reach_destination` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2045_second_minimum_time_to_reach_destination` |

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
.\scripts\test.ps1 -Folder 2045_second_minimum_time_to_reach_destination -AllLanguages
```

```bash
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --all-languages
```

```zsh
./scripts/test.sh --folder 2045_second_minimum_time_to_reach_destination --all-languages
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
