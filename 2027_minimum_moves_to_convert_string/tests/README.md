# Test harness for 2027_minimum_moves_to_convert_string

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language python
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language javascript
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language typescript
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language java
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language cpp
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language c
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language go
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language rust
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language kotlin
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language swift
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language ruby
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language csharp
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language scala
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language php
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm java java 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm c c 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm go go 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm rust rust 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm swift swift 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm scala scala 2027_minimum_moves_to_convert_string
docker compose -f docker/docker-compose.yml run --rm php php 2027_minimum_moves_to_convert_string
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2027_minimum_moves_to_convert_string` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2027_minimum_moves_to_convert_string` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2027_minimum_moves_to_convert_string` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2027_minimum_moves_to_convert_string` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2027_minimum_moves_to_convert_string` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2027_minimum_moves_to_convert_string` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2027_minimum_moves_to_convert_string` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2027_minimum_moves_to_convert_string` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2027_minimum_moves_to_convert_string` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2027_minimum_moves_to_convert_string` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2027_minimum_moves_to_convert_string` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2027_minimum_moves_to_convert_string` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2027_minimum_moves_to_convert_string` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2027_minimum_moves_to_convert_string` |

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
.\scripts\test.ps1 -Folder 2027_minimum_moves_to_convert_string -AllLanguages
```

```bash
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --all-languages
```

```zsh
./scripts/test.sh --folder 2027_minimum_moves_to_convert_string --all-languages
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
