# Test harness for 1079_letter_tile_possibilities

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1079_letter_tile_possibilities --language python
./scripts/test.sh --folder 1079_letter_tile_possibilities --language javascript
./scripts/test.sh --folder 1079_letter_tile_possibilities --language typescript
./scripts/test.sh --folder 1079_letter_tile_possibilities --language java
./scripts/test.sh --folder 1079_letter_tile_possibilities --language cpp
./scripts/test.sh --folder 1079_letter_tile_possibilities --language c
./scripts/test.sh --folder 1079_letter_tile_possibilities --language go
./scripts/test.sh --folder 1079_letter_tile_possibilities --language rust
./scripts/test.sh --folder 1079_letter_tile_possibilities --language kotlin
./scripts/test.sh --folder 1079_letter_tile_possibilities --language swift
./scripts/test.sh --folder 1079_letter_tile_possibilities --language ruby
./scripts/test.sh --folder 1079_letter_tile_possibilities --language csharp
./scripts/test.sh --folder 1079_letter_tile_possibilities --language scala
./scripts/test.sh --folder 1079_letter_tile_possibilities --language php
./scripts/test.sh --folder 1079_letter_tile_possibilities --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1079_letter_tile_possibilities --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm java java 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm c c 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm go go 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm rust rust 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm swift swift 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm scala scala 1079_letter_tile_possibilities
docker compose -f docker/docker-compose.yml run --rm php php 1079_letter_tile_possibilities
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1079_letter_tile_possibilities` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1079_letter_tile_possibilities` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1079_letter_tile_possibilities` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1079_letter_tile_possibilities` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1079_letter_tile_possibilities` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1079_letter_tile_possibilities` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1079_letter_tile_possibilities` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1079_letter_tile_possibilities` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1079_letter_tile_possibilities` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1079_letter_tile_possibilities` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1079_letter_tile_possibilities` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1079_letter_tile_possibilities` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1079_letter_tile_possibilities` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1079_letter_tile_possibilities` |

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
.\scripts\test.ps1 -Folder 1079_letter_tile_possibilities -AllLanguages
```

```bash
./scripts/test.sh --folder 1079_letter_tile_possibilities --all-languages
```

```zsh
./scripts/test.sh --folder 1079_letter_tile_possibilities --all-languages
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
