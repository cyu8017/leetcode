# Test harness for 2241_design_an_atm_machine

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2241_design_an_atm_machine --language python
./scripts/test.sh --folder 2241_design_an_atm_machine --language javascript
./scripts/test.sh --folder 2241_design_an_atm_machine --language typescript
./scripts/test.sh --folder 2241_design_an_atm_machine --language java
./scripts/test.sh --folder 2241_design_an_atm_machine --language cpp
./scripts/test.sh --folder 2241_design_an_atm_machine --language c
./scripts/test.sh --folder 2241_design_an_atm_machine --language go
./scripts/test.sh --folder 2241_design_an_atm_machine --language rust
./scripts/test.sh --folder 2241_design_an_atm_machine --language kotlin
./scripts/test.sh --folder 2241_design_an_atm_machine --language swift
./scripts/test.sh --folder 2241_design_an_atm_machine --language ruby
./scripts/test.sh --folder 2241_design_an_atm_machine --language csharp
./scripts/test.sh --folder 2241_design_an_atm_machine --language scala
./scripts/test.sh --folder 2241_design_an_atm_machine --language php
./scripts/test.sh --folder 2241_design_an_atm_machine --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2241_design_an_atm_machine --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm java java 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm c c 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm go go 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm rust rust 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm swift swift 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm scala scala 2241_design_an_atm_machine
docker compose -f docker/docker-compose.yml run --rm php php 2241_design_an_atm_machine
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2241_design_an_atm_machine` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2241_design_an_atm_machine` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2241_design_an_atm_machine` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2241_design_an_atm_machine` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2241_design_an_atm_machine` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2241_design_an_atm_machine` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2241_design_an_atm_machine` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2241_design_an_atm_machine` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2241_design_an_atm_machine` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2241_design_an_atm_machine` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2241_design_an_atm_machine` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2241_design_an_atm_machine` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2241_design_an_atm_machine` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2241_design_an_atm_machine` |

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
.\scripts\test.ps1 -Folder 2241_design_an_atm_machine -AllLanguages
```

```bash
./scripts/test.sh --folder 2241_design_an_atm_machine --all-languages
```

```zsh
./scripts/test.sh --folder 2241_design_an_atm_machine --all-languages
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
