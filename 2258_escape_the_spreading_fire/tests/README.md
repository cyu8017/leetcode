# Test harness for 2258_escape_the_spreading_fire

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language python
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language javascript
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language typescript
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language java
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language cpp
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language c
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language go
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language rust
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language kotlin
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language swift
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language ruby
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language csharp
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language scala
./scripts/test.sh --folder 2258_escape_the_spreading_fire --language php
./scripts/test.sh --folder 2258_escape_the_spreading_fire --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2258_escape_the_spreading_fire --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm java java 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm c c 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm go go 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm rust rust 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm swift swift 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm scala scala 2258_escape_the_spreading_fire
docker compose -f docker/docker-compose.yml run --rm php php 2258_escape_the_spreading_fire
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2258_escape_the_spreading_fire` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2258_escape_the_spreading_fire` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2258_escape_the_spreading_fire` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2258_escape_the_spreading_fire` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2258_escape_the_spreading_fire` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2258_escape_the_spreading_fire` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2258_escape_the_spreading_fire` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2258_escape_the_spreading_fire` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2258_escape_the_spreading_fire` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2258_escape_the_spreading_fire` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2258_escape_the_spreading_fire` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2258_escape_the_spreading_fire` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2258_escape_the_spreading_fire` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2258_escape_the_spreading_fire` |

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
.\scripts\test.ps1 -Folder 2258_escape_the_spreading_fire -AllLanguages
```

```bash
./scripts/test.sh --folder 2258_escape_the_spreading_fire --all-languages
```

```zsh
./scripts/test.sh --folder 2258_escape_the_spreading_fire --all-languages
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
