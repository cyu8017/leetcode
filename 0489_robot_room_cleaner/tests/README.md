# Test harness for 0489_robot_room_cleaner

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0489_robot_room_cleaner --language python
./scripts/test.sh --folder 0489_robot_room_cleaner --language javascript
./scripts/test.sh --folder 0489_robot_room_cleaner --language typescript
./scripts/test.sh --folder 0489_robot_room_cleaner --language java
./scripts/test.sh --folder 0489_robot_room_cleaner --language cpp
./scripts/test.sh --folder 0489_robot_room_cleaner --language c
./scripts/test.sh --folder 0489_robot_room_cleaner --language go
./scripts/test.sh --folder 0489_robot_room_cleaner --language rust
./scripts/test.sh --folder 0489_robot_room_cleaner --language kotlin
./scripts/test.sh --folder 0489_robot_room_cleaner --language swift
./scripts/test.sh --folder 0489_robot_room_cleaner --language ruby
./scripts/test.sh --folder 0489_robot_room_cleaner --language csharp
./scripts/test.sh --folder 0489_robot_room_cleaner --language scala
./scripts/test.sh --folder 0489_robot_room_cleaner --language php
./scripts/test.sh --folder 0489_robot_room_cleaner --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0489_robot_room_cleaner --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm java java 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm c c 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm go go 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm rust rust 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm swift swift 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm scala scala 0489_robot_room_cleaner
docker compose -f docker/docker-compose.yml run --rm php php 0489_robot_room_cleaner
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0489_robot_room_cleaner` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0489_robot_room_cleaner` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0489_robot_room_cleaner` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0489_robot_room_cleaner` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0489_robot_room_cleaner` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0489_robot_room_cleaner` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0489_robot_room_cleaner` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0489_robot_room_cleaner` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0489_robot_room_cleaner` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0489_robot_room_cleaner` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0489_robot_room_cleaner` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0489_robot_room_cleaner` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0489_robot_room_cleaner` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0489_robot_room_cleaner` |

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
.\scripts\test.ps1 -Folder 0489_robot_room_cleaner -AllLanguages
```

```bash
./scripts/test.sh --folder 0489_robot_room_cleaner --all-languages
```

```zsh
./scripts/test.sh --folder 0489_robot_room_cleaner --all-languages
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
