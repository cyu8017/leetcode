# Test harness for 0317_shortest_distance_from_all_buildings

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language python
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language javascript
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language typescript
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language java
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language cpp
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language c
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language go
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language rust
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language kotlin
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language swift
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language ruby
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language csharp
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language scala
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language php
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm java java 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm c c 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm go go 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm rust rust 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm swift swift 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm scala scala 0317_shortest_distance_from_all_buildings
docker compose -f docker/docker-compose.yml run --rm php php 0317_shortest_distance_from_all_buildings
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0317_shortest_distance_from_all_buildings` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0317_shortest_distance_from_all_buildings` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0317_shortest_distance_from_all_buildings` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0317_shortest_distance_from_all_buildings` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0317_shortest_distance_from_all_buildings` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0317_shortest_distance_from_all_buildings` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0317_shortest_distance_from_all_buildings` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0317_shortest_distance_from_all_buildings` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0317_shortest_distance_from_all_buildings` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0317_shortest_distance_from_all_buildings` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0317_shortest_distance_from_all_buildings` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0317_shortest_distance_from_all_buildings` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0317_shortest_distance_from_all_buildings` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0317_shortest_distance_from_all_buildings` |

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
.\scripts\test.ps1 -Folder 0317_shortest_distance_from_all_buildings -AllLanguages
```

```bash
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --all-languages
```

```zsh
./scripts/test.sh --folder 0317_shortest_distance_from_all_buildings --all-languages
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
