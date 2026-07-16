# Test harness for 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language python
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language javascript
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language typescript
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language java
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language cpp
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language c
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language go
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language rust
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language kotlin
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language swift
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language ruby
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language csharp
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language scala
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language php
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm java java 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm c c 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm go go 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm rust rust 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm swift swift 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm scala scala 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
docker compose -f docker/docker-compose.yml run --rm php php 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible` |

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
.\scripts\test.ps1 -Folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible -AllLanguages
```

```bash
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --all-languages
```

```zsh
./scripts/test.sh --folder 1866_number_of_ways_to_rearrange_sticks_with_k_sticks_visible --all-languages
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
