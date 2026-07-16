# Test harness for 2362_generate_the_invoice

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2362_generate_the_invoice -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2362_generate_the_invoice --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2362_generate_the_invoice --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2362_generate_the_invoice --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2362_generate_the_invoice --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2362_generate_the_invoice --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2362_generate_the_invoice --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2362_generate_the_invoice --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2362_generate_the_invoice --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2362_generate_the_invoice --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2362_generate_the_invoice --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2362_generate_the_invoice --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2362_generate_the_invoice --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2362_generate_the_invoice --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2362_generate_the_invoice --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2362_generate_the_invoice --language python
./scripts/test.sh --folder 2362_generate_the_invoice --language javascript
./scripts/test.sh --folder 2362_generate_the_invoice --language typescript
./scripts/test.sh --folder 2362_generate_the_invoice --language java
./scripts/test.sh --folder 2362_generate_the_invoice --language cpp
./scripts/test.sh --folder 2362_generate_the_invoice --language c
./scripts/test.sh --folder 2362_generate_the_invoice --language go
./scripts/test.sh --folder 2362_generate_the_invoice --language rust
./scripts/test.sh --folder 2362_generate_the_invoice --language kotlin
./scripts/test.sh --folder 2362_generate_the_invoice --language swift
./scripts/test.sh --folder 2362_generate_the_invoice --language ruby
./scripts/test.sh --folder 2362_generate_the_invoice --language csharp
./scripts/test.sh --folder 2362_generate_the_invoice --language scala
./scripts/test.sh --folder 2362_generate_the_invoice --language php
./scripts/test.sh --folder 2362_generate_the_invoice --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2362_generate_the_invoice --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2362_generate_the_invoice --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2362_generate_the_invoice --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2362_generate_the_invoice --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2362_generate_the_invoice --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2362_generate_the_invoice --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2362_generate_the_invoice --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2362_generate_the_invoice --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2362_generate_the_invoice --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2362_generate_the_invoice --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2362_generate_the_invoice --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2362_generate_the_invoice --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2362_generate_the_invoice --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2362_generate_the_invoice --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm java java 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm c c 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm go go 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm rust rust 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm swift swift 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm scala scala 2362_generate_the_invoice
docker compose -f docker/docker-compose.yml run --rm php php 2362_generate_the_invoice
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2362_generate_the_invoice` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2362_generate_the_invoice` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2362_generate_the_invoice` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2362_generate_the_invoice` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2362_generate_the_invoice` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2362_generate_the_invoice` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2362_generate_the_invoice` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2362_generate_the_invoice` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2362_generate_the_invoice` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2362_generate_the_invoice` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2362_generate_the_invoice` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2362_generate_the_invoice` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2362_generate_the_invoice` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2362_generate_the_invoice` |

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
.\scripts\test.ps1 -Folder 2362_generate_the_invoice -AllLanguages
```

```bash
./scripts/test.sh --folder 2362_generate_the_invoice --all-languages
```

```zsh
./scripts/test.sh --folder 2362_generate_the_invoice --all-languages
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
