# Test harness for 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language python
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language javascript
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language typescript
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language java
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language cpp
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language c
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language go
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language rust
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language kotlin
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language swift
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language ruby
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language csharp
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language scala
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language php
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm java java 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm c c 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm go go 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm rust rust 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm swift swift 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm scala scala 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
docker compose -f docker/docker-compose.yml run --rm php php 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps` |

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
.\scripts\test.ps1 -Folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps -AllLanguages
```

```bash
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --all-languages
```

```zsh
./scripts/test.sh --folder 2400_number_of_ways_to_reach_a_position_after_exactly_k_steps --all-languages
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
