# Test harness for 2209_minimum_white_tiles_after_covering_with_carpets

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language python
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language javascript
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language typescript
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language java
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language cpp
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language c
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language go
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language rust
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language kotlin
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language swift
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language ruby
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language csharp
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language scala
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language php
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm java java 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm c c 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm go go 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm rust rust 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm swift swift 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm scala scala 2209_minimum_white_tiles_after_covering_with_carpets
docker compose -f docker/docker-compose.yml run --rm php php 2209_minimum_white_tiles_after_covering_with_carpets
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2209_minimum_white_tiles_after_covering_with_carpets` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2209_minimum_white_tiles_after_covering_with_carpets` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2209_minimum_white_tiles_after_covering_with_carpets` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2209_minimum_white_tiles_after_covering_with_carpets` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2209_minimum_white_tiles_after_covering_with_carpets` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2209_minimum_white_tiles_after_covering_with_carpets` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2209_minimum_white_tiles_after_covering_with_carpets` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2209_minimum_white_tiles_after_covering_with_carpets` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2209_minimum_white_tiles_after_covering_with_carpets` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2209_minimum_white_tiles_after_covering_with_carpets` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2209_minimum_white_tiles_after_covering_with_carpets` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2209_minimum_white_tiles_after_covering_with_carpets` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2209_minimum_white_tiles_after_covering_with_carpets` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2209_minimum_white_tiles_after_covering_with_carpets` |

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
.\scripts\test.ps1 -Folder 2209_minimum_white_tiles_after_covering_with_carpets -AllLanguages
```

```bash
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --all-languages
```

```zsh
./scripts/test.sh --folder 2209_minimum_white_tiles_after_covering_with_carpets --all-languages
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
