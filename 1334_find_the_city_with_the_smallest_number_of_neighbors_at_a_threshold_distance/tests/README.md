# Test harness for 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language python
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language javascript
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language typescript
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language java
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language cpp
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language c
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language go
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language rust
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language kotlin
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language swift
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language ruby
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language csharp
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language scala
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language php
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm java java 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm c c 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm go go 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm rust rust 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm swift swift 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm scala scala 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
docker compose -f docker/docker-compose.yml run --rm php php 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance` |

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
.\scripts\test.ps1 -Folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance -AllLanguages
```

```bash
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --all-languages
```

```zsh
./scripts/test.sh --folder 1334_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance --all-languages
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
