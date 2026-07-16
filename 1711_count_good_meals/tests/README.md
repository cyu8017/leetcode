# Test harness for 1711_count_good_meals

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1711_count_good_meals -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1711_count_good_meals --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1711_count_good_meals --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1711_count_good_meals --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1711_count_good_meals --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1711_count_good_meals --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1711_count_good_meals --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1711_count_good_meals --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1711_count_good_meals --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1711_count_good_meals --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1711_count_good_meals --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1711_count_good_meals --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1711_count_good_meals --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1711_count_good_meals --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1711_count_good_meals --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1711_count_good_meals --language python
./scripts/test.sh --folder 1711_count_good_meals --language javascript
./scripts/test.sh --folder 1711_count_good_meals --language typescript
./scripts/test.sh --folder 1711_count_good_meals --language java
./scripts/test.sh --folder 1711_count_good_meals --language cpp
./scripts/test.sh --folder 1711_count_good_meals --language c
./scripts/test.sh --folder 1711_count_good_meals --language go
./scripts/test.sh --folder 1711_count_good_meals --language rust
./scripts/test.sh --folder 1711_count_good_meals --language kotlin
./scripts/test.sh --folder 1711_count_good_meals --language swift
./scripts/test.sh --folder 1711_count_good_meals --language ruby
./scripts/test.sh --folder 1711_count_good_meals --language csharp
./scripts/test.sh --folder 1711_count_good_meals --language scala
./scripts/test.sh --folder 1711_count_good_meals --language php
./scripts/test.sh --folder 1711_count_good_meals --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1711_count_good_meals --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1711_count_good_meals --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1711_count_good_meals --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1711_count_good_meals --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1711_count_good_meals --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1711_count_good_meals --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1711_count_good_meals --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1711_count_good_meals --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1711_count_good_meals --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1711_count_good_meals --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1711_count_good_meals --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1711_count_good_meals --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1711_count_good_meals --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1711_count_good_meals --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm java java 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm c c 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm go go 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm rust rust 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm swift swift 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm scala scala 1711_count_good_meals
docker compose -f docker/docker-compose.yml run --rm php php 1711_count_good_meals
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1711_count_good_meals` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1711_count_good_meals` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1711_count_good_meals` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1711_count_good_meals` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1711_count_good_meals` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1711_count_good_meals` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1711_count_good_meals` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1711_count_good_meals` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1711_count_good_meals` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1711_count_good_meals` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1711_count_good_meals` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1711_count_good_meals` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1711_count_good_meals` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1711_count_good_meals` |

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
.\scripts\test.ps1 -Folder 1711_count_good_meals -AllLanguages
```

```bash
./scripts/test.sh --folder 1711_count_good_meals --all-languages
```

```zsh
./scripts/test.sh --folder 1711_count_good_meals --all-languages
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
