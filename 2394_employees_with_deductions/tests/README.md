# Test harness for 2394_employees_with_deductions

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2394_employees_with_deductions -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2394_employees_with_deductions --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2394_employees_with_deductions --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2394_employees_with_deductions --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2394_employees_with_deductions --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2394_employees_with_deductions --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2394_employees_with_deductions --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2394_employees_with_deductions --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2394_employees_with_deductions --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2394_employees_with_deductions --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2394_employees_with_deductions --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2394_employees_with_deductions --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2394_employees_with_deductions --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2394_employees_with_deductions --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2394_employees_with_deductions --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2394_employees_with_deductions --language python
./scripts/test.sh --folder 2394_employees_with_deductions --language javascript
./scripts/test.sh --folder 2394_employees_with_deductions --language typescript
./scripts/test.sh --folder 2394_employees_with_deductions --language java
./scripts/test.sh --folder 2394_employees_with_deductions --language cpp
./scripts/test.sh --folder 2394_employees_with_deductions --language c
./scripts/test.sh --folder 2394_employees_with_deductions --language go
./scripts/test.sh --folder 2394_employees_with_deductions --language rust
./scripts/test.sh --folder 2394_employees_with_deductions --language kotlin
./scripts/test.sh --folder 2394_employees_with_deductions --language swift
./scripts/test.sh --folder 2394_employees_with_deductions --language ruby
./scripts/test.sh --folder 2394_employees_with_deductions --language csharp
./scripts/test.sh --folder 2394_employees_with_deductions --language scala
./scripts/test.sh --folder 2394_employees_with_deductions --language php
./scripts/test.sh --folder 2394_employees_with_deductions --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2394_employees_with_deductions --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2394_employees_with_deductions --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2394_employees_with_deductions --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2394_employees_with_deductions --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2394_employees_with_deductions --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2394_employees_with_deductions --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2394_employees_with_deductions --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2394_employees_with_deductions --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2394_employees_with_deductions --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2394_employees_with_deductions --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2394_employees_with_deductions --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2394_employees_with_deductions --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2394_employees_with_deductions --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2394_employees_with_deductions --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm java java 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm c c 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm go go 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm rust rust 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm swift swift 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm scala scala 2394_employees_with_deductions
docker compose -f docker/docker-compose.yml run --rm php php 2394_employees_with_deductions
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2394_employees_with_deductions` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2394_employees_with_deductions` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2394_employees_with_deductions` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2394_employees_with_deductions` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2394_employees_with_deductions` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2394_employees_with_deductions` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2394_employees_with_deductions` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2394_employees_with_deductions` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2394_employees_with_deductions` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2394_employees_with_deductions` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2394_employees_with_deductions` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2394_employees_with_deductions` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2394_employees_with_deductions` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2394_employees_with_deductions` |

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
.\scripts\test.ps1 -Folder 2394_employees_with_deductions -AllLanguages
```

```bash
./scripts/test.sh --folder 2394_employees_with_deductions --all-languages
```

```zsh
./scripts/test.sh --folder 2394_employees_with_deductions --all-languages
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
