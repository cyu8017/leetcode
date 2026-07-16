# Test harness for 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language python
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language javascript
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language typescript
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language java
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language cpp
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language c
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language go
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language rust
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language kotlin
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language swift
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language ruby
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language csharp
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language scala
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language php
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm java java 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm c c 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm go go 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm rust rust 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm swift swift 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm scala scala 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
docker compose -f docker/docker-compose.yml run --rm php php 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts` |

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
.\scripts\test.ps1 -Folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts -AllLanguages
```

```bash
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --all-languages
```

```zsh
./scripts/test.sh --folder 1465_maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts --all-languages
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
