# Test harness for 0342_power_of_four

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0342_power_of_four -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0342_power_of_four --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0342_power_of_four --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0342_power_of_four --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0342_power_of_four --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0342_power_of_four --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0342_power_of_four --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0342_power_of_four --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0342_power_of_four --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0342_power_of_four --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0342_power_of_four --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0342_power_of_four --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0342_power_of_four --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0342_power_of_four --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0342_power_of_four --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0342_power_of_four --language python
./scripts/test.sh --folder 0342_power_of_four --language javascript
./scripts/test.sh --folder 0342_power_of_four --language typescript
./scripts/test.sh --folder 0342_power_of_four --language java
./scripts/test.sh --folder 0342_power_of_four --language cpp
./scripts/test.sh --folder 0342_power_of_four --language c
./scripts/test.sh --folder 0342_power_of_four --language go
./scripts/test.sh --folder 0342_power_of_four --language rust
./scripts/test.sh --folder 0342_power_of_four --language kotlin
./scripts/test.sh --folder 0342_power_of_four --language swift
./scripts/test.sh --folder 0342_power_of_four --language ruby
./scripts/test.sh --folder 0342_power_of_four --language csharp
./scripts/test.sh --folder 0342_power_of_four --language scala
./scripts/test.sh --folder 0342_power_of_four --language php
./scripts/test.sh --folder 0342_power_of_four --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0342_power_of_four --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0342_power_of_four --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0342_power_of_four --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0342_power_of_four --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0342_power_of_four --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0342_power_of_four --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0342_power_of_four --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0342_power_of_four --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0342_power_of_four --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0342_power_of_four --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0342_power_of_four --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0342_power_of_four --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0342_power_of_four --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0342_power_of_four --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm java java 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm c c 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm go go 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm rust rust 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm swift swift 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm scala scala 0342_power_of_four
docker compose -f docker/docker-compose.yml run --rm php php 0342_power_of_four
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0342_power_of_four` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0342_power_of_four` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0342_power_of_four` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0342_power_of_four` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0342_power_of_four` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0342_power_of_four` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0342_power_of_four` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0342_power_of_four` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0342_power_of_four` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0342_power_of_four` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0342_power_of_four` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0342_power_of_four` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0342_power_of_four` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0342_power_of_four` |

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
.\scripts\test.ps1 -Folder 0342_power_of_four -AllLanguages
```

```bash
./scripts/test.sh --folder 0342_power_of_four --all-languages
```

```zsh
./scripts/test.sh --folder 0342_power_of_four --all-languages
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
