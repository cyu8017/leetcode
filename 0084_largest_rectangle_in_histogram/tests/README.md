# Test harness for 0084_largest_rectangle_in_histogram

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language python
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language javascript
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language typescript
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language java
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language cpp
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language c
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language go
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language rust
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language kotlin
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language swift
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language ruby
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language csharp
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language scala
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language php
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm java java 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm c c 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm go go 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm rust rust 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm swift swift 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm scala scala 0084_largest_rectangle_in_histogram
docker compose -f docker/docker-compose.yml run --rm php php 0084_largest_rectangle_in_histogram
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0084_largest_rectangle_in_histogram` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0084_largest_rectangle_in_histogram` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0084_largest_rectangle_in_histogram` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0084_largest_rectangle_in_histogram` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0084_largest_rectangle_in_histogram` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0084_largest_rectangle_in_histogram` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0084_largest_rectangle_in_histogram` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0084_largest_rectangle_in_histogram` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0084_largest_rectangle_in_histogram` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0084_largest_rectangle_in_histogram` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0084_largest_rectangle_in_histogram` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0084_largest_rectangle_in_histogram` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0084_largest_rectangle_in_histogram` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0084_largest_rectangle_in_histogram` |

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
.\scripts\test.ps1 -Folder 0084_largest_rectangle_in_histogram -AllLanguages
```

```bash
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --all-languages
```

```zsh
./scripts/test.sh --folder 0084_largest_rectangle_in_histogram --all-languages
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
