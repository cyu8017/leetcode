# Test harness for 4001_aggregate_two_time_series

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 4001_aggregate_two_time_series --language python
./scripts/test.sh --folder 4001_aggregate_two_time_series --language javascript
./scripts/test.sh --folder 4001_aggregate_two_time_series --language typescript
./scripts/test.sh --folder 4001_aggregate_two_time_series --language java
./scripts/test.sh --folder 4001_aggregate_two_time_series --language cpp
./scripts/test.sh --folder 4001_aggregate_two_time_series --language c
./scripts/test.sh --folder 4001_aggregate_two_time_series --language go
./scripts/test.sh --folder 4001_aggregate_two_time_series --language rust
./scripts/test.sh --folder 4001_aggregate_two_time_series --language kotlin
./scripts/test.sh --folder 4001_aggregate_two_time_series --language swift
./scripts/test.sh --folder 4001_aggregate_two_time_series --language ruby
./scripts/test.sh --folder 4001_aggregate_two_time_series --language csharp
./scripts/test.sh --folder 4001_aggregate_two_time_series --language scala
./scripts/test.sh --folder 4001_aggregate_two_time_series --language php
./scripts/test.sh --folder 4001_aggregate_two_time_series --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 4001_aggregate_two_time_series --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm javascript javascript 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm typescript typescript 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm java java 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm cpp cpp 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm c c 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm go go 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm rust rust 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm swift swift 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm ruby ruby 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm csharp csharp 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm scala scala 4001_aggregate_two_time_series
docker compose -f docker/docker-compose.yml run --rm php php 4001_aggregate_two_time_series
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 4001_aggregate_two_time_series` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 4001_aggregate_two_time_series` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 4001_aggregate_two_time_series` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 4001_aggregate_two_time_series` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 4001_aggregate_two_time_series` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 4001_aggregate_two_time_series` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 4001_aggregate_two_time_series` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 4001_aggregate_two_time_series` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 4001_aggregate_two_time_series` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 4001_aggregate_two_time_series` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 4001_aggregate_two_time_series` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 4001_aggregate_two_time_series` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 4001_aggregate_two_time_series` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 4001_aggregate_two_time_series` |

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
.\scripts\test.ps1 -Folder 4001_aggregate_two_time_series -AllLanguages
```

```bash
./scripts/test.sh --folder 4001_aggregate_two_time_series --all-languages
```

```zsh
./scripts/test.sh --folder 4001_aggregate_two_time_series --all-languages
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
