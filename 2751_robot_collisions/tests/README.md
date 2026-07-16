# Test harness for 2751_robot_collisions

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2751_robot_collisions -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2751_robot_collisions --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2751_robot_collisions --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2751_robot_collisions --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2751_robot_collisions --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2751_robot_collisions --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2751_robot_collisions --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2751_robot_collisions --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2751_robot_collisions --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2751_robot_collisions --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2751_robot_collisions --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2751_robot_collisions --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2751_robot_collisions --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2751_robot_collisions --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2751_robot_collisions --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2751_robot_collisions --language python
./scripts/test.sh --folder 2751_robot_collisions --language javascript
./scripts/test.sh --folder 2751_robot_collisions --language typescript
./scripts/test.sh --folder 2751_robot_collisions --language java
./scripts/test.sh --folder 2751_robot_collisions --language cpp
./scripts/test.sh --folder 2751_robot_collisions --language c
./scripts/test.sh --folder 2751_robot_collisions --language go
./scripts/test.sh --folder 2751_robot_collisions --language rust
./scripts/test.sh --folder 2751_robot_collisions --language kotlin
./scripts/test.sh --folder 2751_robot_collisions --language swift
./scripts/test.sh --folder 2751_robot_collisions --language ruby
./scripts/test.sh --folder 2751_robot_collisions --language csharp
./scripts/test.sh --folder 2751_robot_collisions --language scala
./scripts/test.sh --folder 2751_robot_collisions --language php
./scripts/test.sh --folder 2751_robot_collisions --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2751_robot_collisions --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2751_robot_collisions --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2751_robot_collisions --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2751_robot_collisions --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2751_robot_collisions --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2751_robot_collisions --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2751_robot_collisions --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2751_robot_collisions --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2751_robot_collisions --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2751_robot_collisions --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2751_robot_collisions --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2751_robot_collisions --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2751_robot_collisions --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2751_robot_collisions --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm java java 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm c c 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm go go 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm rust rust 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm swift swift 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm scala scala 2751_robot_collisions
docker compose -f docker/docker-compose.yml run --rm php php 2751_robot_collisions
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2751_robot_collisions` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2751_robot_collisions` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2751_robot_collisions` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2751_robot_collisions` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2751_robot_collisions` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2751_robot_collisions` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2751_robot_collisions` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2751_robot_collisions` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2751_robot_collisions` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2751_robot_collisions` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2751_robot_collisions` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2751_robot_collisions` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2751_robot_collisions` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2751_robot_collisions` |

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
.\scripts\test.ps1 -Folder 2751_robot_collisions -AllLanguages
```

```bash
./scripts/test.sh --folder 2751_robot_collisions --all-languages
```

```zsh
./scripts/test.sh --folder 2751_robot_collisions --all-languages
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
