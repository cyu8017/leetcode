# Test harness for 0614_second_degree_follower

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0614_second_degree_follower -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0614_second_degree_follower --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0614_second_degree_follower --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0614_second_degree_follower --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0614_second_degree_follower --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0614_second_degree_follower --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0614_second_degree_follower --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0614_second_degree_follower --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0614_second_degree_follower --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0614_second_degree_follower --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0614_second_degree_follower --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0614_second_degree_follower --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0614_second_degree_follower --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0614_second_degree_follower --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0614_second_degree_follower --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0614_second_degree_follower --language python
./scripts/test.sh --folder 0614_second_degree_follower --language javascript
./scripts/test.sh --folder 0614_second_degree_follower --language typescript
./scripts/test.sh --folder 0614_second_degree_follower --language java
./scripts/test.sh --folder 0614_second_degree_follower --language cpp
./scripts/test.sh --folder 0614_second_degree_follower --language c
./scripts/test.sh --folder 0614_second_degree_follower --language go
./scripts/test.sh --folder 0614_second_degree_follower --language rust
./scripts/test.sh --folder 0614_second_degree_follower --language kotlin
./scripts/test.sh --folder 0614_second_degree_follower --language swift
./scripts/test.sh --folder 0614_second_degree_follower --language ruby
./scripts/test.sh --folder 0614_second_degree_follower --language csharp
./scripts/test.sh --folder 0614_second_degree_follower --language scala
./scripts/test.sh --folder 0614_second_degree_follower --language php
./scripts/test.sh --folder 0614_second_degree_follower --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0614_second_degree_follower --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0614_second_degree_follower --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0614_second_degree_follower --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0614_second_degree_follower --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0614_second_degree_follower --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0614_second_degree_follower --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0614_second_degree_follower --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0614_second_degree_follower --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0614_second_degree_follower --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0614_second_degree_follower --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0614_second_degree_follower --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0614_second_degree_follower --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0614_second_degree_follower --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0614_second_degree_follower --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm java java 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm c c 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm go go 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm rust rust 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm swift swift 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm scala scala 0614_second_degree_follower
docker compose -f docker/docker-compose.yml run --rm php php 0614_second_degree_follower
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0614_second_degree_follower` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0614_second_degree_follower` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0614_second_degree_follower` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0614_second_degree_follower` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0614_second_degree_follower` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0614_second_degree_follower` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0614_second_degree_follower` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0614_second_degree_follower` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0614_second_degree_follower` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0614_second_degree_follower` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0614_second_degree_follower` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0614_second_degree_follower` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0614_second_degree_follower` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0614_second_degree_follower` |

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
.\scripts\test.ps1 -Folder 0614_second_degree_follower -AllLanguages
```

```bash
./scripts/test.sh --folder 0614_second_degree_follower --all-languages
```

```zsh
./scripts/test.sh --folder 0614_second_degree_follower --all-languages
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
