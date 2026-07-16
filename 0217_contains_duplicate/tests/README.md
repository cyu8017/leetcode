# Test harness for 0217_contains_duplicate

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0217_contains_duplicate -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0217_contains_duplicate --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0217_contains_duplicate --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0217_contains_duplicate --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0217_contains_duplicate --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0217_contains_duplicate --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0217_contains_duplicate --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0217_contains_duplicate --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0217_contains_duplicate --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0217_contains_duplicate --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0217_contains_duplicate --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0217_contains_duplicate --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0217_contains_duplicate --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0217_contains_duplicate --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0217_contains_duplicate --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0217_contains_duplicate --language python
./scripts/test.sh --folder 0217_contains_duplicate --language javascript
./scripts/test.sh --folder 0217_contains_duplicate --language typescript
./scripts/test.sh --folder 0217_contains_duplicate --language java
./scripts/test.sh --folder 0217_contains_duplicate --language cpp
./scripts/test.sh --folder 0217_contains_duplicate --language c
./scripts/test.sh --folder 0217_contains_duplicate --language go
./scripts/test.sh --folder 0217_contains_duplicate --language rust
./scripts/test.sh --folder 0217_contains_duplicate --language kotlin
./scripts/test.sh --folder 0217_contains_duplicate --language swift
./scripts/test.sh --folder 0217_contains_duplicate --language ruby
./scripts/test.sh --folder 0217_contains_duplicate --language csharp
./scripts/test.sh --folder 0217_contains_duplicate --language scala
./scripts/test.sh --folder 0217_contains_duplicate --language php
./scripts/test.sh --folder 0217_contains_duplicate --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0217_contains_duplicate --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0217_contains_duplicate --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0217_contains_duplicate --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0217_contains_duplicate --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0217_contains_duplicate --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0217_contains_duplicate --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0217_contains_duplicate --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0217_contains_duplicate --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0217_contains_duplicate --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0217_contains_duplicate --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0217_contains_duplicate --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0217_contains_duplicate --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0217_contains_duplicate --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0217_contains_duplicate --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm java java 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm c c 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm go go 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm rust rust 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm swift swift 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm scala scala 0217_contains_duplicate
docker compose -f docker/docker-compose.yml run --rm php php 0217_contains_duplicate
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0217_contains_duplicate` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0217_contains_duplicate` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0217_contains_duplicate` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0217_contains_duplicate` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0217_contains_duplicate` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0217_contains_duplicate` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0217_contains_duplicate` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0217_contains_duplicate` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0217_contains_duplicate` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0217_contains_duplicate` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0217_contains_duplicate` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0217_contains_duplicate` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0217_contains_duplicate` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0217_contains_duplicate` |

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
.\scripts\test.ps1 -Folder 0217_contains_duplicate -AllLanguages
```

```bash
./scripts/test.sh --folder 0217_contains_duplicate --all-languages
```

```zsh
./scripts/test.sh --folder 0217_contains_duplicate --all-languages
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
