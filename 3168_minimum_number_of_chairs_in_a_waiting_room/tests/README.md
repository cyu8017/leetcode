# Test harness for 3168_minimum_number_of_chairs_in_a_waiting_room

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language python
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language javascript
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language typescript
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language java
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language cpp
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language c
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language go
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language rust
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language kotlin
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language swift
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language ruby
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language csharp
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language scala
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language php
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm java java 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm c c 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm go go 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm rust rust 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm swift swift 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm scala scala 3168_minimum_number_of_chairs_in_a_waiting_room
docker compose -f docker/docker-compose.yml run --rm php php 3168_minimum_number_of_chairs_in_a_waiting_room
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3168_minimum_number_of_chairs_in_a_waiting_room` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3168_minimum_number_of_chairs_in_a_waiting_room` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3168_minimum_number_of_chairs_in_a_waiting_room` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3168_minimum_number_of_chairs_in_a_waiting_room` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3168_minimum_number_of_chairs_in_a_waiting_room` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3168_minimum_number_of_chairs_in_a_waiting_room` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3168_minimum_number_of_chairs_in_a_waiting_room` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3168_minimum_number_of_chairs_in_a_waiting_room` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3168_minimum_number_of_chairs_in_a_waiting_room` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3168_minimum_number_of_chairs_in_a_waiting_room` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3168_minimum_number_of_chairs_in_a_waiting_room` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3168_minimum_number_of_chairs_in_a_waiting_room` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3168_minimum_number_of_chairs_in_a_waiting_room` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3168_minimum_number_of_chairs_in_a_waiting_room` |

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
.\scripts\test.ps1 -Folder 3168_minimum_number_of_chairs_in_a_waiting_room -AllLanguages
```

```bash
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --all-languages
```

```zsh
./scripts/test.sh --folder 3168_minimum_number_of_chairs_in_a_waiting_room --all-languages
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
