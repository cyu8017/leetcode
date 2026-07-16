# Test harness for 0204_count_primes

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0204_count_primes -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0204_count_primes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0204_count_primes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0204_count_primes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0204_count_primes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0204_count_primes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0204_count_primes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0204_count_primes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0204_count_primes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0204_count_primes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0204_count_primes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0204_count_primes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0204_count_primes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0204_count_primes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0204_count_primes --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0204_count_primes --language python
./scripts/test.sh --folder 0204_count_primes --language javascript
./scripts/test.sh --folder 0204_count_primes --language typescript
./scripts/test.sh --folder 0204_count_primes --language java
./scripts/test.sh --folder 0204_count_primes --language cpp
./scripts/test.sh --folder 0204_count_primes --language c
./scripts/test.sh --folder 0204_count_primes --language go
./scripts/test.sh --folder 0204_count_primes --language rust
./scripts/test.sh --folder 0204_count_primes --language kotlin
./scripts/test.sh --folder 0204_count_primes --language swift
./scripts/test.sh --folder 0204_count_primes --language ruby
./scripts/test.sh --folder 0204_count_primes --language csharp
./scripts/test.sh --folder 0204_count_primes --language scala
./scripts/test.sh --folder 0204_count_primes --language php
./scripts/test.sh --folder 0204_count_primes --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0204_count_primes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0204_count_primes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0204_count_primes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0204_count_primes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0204_count_primes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0204_count_primes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0204_count_primes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0204_count_primes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0204_count_primes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0204_count_primes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0204_count_primes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0204_count_primes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0204_count_primes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0204_count_primes --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm java java 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm c c 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm go go 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm rust rust 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm swift swift 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm scala scala 0204_count_primes
docker compose -f docker/docker-compose.yml run --rm php php 0204_count_primes
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0204_count_primes` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0204_count_primes` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0204_count_primes` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0204_count_primes` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0204_count_primes` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0204_count_primes` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0204_count_primes` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0204_count_primes` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0204_count_primes` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0204_count_primes` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0204_count_primes` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0204_count_primes` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0204_count_primes` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0204_count_primes` |

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
.\scripts\test.ps1 -Folder 0204_count_primes -AllLanguages
```

```bash
./scripts/test.sh --folder 0204_count_primes --all-languages
```

```zsh
./scripts/test.sh --folder 0204_count_primes --all-languages
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
