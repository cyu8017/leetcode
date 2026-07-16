# Test harness for 1125_smallest_sufficient_team

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1125_smallest_sufficient_team --language python
./scripts/test.sh --folder 1125_smallest_sufficient_team --language javascript
./scripts/test.sh --folder 1125_smallest_sufficient_team --language typescript
./scripts/test.sh --folder 1125_smallest_sufficient_team --language java
./scripts/test.sh --folder 1125_smallest_sufficient_team --language cpp
./scripts/test.sh --folder 1125_smallest_sufficient_team --language c
./scripts/test.sh --folder 1125_smallest_sufficient_team --language go
./scripts/test.sh --folder 1125_smallest_sufficient_team --language rust
./scripts/test.sh --folder 1125_smallest_sufficient_team --language kotlin
./scripts/test.sh --folder 1125_smallest_sufficient_team --language swift
./scripts/test.sh --folder 1125_smallest_sufficient_team --language ruby
./scripts/test.sh --folder 1125_smallest_sufficient_team --language csharp
./scripts/test.sh --folder 1125_smallest_sufficient_team --language scala
./scripts/test.sh --folder 1125_smallest_sufficient_team --language php
./scripts/test.sh --folder 1125_smallest_sufficient_team --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1125_smallest_sufficient_team --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm java java 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm c c 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm go go 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm rust rust 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm swift swift 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm scala scala 1125_smallest_sufficient_team
docker compose -f docker/docker-compose.yml run --rm php php 1125_smallest_sufficient_team
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1125_smallest_sufficient_team` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1125_smallest_sufficient_team` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1125_smallest_sufficient_team` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1125_smallest_sufficient_team` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1125_smallest_sufficient_team` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1125_smallest_sufficient_team` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1125_smallest_sufficient_team` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1125_smallest_sufficient_team` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1125_smallest_sufficient_team` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1125_smallest_sufficient_team` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1125_smallest_sufficient_team` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1125_smallest_sufficient_team` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1125_smallest_sufficient_team` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1125_smallest_sufficient_team` |

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
.\scripts\test.ps1 -Folder 1125_smallest_sufficient_team -AllLanguages
```

```bash
./scripts/test.sh --folder 1125_smallest_sufficient_team --all-languages
```

```zsh
./scripts/test.sh --folder 1125_smallest_sufficient_team --all-languages
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
