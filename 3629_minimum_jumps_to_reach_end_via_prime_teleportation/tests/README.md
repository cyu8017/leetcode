# Test harness for 3629_minimum_jumps_to_reach_end_via_prime_teleportation

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language python
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language javascript
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language typescript
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language java
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language cpp
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language c
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language go
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language rust
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language kotlin
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language swift
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language ruby
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language csharp
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language scala
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language php
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm java java 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm c c 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm go go 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm rust rust 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm swift swift 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm scala scala 3629_minimum_jumps_to_reach_end_via_prime_teleportation
docker compose -f docker/docker-compose.yml run --rm php php 3629_minimum_jumps_to_reach_end_via_prime_teleportation
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3629_minimum_jumps_to_reach_end_via_prime_teleportation` |

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
.\scripts\test.ps1 -Folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation -AllLanguages
```

```bash
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --all-languages
```

```zsh
./scripts/test.sh --folder 3629_minimum_jumps_to_reach_end_via_prime_teleportation --all-languages
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
