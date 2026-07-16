# Test harness for 1789_primary_department_for_each_employee

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language python
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language javascript
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language typescript
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language java
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language cpp
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language c
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language go
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language rust
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language kotlin
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language swift
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language ruby
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language csharp
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language scala
./scripts/test.sh --folder 1789_primary_department_for_each_employee --language php
./scripts/test.sh --folder 1789_primary_department_for_each_employee --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1789_primary_department_for_each_employee --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm java java 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm c c 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm go go 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm rust rust 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm swift swift 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm scala scala 1789_primary_department_for_each_employee
docker compose -f docker/docker-compose.yml run --rm php php 1789_primary_department_for_each_employee
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1789_primary_department_for_each_employee` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1789_primary_department_for_each_employee` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1789_primary_department_for_each_employee` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1789_primary_department_for_each_employee` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1789_primary_department_for_each_employee` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1789_primary_department_for_each_employee` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1789_primary_department_for_each_employee` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1789_primary_department_for_each_employee` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1789_primary_department_for_each_employee` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1789_primary_department_for_each_employee` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1789_primary_department_for_each_employee` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1789_primary_department_for_each_employee` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1789_primary_department_for_each_employee` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1789_primary_department_for_each_employee` |

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
.\scripts\test.ps1 -Folder 1789_primary_department_for_each_employee -AllLanguages
```

```bash
./scripts/test.sh --folder 1789_primary_department_for_each_employee --all-languages
```

```zsh
./scripts/test.sh --folder 1789_primary_department_for_each_employee --all-languages
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
