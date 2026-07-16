# Test harness for 3057_employees_project_allocation

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3057_employees_project_allocation -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3057_employees_project_allocation --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3057_employees_project_allocation --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3057_employees_project_allocation --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3057_employees_project_allocation --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3057_employees_project_allocation --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3057_employees_project_allocation --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3057_employees_project_allocation --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3057_employees_project_allocation --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3057_employees_project_allocation --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3057_employees_project_allocation --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3057_employees_project_allocation --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3057_employees_project_allocation --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3057_employees_project_allocation --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3057_employees_project_allocation --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3057_employees_project_allocation --language python
./scripts/test.sh --folder 3057_employees_project_allocation --language javascript
./scripts/test.sh --folder 3057_employees_project_allocation --language typescript
./scripts/test.sh --folder 3057_employees_project_allocation --language java
./scripts/test.sh --folder 3057_employees_project_allocation --language cpp
./scripts/test.sh --folder 3057_employees_project_allocation --language c
./scripts/test.sh --folder 3057_employees_project_allocation --language go
./scripts/test.sh --folder 3057_employees_project_allocation --language rust
./scripts/test.sh --folder 3057_employees_project_allocation --language kotlin
./scripts/test.sh --folder 3057_employees_project_allocation --language swift
./scripts/test.sh --folder 3057_employees_project_allocation --language ruby
./scripts/test.sh --folder 3057_employees_project_allocation --language csharp
./scripts/test.sh --folder 3057_employees_project_allocation --language scala
./scripts/test.sh --folder 3057_employees_project_allocation --language php
./scripts/test.sh --folder 3057_employees_project_allocation --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3057_employees_project_allocation --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3057_employees_project_allocation --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3057_employees_project_allocation --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3057_employees_project_allocation --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3057_employees_project_allocation --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3057_employees_project_allocation --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3057_employees_project_allocation --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3057_employees_project_allocation --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3057_employees_project_allocation --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3057_employees_project_allocation --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3057_employees_project_allocation --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3057_employees_project_allocation --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3057_employees_project_allocation --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3057_employees_project_allocation --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm java java 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm c c 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm go go 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm rust rust 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm swift swift 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm scala scala 3057_employees_project_allocation
docker compose -f docker/docker-compose.yml run --rm php php 3057_employees_project_allocation
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3057_employees_project_allocation` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3057_employees_project_allocation` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3057_employees_project_allocation` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3057_employees_project_allocation` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3057_employees_project_allocation` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3057_employees_project_allocation` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3057_employees_project_allocation` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3057_employees_project_allocation` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3057_employees_project_allocation` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3057_employees_project_allocation` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3057_employees_project_allocation` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3057_employees_project_allocation` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3057_employees_project_allocation` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3057_employees_project_allocation` |

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
.\scripts\test.ps1 -Folder 3057_employees_project_allocation -AllLanguages
```

```bash
./scripts/test.sh --folder 3057_employees_project_allocation --all-languages
```

```zsh
./scripts/test.sh --folder 3057_employees_project_allocation --all-languages
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
