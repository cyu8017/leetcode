# Test harness for 0733_flood_fill

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0733_flood_fill -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0733_flood_fill --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0733_flood_fill --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0733_flood_fill --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0733_flood_fill --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0733_flood_fill --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0733_flood_fill --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0733_flood_fill --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0733_flood_fill --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0733_flood_fill --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0733_flood_fill --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0733_flood_fill --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0733_flood_fill --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0733_flood_fill --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0733_flood_fill --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0733_flood_fill --language python
./scripts/test.sh --folder 0733_flood_fill --language javascript
./scripts/test.sh --folder 0733_flood_fill --language typescript
./scripts/test.sh --folder 0733_flood_fill --language java
./scripts/test.sh --folder 0733_flood_fill --language cpp
./scripts/test.sh --folder 0733_flood_fill --language c
./scripts/test.sh --folder 0733_flood_fill --language go
./scripts/test.sh --folder 0733_flood_fill --language rust
./scripts/test.sh --folder 0733_flood_fill --language kotlin
./scripts/test.sh --folder 0733_flood_fill --language swift
./scripts/test.sh --folder 0733_flood_fill --language ruby
./scripts/test.sh --folder 0733_flood_fill --language csharp
./scripts/test.sh --folder 0733_flood_fill --language scala
./scripts/test.sh --folder 0733_flood_fill --language php
./scripts/test.sh --folder 0733_flood_fill --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0733_flood_fill --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0733_flood_fill --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0733_flood_fill --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0733_flood_fill --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0733_flood_fill --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0733_flood_fill --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0733_flood_fill --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0733_flood_fill --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0733_flood_fill --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0733_flood_fill --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0733_flood_fill --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0733_flood_fill --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0733_flood_fill --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0733_flood_fill --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm java java 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm c c 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm go go 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm rust rust 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm swift swift 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm scala scala 0733_flood_fill
docker compose -f docker/docker-compose.yml run --rm php php 0733_flood_fill
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0733_flood_fill` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0733_flood_fill` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0733_flood_fill` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0733_flood_fill` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0733_flood_fill` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0733_flood_fill` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0733_flood_fill` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0733_flood_fill` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0733_flood_fill` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0733_flood_fill` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0733_flood_fill` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0733_flood_fill` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0733_flood_fill` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0733_flood_fill` |

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
.\scripts\test.ps1 -Folder 0733_flood_fill -AllLanguages
```

```bash
./scripts/test.sh --folder 0733_flood_fill --all-languages
```

```zsh
./scripts/test.sh --folder 0733_flood_fill --all-languages
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
