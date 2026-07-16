# Test harness for 3893_maximum_team_size_with_overlapping_intervals

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language python
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language javascript
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language typescript
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language java
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language cpp
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language c
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language go
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language rust
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language kotlin
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language swift
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language ruby
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language csharp
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language scala
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language php
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm java java 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm c c 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm go go 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm rust rust 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm swift swift 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm scala scala 3893_maximum_team_size_with_overlapping_intervals
docker compose -f docker/docker-compose.yml run --rm php php 3893_maximum_team_size_with_overlapping_intervals
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3893_maximum_team_size_with_overlapping_intervals` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3893_maximum_team_size_with_overlapping_intervals` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3893_maximum_team_size_with_overlapping_intervals` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3893_maximum_team_size_with_overlapping_intervals` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3893_maximum_team_size_with_overlapping_intervals` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3893_maximum_team_size_with_overlapping_intervals` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3893_maximum_team_size_with_overlapping_intervals` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3893_maximum_team_size_with_overlapping_intervals` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3893_maximum_team_size_with_overlapping_intervals` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3893_maximum_team_size_with_overlapping_intervals` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3893_maximum_team_size_with_overlapping_intervals` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3893_maximum_team_size_with_overlapping_intervals` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3893_maximum_team_size_with_overlapping_intervals` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3893_maximum_team_size_with_overlapping_intervals` |

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
.\scripts\test.ps1 -Folder 3893_maximum_team_size_with_overlapping_intervals -AllLanguages
```

```bash
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --all-languages
```

```zsh
./scripts/test.sh --folder 3893_maximum_team_size_with_overlapping_intervals --all-languages
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
