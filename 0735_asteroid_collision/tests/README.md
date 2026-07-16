# Test harness for 0735_asteroid_collision

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0735_asteroid_collision -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0735_asteroid_collision --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0735_asteroid_collision --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0735_asteroid_collision --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0735_asteroid_collision --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0735_asteroid_collision --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0735_asteroid_collision --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0735_asteroid_collision --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0735_asteroid_collision --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0735_asteroid_collision --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0735_asteroid_collision --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0735_asteroid_collision --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0735_asteroid_collision --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0735_asteroid_collision --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0735_asteroid_collision --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0735_asteroid_collision --language python
./scripts/test.sh --folder 0735_asteroid_collision --language javascript
./scripts/test.sh --folder 0735_asteroid_collision --language typescript
./scripts/test.sh --folder 0735_asteroid_collision --language java
./scripts/test.sh --folder 0735_asteroid_collision --language cpp
./scripts/test.sh --folder 0735_asteroid_collision --language c
./scripts/test.sh --folder 0735_asteroid_collision --language go
./scripts/test.sh --folder 0735_asteroid_collision --language rust
./scripts/test.sh --folder 0735_asteroid_collision --language kotlin
./scripts/test.sh --folder 0735_asteroid_collision --language swift
./scripts/test.sh --folder 0735_asteroid_collision --language ruby
./scripts/test.sh --folder 0735_asteroid_collision --language csharp
./scripts/test.sh --folder 0735_asteroid_collision --language scala
./scripts/test.sh --folder 0735_asteroid_collision --language php
./scripts/test.sh --folder 0735_asteroid_collision --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0735_asteroid_collision --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0735_asteroid_collision --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0735_asteroid_collision --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0735_asteroid_collision --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0735_asteroid_collision --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0735_asteroid_collision --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0735_asteroid_collision --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0735_asteroid_collision --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0735_asteroid_collision --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0735_asteroid_collision --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0735_asteroid_collision --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0735_asteroid_collision --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0735_asteroid_collision --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0735_asteroid_collision --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm java java 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm c c 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm go go 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm rust rust 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm swift swift 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm scala scala 0735_asteroid_collision
docker compose -f docker/docker-compose.yml run --rm php php 0735_asteroid_collision
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0735_asteroid_collision` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0735_asteroid_collision` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0735_asteroid_collision` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0735_asteroid_collision` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0735_asteroid_collision` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0735_asteroid_collision` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0735_asteroid_collision` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0735_asteroid_collision` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0735_asteroid_collision` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0735_asteroid_collision` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0735_asteroid_collision` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0735_asteroid_collision` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0735_asteroid_collision` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0735_asteroid_collision` |

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
.\scripts\test.ps1 -Folder 0735_asteroid_collision -AllLanguages
```

```bash
./scripts/test.sh --folder 0735_asteroid_collision --all-languages
```

```zsh
./scripts/test.sh --folder 0735_asteroid_collision --all-languages
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
