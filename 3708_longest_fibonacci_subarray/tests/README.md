# Test harness for 3708_longest_fibonacci_subarray

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language python
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language javascript
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language typescript
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language java
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language cpp
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language c
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language go
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language rust
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language kotlin
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language swift
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language ruby
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language csharp
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language scala
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language php
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3708_longest_fibonacci_subarray --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm java java 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm c c 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm go go 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm rust rust 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm swift swift 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm scala scala 3708_longest_fibonacci_subarray
docker compose -f docker/docker-compose.yml run --rm php php 3708_longest_fibonacci_subarray
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3708_longest_fibonacci_subarray` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3708_longest_fibonacci_subarray` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3708_longest_fibonacci_subarray` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3708_longest_fibonacci_subarray` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3708_longest_fibonacci_subarray` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3708_longest_fibonacci_subarray` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3708_longest_fibonacci_subarray` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3708_longest_fibonacci_subarray` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3708_longest_fibonacci_subarray` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3708_longest_fibonacci_subarray` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3708_longest_fibonacci_subarray` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3708_longest_fibonacci_subarray` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3708_longest_fibonacci_subarray` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3708_longest_fibonacci_subarray` |

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
.\scripts\test.ps1 -Folder 3708_longest_fibonacci_subarray -AllLanguages
```

```bash
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --all-languages
```

```zsh
./scripts/test.sh --folder 3708_longest_fibonacci_subarray --all-languages
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
