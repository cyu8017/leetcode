# Test harness for 1453_maximum_number_of_darts_inside_of_a_circular_dartboard

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language python
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language javascript
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language typescript
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language java
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language cpp
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language c
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language go
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language rust
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language kotlin
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language swift
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language ruby
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language csharp
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language scala
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language php
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm java java 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm c c 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm go go 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm rust rust 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm swift swift 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm scala scala 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
docker compose -f docker/docker-compose.yml run --rm php php 1453_maximum_number_of_darts_inside_of_a_circular_dartboard
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1453_maximum_number_of_darts_inside_of_a_circular_dartboard` |

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
.\scripts\test.ps1 -Folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard -AllLanguages
```

```bash
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --all-languages
```

```zsh
./scripts/test.sh --folder 1453_maximum_number_of_darts_inside_of_a_circular_dartboard --all-languages
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
