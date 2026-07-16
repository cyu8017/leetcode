# Test harness for 3028_ant_on_the_boundary

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3028_ant_on_the_boundary --language python
./scripts/test.sh --folder 3028_ant_on_the_boundary --language javascript
./scripts/test.sh --folder 3028_ant_on_the_boundary --language typescript
./scripts/test.sh --folder 3028_ant_on_the_boundary --language java
./scripts/test.sh --folder 3028_ant_on_the_boundary --language cpp
./scripts/test.sh --folder 3028_ant_on_the_boundary --language c
./scripts/test.sh --folder 3028_ant_on_the_boundary --language go
./scripts/test.sh --folder 3028_ant_on_the_boundary --language rust
./scripts/test.sh --folder 3028_ant_on_the_boundary --language kotlin
./scripts/test.sh --folder 3028_ant_on_the_boundary --language swift
./scripts/test.sh --folder 3028_ant_on_the_boundary --language ruby
./scripts/test.sh --folder 3028_ant_on_the_boundary --language csharp
./scripts/test.sh --folder 3028_ant_on_the_boundary --language scala
./scripts/test.sh --folder 3028_ant_on_the_boundary --language php
./scripts/test.sh --folder 3028_ant_on_the_boundary --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3028_ant_on_the_boundary --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm java java 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm c c 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm go go 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm rust rust 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm swift swift 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm scala scala 3028_ant_on_the_boundary
docker compose -f docker/docker-compose.yml run --rm php php 3028_ant_on_the_boundary
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3028_ant_on_the_boundary` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3028_ant_on_the_boundary` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3028_ant_on_the_boundary` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3028_ant_on_the_boundary` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3028_ant_on_the_boundary` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3028_ant_on_the_boundary` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3028_ant_on_the_boundary` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3028_ant_on_the_boundary` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3028_ant_on_the_boundary` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3028_ant_on_the_boundary` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3028_ant_on_the_boundary` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3028_ant_on_the_boundary` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3028_ant_on_the_boundary` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3028_ant_on_the_boundary` |

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
.\scripts\test.ps1 -Folder 3028_ant_on_the_boundary -AllLanguages
```

```bash
./scripts/test.sh --folder 3028_ant_on_the_boundary --all-languages
```

```zsh
./scripts/test.sh --folder 3028_ant_on_the_boundary --all-languages
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
