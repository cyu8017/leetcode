# Test harness for 3173_bitwise_or_of_adjacent_elements

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language python
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language javascript
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language typescript
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language java
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language cpp
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language c
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language go
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language rust
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language kotlin
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language swift
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language ruby
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language csharp
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language scala
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language php
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm java java 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm c c 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm go go 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm rust rust 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm swift swift 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm scala scala 3173_bitwise_or_of_adjacent_elements
docker compose -f docker/docker-compose.yml run --rm php php 3173_bitwise_or_of_adjacent_elements
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3173_bitwise_or_of_adjacent_elements` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3173_bitwise_or_of_adjacent_elements` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3173_bitwise_or_of_adjacent_elements` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3173_bitwise_or_of_adjacent_elements` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3173_bitwise_or_of_adjacent_elements` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3173_bitwise_or_of_adjacent_elements` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3173_bitwise_or_of_adjacent_elements` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3173_bitwise_or_of_adjacent_elements` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3173_bitwise_or_of_adjacent_elements` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3173_bitwise_or_of_adjacent_elements` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3173_bitwise_or_of_adjacent_elements` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3173_bitwise_or_of_adjacent_elements` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3173_bitwise_or_of_adjacent_elements` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3173_bitwise_or_of_adjacent_elements` |

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
.\scripts\test.ps1 -Folder 3173_bitwise_or_of_adjacent_elements -AllLanguages
```

```bash
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --all-languages
```

```zsh
./scripts/test.sh --folder 3173_bitwise_or_of_adjacent_elements --all-languages
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
