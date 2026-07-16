# Test harness for 2021_brightest_position_on_street

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2021_brightest_position_on_street --language python
./scripts/test.sh --folder 2021_brightest_position_on_street --language javascript
./scripts/test.sh --folder 2021_brightest_position_on_street --language typescript
./scripts/test.sh --folder 2021_brightest_position_on_street --language java
./scripts/test.sh --folder 2021_brightest_position_on_street --language cpp
./scripts/test.sh --folder 2021_brightest_position_on_street --language c
./scripts/test.sh --folder 2021_brightest_position_on_street --language go
./scripts/test.sh --folder 2021_brightest_position_on_street --language rust
./scripts/test.sh --folder 2021_brightest_position_on_street --language kotlin
./scripts/test.sh --folder 2021_brightest_position_on_street --language swift
./scripts/test.sh --folder 2021_brightest_position_on_street --language ruby
./scripts/test.sh --folder 2021_brightest_position_on_street --language csharp
./scripts/test.sh --folder 2021_brightest_position_on_street --language scala
./scripts/test.sh --folder 2021_brightest_position_on_street --language php
./scripts/test.sh --folder 2021_brightest_position_on_street --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2021_brightest_position_on_street --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm java java 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm c c 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm go go 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm rust rust 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm swift swift 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm scala scala 2021_brightest_position_on_street
docker compose -f docker/docker-compose.yml run --rm php php 2021_brightest_position_on_street
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2021_brightest_position_on_street` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2021_brightest_position_on_street` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2021_brightest_position_on_street` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2021_brightest_position_on_street` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2021_brightest_position_on_street` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2021_brightest_position_on_street` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2021_brightest_position_on_street` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2021_brightest_position_on_street` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2021_brightest_position_on_street` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2021_brightest_position_on_street` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2021_brightest_position_on_street` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2021_brightest_position_on_street` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2021_brightest_position_on_street` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2021_brightest_position_on_street` |

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
.\scripts\test.ps1 -Folder 2021_brightest_position_on_street -AllLanguages
```

```bash
./scripts/test.sh --folder 2021_brightest_position_on_street --all-languages
```

```zsh
./scripts/test.sh --folder 2021_brightest_position_on_street --all-languages
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
