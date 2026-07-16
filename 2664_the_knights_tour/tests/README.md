# Test harness for 2664_the_knights_tour

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2664_the_knights_tour -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2664_the_knights_tour --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2664_the_knights_tour --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2664_the_knights_tour --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2664_the_knights_tour --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2664_the_knights_tour --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2664_the_knights_tour --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2664_the_knights_tour --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2664_the_knights_tour --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2664_the_knights_tour --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2664_the_knights_tour --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2664_the_knights_tour --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2664_the_knights_tour --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2664_the_knights_tour --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2664_the_knights_tour --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2664_the_knights_tour --language python
./scripts/test.sh --folder 2664_the_knights_tour --language javascript
./scripts/test.sh --folder 2664_the_knights_tour --language typescript
./scripts/test.sh --folder 2664_the_knights_tour --language java
./scripts/test.sh --folder 2664_the_knights_tour --language cpp
./scripts/test.sh --folder 2664_the_knights_tour --language c
./scripts/test.sh --folder 2664_the_knights_tour --language go
./scripts/test.sh --folder 2664_the_knights_tour --language rust
./scripts/test.sh --folder 2664_the_knights_tour --language kotlin
./scripts/test.sh --folder 2664_the_knights_tour --language swift
./scripts/test.sh --folder 2664_the_knights_tour --language ruby
./scripts/test.sh --folder 2664_the_knights_tour --language csharp
./scripts/test.sh --folder 2664_the_knights_tour --language scala
./scripts/test.sh --folder 2664_the_knights_tour --language php
./scripts/test.sh --folder 2664_the_knights_tour --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2664_the_knights_tour --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2664_the_knights_tour --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2664_the_knights_tour --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2664_the_knights_tour --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2664_the_knights_tour --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2664_the_knights_tour --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2664_the_knights_tour --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2664_the_knights_tour --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2664_the_knights_tour --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2664_the_knights_tour --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2664_the_knights_tour --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2664_the_knights_tour --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2664_the_knights_tour --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2664_the_knights_tour --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm java java 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm c c 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm go go 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm rust rust 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm swift swift 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm scala scala 2664_the_knights_tour
docker compose -f docker/docker-compose.yml run --rm php php 2664_the_knights_tour
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2664_the_knights_tour` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2664_the_knights_tour` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2664_the_knights_tour` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2664_the_knights_tour` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2664_the_knights_tour` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2664_the_knights_tour` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2664_the_knights_tour` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2664_the_knights_tour` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2664_the_knights_tour` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2664_the_knights_tour` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2664_the_knights_tour` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2664_the_knights_tour` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2664_the_knights_tour` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2664_the_knights_tour` |

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
.\scripts\test.ps1 -Folder 2664_the_knights_tour -AllLanguages
```

```bash
./scripts/test.sh --folder 2664_the_knights_tour --all-languages
```

```zsh
./scripts/test.sh --folder 2664_the_knights_tour --all-languages
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
