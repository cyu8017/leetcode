# Test harness for 1498_number_of_subsequences_that_satisfy_the_given_sum_condition

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language python
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language javascript
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language typescript
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language java
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language cpp
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language c
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language go
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language rust
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language kotlin
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language swift
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language ruby
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language csharp
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language scala
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language php
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm java java 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm c c 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm go go 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm rust rust 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm swift swift 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm scala scala 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
docker compose -f docker/docker-compose.yml run --rm php php 1498_number_of_subsequences_that_satisfy_the_given_sum_condition
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1498_number_of_subsequences_that_satisfy_the_given_sum_condition` |

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
.\scripts\test.ps1 -Folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition -AllLanguages
```

```bash
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --all-languages
```

```zsh
./scripts/test.sh --folder 1498_number_of_subsequences_that_satisfy_the_given_sum_condition --all-languages
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
