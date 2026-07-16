# Test harness for 0016_3sum_closest

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0016_3sum_closest -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0016_3sum_closest --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0016_3sum_closest --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0016_3sum_closest --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0016_3sum_closest --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0016_3sum_closest --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0016_3sum_closest --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0016_3sum_closest --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0016_3sum_closest --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0016_3sum_closest --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0016_3sum_closest --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0016_3sum_closest --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0016_3sum_closest --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0016_3sum_closest --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0016_3sum_closest --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0016_3sum_closest --language python
./scripts/test.sh --folder 0016_3sum_closest --language javascript
./scripts/test.sh --folder 0016_3sum_closest --language typescript
./scripts/test.sh --folder 0016_3sum_closest --language java
./scripts/test.sh --folder 0016_3sum_closest --language cpp
./scripts/test.sh --folder 0016_3sum_closest --language c
./scripts/test.sh --folder 0016_3sum_closest --language go
./scripts/test.sh --folder 0016_3sum_closest --language rust
./scripts/test.sh --folder 0016_3sum_closest --language kotlin
./scripts/test.sh --folder 0016_3sum_closest --language swift
./scripts/test.sh --folder 0016_3sum_closest --language ruby
./scripts/test.sh --folder 0016_3sum_closest --language csharp
./scripts/test.sh --folder 0016_3sum_closest --language scala
./scripts/test.sh --folder 0016_3sum_closest --language php
./scripts/test.sh --folder 0016_3sum_closest --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0016_3sum_closest --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0016_3sum_closest --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0016_3sum_closest --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0016_3sum_closest --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0016_3sum_closest --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0016_3sum_closest --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0016_3sum_closest --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0016_3sum_closest --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0016_3sum_closest --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0016_3sum_closest --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0016_3sum_closest --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0016_3sum_closest --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0016_3sum_closest --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0016_3sum_closest --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm java java 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm c c 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm go go 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm rust rust 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm swift swift 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm scala scala 0016_3sum_closest
docker compose -f docker/docker-compose.yml run --rm php php 0016_3sum_closest
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0016_3sum_closest` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0016_3sum_closest` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0016_3sum_closest` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0016_3sum_closest` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0016_3sum_closest` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0016_3sum_closest` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0016_3sum_closest` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0016_3sum_closest` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0016_3sum_closest` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0016_3sum_closest` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0016_3sum_closest` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0016_3sum_closest` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0016_3sum_closest` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0016_3sum_closest` |

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
.\scripts\test.ps1 -Folder 0016_3sum_closest -AllLanguages
```

```bash
./scripts/test.sh --folder 0016_3sum_closest --all-languages
```

```zsh
./scripts/test.sh --folder 0016_3sum_closest --all-languages
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
