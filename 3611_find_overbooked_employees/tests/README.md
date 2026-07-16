# Test harness for 3611_find_overbooked_employees

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3611_find_overbooked_employees --language python
./scripts/test.sh --folder 3611_find_overbooked_employees --language javascript
./scripts/test.sh --folder 3611_find_overbooked_employees --language typescript
./scripts/test.sh --folder 3611_find_overbooked_employees --language java
./scripts/test.sh --folder 3611_find_overbooked_employees --language cpp
./scripts/test.sh --folder 3611_find_overbooked_employees --language c
./scripts/test.sh --folder 3611_find_overbooked_employees --language go
./scripts/test.sh --folder 3611_find_overbooked_employees --language rust
./scripts/test.sh --folder 3611_find_overbooked_employees --language kotlin
./scripts/test.sh --folder 3611_find_overbooked_employees --language swift
./scripts/test.sh --folder 3611_find_overbooked_employees --language ruby
./scripts/test.sh --folder 3611_find_overbooked_employees --language csharp
./scripts/test.sh --folder 3611_find_overbooked_employees --language scala
./scripts/test.sh --folder 3611_find_overbooked_employees --language php
./scripts/test.sh --folder 3611_find_overbooked_employees --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3611_find_overbooked_employees --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm java java 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm c c 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm go go 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm rust rust 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm swift swift 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm scala scala 3611_find_overbooked_employees
docker compose -f docker/docker-compose.yml run --rm php php 3611_find_overbooked_employees
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3611_find_overbooked_employees` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3611_find_overbooked_employees` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3611_find_overbooked_employees` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3611_find_overbooked_employees` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3611_find_overbooked_employees` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3611_find_overbooked_employees` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3611_find_overbooked_employees` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3611_find_overbooked_employees` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3611_find_overbooked_employees` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3611_find_overbooked_employees` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3611_find_overbooked_employees` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3611_find_overbooked_employees` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3611_find_overbooked_employees` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3611_find_overbooked_employees` |

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
.\scripts\test.ps1 -Folder 3611_find_overbooked_employees -AllLanguages
```

```bash
./scripts/test.sh --folder 3611_find_overbooked_employees --all-languages
```

```zsh
./scripts/test.sh --folder 3611_find_overbooked_employees --all-languages
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
