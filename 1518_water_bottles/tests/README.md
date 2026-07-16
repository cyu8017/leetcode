# Test harness for 1518_water_bottles

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1518_water_bottles -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1518_water_bottles --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1518_water_bottles --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1518_water_bottles --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1518_water_bottles --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1518_water_bottles --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1518_water_bottles --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1518_water_bottles --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1518_water_bottles --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1518_water_bottles --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1518_water_bottles --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1518_water_bottles --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1518_water_bottles --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1518_water_bottles --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1518_water_bottles --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1518_water_bottles --language python
./scripts/test.sh --folder 1518_water_bottles --language javascript
./scripts/test.sh --folder 1518_water_bottles --language typescript
./scripts/test.sh --folder 1518_water_bottles --language java
./scripts/test.sh --folder 1518_water_bottles --language cpp
./scripts/test.sh --folder 1518_water_bottles --language c
./scripts/test.sh --folder 1518_water_bottles --language go
./scripts/test.sh --folder 1518_water_bottles --language rust
./scripts/test.sh --folder 1518_water_bottles --language kotlin
./scripts/test.sh --folder 1518_water_bottles --language swift
./scripts/test.sh --folder 1518_water_bottles --language ruby
./scripts/test.sh --folder 1518_water_bottles --language csharp
./scripts/test.sh --folder 1518_water_bottles --language scala
./scripts/test.sh --folder 1518_water_bottles --language php
./scripts/test.sh --folder 1518_water_bottles --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1518_water_bottles --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1518_water_bottles --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1518_water_bottles --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1518_water_bottles --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1518_water_bottles --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1518_water_bottles --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1518_water_bottles --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1518_water_bottles --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1518_water_bottles --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1518_water_bottles --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1518_water_bottles --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1518_water_bottles --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1518_water_bottles --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1518_water_bottles --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm java java 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm c c 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm go go 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm rust rust 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm swift swift 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm scala scala 1518_water_bottles
docker compose -f docker/docker-compose.yml run --rm php php 1518_water_bottles
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1518_water_bottles` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1518_water_bottles` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1518_water_bottles` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1518_water_bottles` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1518_water_bottles` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1518_water_bottles` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1518_water_bottles` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1518_water_bottles` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1518_water_bottles` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1518_water_bottles` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1518_water_bottles` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1518_water_bottles` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1518_water_bottles` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1518_water_bottles` |

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
.\scripts\test.ps1 -Folder 1518_water_bottles -AllLanguages
```

```bash
./scripts/test.sh --folder 1518_water_bottles --all-languages
```

```zsh
./scripts/test.sh --folder 1518_water_bottles --all-languages
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
