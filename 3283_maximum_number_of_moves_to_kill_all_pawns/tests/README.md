# Test harness for 3283_maximum_number_of_moves_to_kill_all_pawns

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language python
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language javascript
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language typescript
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language java
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language cpp
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language c
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language go
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language rust
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language kotlin
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language swift
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language ruby
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language csharp
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language scala
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language php
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm java java 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm c c 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm go go 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm rust rust 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm swift swift 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm scala scala 3283_maximum_number_of_moves_to_kill_all_pawns
docker compose -f docker/docker-compose.yml run --rm php php 3283_maximum_number_of_moves_to_kill_all_pawns
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3283_maximum_number_of_moves_to_kill_all_pawns` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3283_maximum_number_of_moves_to_kill_all_pawns` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3283_maximum_number_of_moves_to_kill_all_pawns` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3283_maximum_number_of_moves_to_kill_all_pawns` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3283_maximum_number_of_moves_to_kill_all_pawns` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3283_maximum_number_of_moves_to_kill_all_pawns` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3283_maximum_number_of_moves_to_kill_all_pawns` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3283_maximum_number_of_moves_to_kill_all_pawns` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3283_maximum_number_of_moves_to_kill_all_pawns` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3283_maximum_number_of_moves_to_kill_all_pawns` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3283_maximum_number_of_moves_to_kill_all_pawns` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3283_maximum_number_of_moves_to_kill_all_pawns` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3283_maximum_number_of_moves_to_kill_all_pawns` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3283_maximum_number_of_moves_to_kill_all_pawns` |

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
.\scripts\test.ps1 -Folder 3283_maximum_number_of_moves_to_kill_all_pawns -AllLanguages
```

```bash
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --all-languages
```

```zsh
./scripts/test.sh --folder 3283_maximum_number_of_moves_to_kill_all_pawns --all-languages
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
