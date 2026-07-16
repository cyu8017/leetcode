# Test harness for 2680_maximum_or

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2680_maximum_or -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2680_maximum_or --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2680_maximum_or --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2680_maximum_or --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2680_maximum_or --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2680_maximum_or --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2680_maximum_or --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2680_maximum_or --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2680_maximum_or --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2680_maximum_or --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2680_maximum_or --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2680_maximum_or --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2680_maximum_or --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2680_maximum_or --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2680_maximum_or --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2680_maximum_or --language python
./scripts/test.sh --folder 2680_maximum_or --language javascript
./scripts/test.sh --folder 2680_maximum_or --language typescript
./scripts/test.sh --folder 2680_maximum_or --language java
./scripts/test.sh --folder 2680_maximum_or --language cpp
./scripts/test.sh --folder 2680_maximum_or --language c
./scripts/test.sh --folder 2680_maximum_or --language go
./scripts/test.sh --folder 2680_maximum_or --language rust
./scripts/test.sh --folder 2680_maximum_or --language kotlin
./scripts/test.sh --folder 2680_maximum_or --language swift
./scripts/test.sh --folder 2680_maximum_or --language ruby
./scripts/test.sh --folder 2680_maximum_or --language csharp
./scripts/test.sh --folder 2680_maximum_or --language scala
./scripts/test.sh --folder 2680_maximum_or --language php
./scripts/test.sh --folder 2680_maximum_or --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2680_maximum_or --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2680_maximum_or --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2680_maximum_or --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2680_maximum_or --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2680_maximum_or --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2680_maximum_or --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2680_maximum_or --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2680_maximum_or --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2680_maximum_or --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2680_maximum_or --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2680_maximum_or --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2680_maximum_or --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2680_maximum_or --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2680_maximum_or --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm java java 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm c c 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm go go 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm rust rust 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm swift swift 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm scala scala 2680_maximum_or
docker compose -f docker/docker-compose.yml run --rm php php 2680_maximum_or
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2680_maximum_or` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2680_maximum_or` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2680_maximum_or` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2680_maximum_or` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2680_maximum_or` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2680_maximum_or` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2680_maximum_or` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2680_maximum_or` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2680_maximum_or` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2680_maximum_or` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2680_maximum_or` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2680_maximum_or` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2680_maximum_or` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2680_maximum_or` |

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
.\scripts\test.ps1 -Folder 2680_maximum_or -AllLanguages
```

```bash
./scripts/test.sh --folder 2680_maximum_or --all-languages
```

```zsh
./scripts/test.sh --folder 2680_maximum_or --all-languages
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
