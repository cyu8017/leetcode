# Test harness for 3154_find_number_of_ways_to_reach_the_k_th_stair

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language python
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language javascript
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language typescript
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language java
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language cpp
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language c
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language go
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language rust
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language kotlin
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language swift
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language ruby
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language csharp
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language scala
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language php
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm java java 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm c c 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm go go 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm rust rust 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm swift swift 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm scala scala 3154_find_number_of_ways_to_reach_the_k_th_stair
docker compose -f docker/docker-compose.yml run --rm php php 3154_find_number_of_ways_to_reach_the_k_th_stair
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3154_find_number_of_ways_to_reach_the_k_th_stair` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3154_find_number_of_ways_to_reach_the_k_th_stair` |

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
.\scripts\test.ps1 -Folder 3154_find_number_of_ways_to_reach_the_k_th_stair -AllLanguages
```

```bash
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --all-languages
```

```zsh
./scripts/test.sh --folder 3154_find_number_of_ways_to_reach_the_k_th_stair --all-languages
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
