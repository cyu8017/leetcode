# Test harness for 1568_minimum_number_of_days_to_disconnect_island

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language python
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language javascript
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language typescript
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language java
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language cpp
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language c
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language go
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language rust
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language kotlin
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language swift
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language ruby
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language csharp
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language scala
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language php
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm java java 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm c c 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm go go 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm rust rust 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm swift swift 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm scala scala 1568_minimum_number_of_days_to_disconnect_island
docker compose -f docker/docker-compose.yml run --rm php php 1568_minimum_number_of_days_to_disconnect_island
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1568_minimum_number_of_days_to_disconnect_island` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1568_minimum_number_of_days_to_disconnect_island` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1568_minimum_number_of_days_to_disconnect_island` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1568_minimum_number_of_days_to_disconnect_island` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1568_minimum_number_of_days_to_disconnect_island` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1568_minimum_number_of_days_to_disconnect_island` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1568_minimum_number_of_days_to_disconnect_island` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1568_minimum_number_of_days_to_disconnect_island` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1568_minimum_number_of_days_to_disconnect_island` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1568_minimum_number_of_days_to_disconnect_island` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1568_minimum_number_of_days_to_disconnect_island` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1568_minimum_number_of_days_to_disconnect_island` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1568_minimum_number_of_days_to_disconnect_island` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1568_minimum_number_of_days_to_disconnect_island` |

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
.\scripts\test.ps1 -Folder 1568_minimum_number_of_days_to_disconnect_island -AllLanguages
```

```bash
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --all-languages
```

```zsh
./scripts/test.sh --folder 1568_minimum_number_of_days_to_disconnect_island --all-languages
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
