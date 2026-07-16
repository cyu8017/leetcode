# Test harness for 2884_modify_columns

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2884_modify_columns -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2884_modify_columns --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2884_modify_columns --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2884_modify_columns --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2884_modify_columns --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2884_modify_columns --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2884_modify_columns --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2884_modify_columns --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2884_modify_columns --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2884_modify_columns --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2884_modify_columns --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2884_modify_columns --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2884_modify_columns --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2884_modify_columns --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2884_modify_columns --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2884_modify_columns --language python
./scripts/test.sh --folder 2884_modify_columns --language javascript
./scripts/test.sh --folder 2884_modify_columns --language typescript
./scripts/test.sh --folder 2884_modify_columns --language java
./scripts/test.sh --folder 2884_modify_columns --language cpp
./scripts/test.sh --folder 2884_modify_columns --language c
./scripts/test.sh --folder 2884_modify_columns --language go
./scripts/test.sh --folder 2884_modify_columns --language rust
./scripts/test.sh --folder 2884_modify_columns --language kotlin
./scripts/test.sh --folder 2884_modify_columns --language swift
./scripts/test.sh --folder 2884_modify_columns --language ruby
./scripts/test.sh --folder 2884_modify_columns --language csharp
./scripts/test.sh --folder 2884_modify_columns --language scala
./scripts/test.sh --folder 2884_modify_columns --language php
./scripts/test.sh --folder 2884_modify_columns --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2884_modify_columns --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2884_modify_columns --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2884_modify_columns --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2884_modify_columns --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2884_modify_columns --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2884_modify_columns --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2884_modify_columns --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2884_modify_columns --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2884_modify_columns --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2884_modify_columns --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2884_modify_columns --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2884_modify_columns --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2884_modify_columns --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2884_modify_columns --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm java java 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm c c 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm go go 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm rust rust 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm swift swift 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm scala scala 2884_modify_columns
docker compose -f docker/docker-compose.yml run --rm php php 2884_modify_columns
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2884_modify_columns` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2884_modify_columns` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2884_modify_columns` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2884_modify_columns` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2884_modify_columns` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2884_modify_columns` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2884_modify_columns` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2884_modify_columns` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2884_modify_columns` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2884_modify_columns` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2884_modify_columns` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2884_modify_columns` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2884_modify_columns` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2884_modify_columns` |

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
.\scripts\test.ps1 -Folder 2884_modify_columns -AllLanguages
```

```bash
./scripts/test.sh --folder 2884_modify_columns --all-languages
```

```zsh
./scripts/test.sh --folder 2884_modify_columns --all-languages
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
