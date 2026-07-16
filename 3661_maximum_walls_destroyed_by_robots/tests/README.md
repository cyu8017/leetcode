# Test harness for 3661_maximum_walls_destroyed_by_robots

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language python
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language javascript
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language typescript
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language java
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language cpp
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language c
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language go
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language rust
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language kotlin
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language swift
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language ruby
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language csharp
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language scala
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language php
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm java java 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm c c 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm go go 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm rust rust 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm swift swift 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm scala scala 3661_maximum_walls_destroyed_by_robots
docker compose -f docker/docker-compose.yml run --rm php php 3661_maximum_walls_destroyed_by_robots
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3661_maximum_walls_destroyed_by_robots` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3661_maximum_walls_destroyed_by_robots` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3661_maximum_walls_destroyed_by_robots` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3661_maximum_walls_destroyed_by_robots` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3661_maximum_walls_destroyed_by_robots` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3661_maximum_walls_destroyed_by_robots` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3661_maximum_walls_destroyed_by_robots` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3661_maximum_walls_destroyed_by_robots` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3661_maximum_walls_destroyed_by_robots` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3661_maximum_walls_destroyed_by_robots` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3661_maximum_walls_destroyed_by_robots` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3661_maximum_walls_destroyed_by_robots` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3661_maximum_walls_destroyed_by_robots` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3661_maximum_walls_destroyed_by_robots` |

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
.\scripts\test.ps1 -Folder 3661_maximum_walls_destroyed_by_robots -AllLanguages
```

```bash
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --all-languages
```

```zsh
./scripts/test.sh --folder 3661_maximum_walls_destroyed_by_robots --all-languages
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
