# Test harness for 1042_flower_planting_with_no_adjacent

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language python
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language javascript
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language typescript
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language java
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language cpp
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language c
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language go
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language rust
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language kotlin
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language swift
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language ruby
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language csharp
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language scala
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language php
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm java java 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm c c 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm go go 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm rust rust 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm swift swift 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm scala scala 1042_flower_planting_with_no_adjacent
docker compose -f docker/docker-compose.yml run --rm php php 1042_flower_planting_with_no_adjacent
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1042_flower_planting_with_no_adjacent` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1042_flower_planting_with_no_adjacent` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1042_flower_planting_with_no_adjacent` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1042_flower_planting_with_no_adjacent` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1042_flower_planting_with_no_adjacent` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1042_flower_planting_with_no_adjacent` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1042_flower_planting_with_no_adjacent` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1042_flower_planting_with_no_adjacent` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1042_flower_planting_with_no_adjacent` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1042_flower_planting_with_no_adjacent` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1042_flower_planting_with_no_adjacent` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1042_flower_planting_with_no_adjacent` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1042_flower_planting_with_no_adjacent` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1042_flower_planting_with_no_adjacent` |

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
.\scripts\test.ps1 -Folder 1042_flower_planting_with_no_adjacent -AllLanguages
```

```bash
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --all-languages
```

```zsh
./scripts/test.sh --folder 1042_flower_planting_with_no_adjacent --all-languages
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
