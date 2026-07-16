# Test harness for 2681_power_of_heroes

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2681_power_of_heroes -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2681_power_of_heroes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2681_power_of_heroes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2681_power_of_heroes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2681_power_of_heroes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2681_power_of_heroes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2681_power_of_heroes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2681_power_of_heroes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2681_power_of_heroes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2681_power_of_heroes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2681_power_of_heroes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2681_power_of_heroes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2681_power_of_heroes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2681_power_of_heroes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2681_power_of_heroes --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2681_power_of_heroes --language python
./scripts/test.sh --folder 2681_power_of_heroes --language javascript
./scripts/test.sh --folder 2681_power_of_heroes --language typescript
./scripts/test.sh --folder 2681_power_of_heroes --language java
./scripts/test.sh --folder 2681_power_of_heroes --language cpp
./scripts/test.sh --folder 2681_power_of_heroes --language c
./scripts/test.sh --folder 2681_power_of_heroes --language go
./scripts/test.sh --folder 2681_power_of_heroes --language rust
./scripts/test.sh --folder 2681_power_of_heroes --language kotlin
./scripts/test.sh --folder 2681_power_of_heroes --language swift
./scripts/test.sh --folder 2681_power_of_heroes --language ruby
./scripts/test.sh --folder 2681_power_of_heroes --language csharp
./scripts/test.sh --folder 2681_power_of_heroes --language scala
./scripts/test.sh --folder 2681_power_of_heroes --language php
./scripts/test.sh --folder 2681_power_of_heroes --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2681_power_of_heroes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2681_power_of_heroes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2681_power_of_heroes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2681_power_of_heroes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2681_power_of_heroes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2681_power_of_heroes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2681_power_of_heroes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2681_power_of_heroes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2681_power_of_heroes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2681_power_of_heroes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2681_power_of_heroes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2681_power_of_heroes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2681_power_of_heroes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2681_power_of_heroes --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm java java 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm c c 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm go go 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm rust rust 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm swift swift 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm scala scala 2681_power_of_heroes
docker compose -f docker/docker-compose.yml run --rm php php 2681_power_of_heroes
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2681_power_of_heroes` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2681_power_of_heroes` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2681_power_of_heroes` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2681_power_of_heroes` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2681_power_of_heroes` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2681_power_of_heroes` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2681_power_of_heroes` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2681_power_of_heroes` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2681_power_of_heroes` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2681_power_of_heroes` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2681_power_of_heroes` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2681_power_of_heroes` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2681_power_of_heroes` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2681_power_of_heroes` |

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
.\scripts\test.ps1 -Folder 2681_power_of_heroes -AllLanguages
```

```bash
./scripts/test.sh --folder 2681_power_of_heroes --all-languages
```

```zsh
./scripts/test.sh --folder 2681_power_of_heroes --all-languages
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
