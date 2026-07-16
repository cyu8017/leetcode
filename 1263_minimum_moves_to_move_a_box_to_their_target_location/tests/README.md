# Test harness for 1263_minimum_moves_to_move_a_box_to_their_target_location

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language python
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language javascript
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language typescript
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language java
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language cpp
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language c
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language go
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language rust
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language kotlin
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language swift
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language ruby
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language csharp
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language scala
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language php
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm java java 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm c c 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm go go 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm rust rust 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm swift swift 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm scala scala 1263_minimum_moves_to_move_a_box_to_their_target_location
docker compose -f docker/docker-compose.yml run --rm php php 1263_minimum_moves_to_move_a_box_to_their_target_location
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1263_minimum_moves_to_move_a_box_to_their_target_location` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1263_minimum_moves_to_move_a_box_to_their_target_location` |

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
.\scripts\test.ps1 -Folder 1263_minimum_moves_to_move_a_box_to_their_target_location -AllLanguages
```

```bash
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --all-languages
```

```zsh
./scripts/test.sh --folder 1263_minimum_moves_to_move_a_box_to_their_target_location --all-languages
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
