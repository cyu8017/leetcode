# Test harness for 2507_smallest_value_after_replacing_with_sum_of_prime_factors

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language python
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language javascript
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language typescript
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language java
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language cpp
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language c
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language go
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language rust
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language kotlin
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language swift
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language ruby
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language csharp
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language scala
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language php
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm java java 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm c c 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm go go 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm rust rust 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm swift swift 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm scala scala 2507_smallest_value_after_replacing_with_sum_of_prime_factors
docker compose -f docker/docker-compose.yml run --rm php php 2507_smallest_value_after_replacing_with_sum_of_prime_factors
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2507_smallest_value_after_replacing_with_sum_of_prime_factors` |

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
.\scripts\test.ps1 -Folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors -AllLanguages
```

```bash
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --all-languages
```

```zsh
./scripts/test.sh --folder 2507_smallest_value_after_replacing_with_sum_of_prime_factors --all-languages
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
