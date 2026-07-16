# Test harness for 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language python
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language javascript
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language typescript
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language java
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language cpp
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language c
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language go
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language rust
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language kotlin
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language swift
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language ruby
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language csharp
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language scala
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language php
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm java java 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm c c 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm go go 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm rust rust 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm swift swift 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm scala scala 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
docker compose -f docker/docker-compose.yml run --rm php php 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold` |

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
.\scripts\test.ps1 -Folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold -AllLanguages
```

```bash
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --all-languages
```

```zsh
./scripts/test.sh --folder 1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold --all-languages
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
