# Test harness for 2126_destroying_asteroids

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2126_destroying_asteroids -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2126_destroying_asteroids --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2126_destroying_asteroids --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2126_destroying_asteroids --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2126_destroying_asteroids --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2126_destroying_asteroids --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2126_destroying_asteroids --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2126_destroying_asteroids --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2126_destroying_asteroids --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2126_destroying_asteroids --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2126_destroying_asteroids --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2126_destroying_asteroids --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2126_destroying_asteroids --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2126_destroying_asteroids --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2126_destroying_asteroids --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2126_destroying_asteroids --language python
./scripts/test.sh --folder 2126_destroying_asteroids --language javascript
./scripts/test.sh --folder 2126_destroying_asteroids --language typescript
./scripts/test.sh --folder 2126_destroying_asteroids --language java
./scripts/test.sh --folder 2126_destroying_asteroids --language cpp
./scripts/test.sh --folder 2126_destroying_asteroids --language c
./scripts/test.sh --folder 2126_destroying_asteroids --language go
./scripts/test.sh --folder 2126_destroying_asteroids --language rust
./scripts/test.sh --folder 2126_destroying_asteroids --language kotlin
./scripts/test.sh --folder 2126_destroying_asteroids --language swift
./scripts/test.sh --folder 2126_destroying_asteroids --language ruby
./scripts/test.sh --folder 2126_destroying_asteroids --language csharp
./scripts/test.sh --folder 2126_destroying_asteroids --language scala
./scripts/test.sh --folder 2126_destroying_asteroids --language php
./scripts/test.sh --folder 2126_destroying_asteroids --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2126_destroying_asteroids --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2126_destroying_asteroids --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2126_destroying_asteroids --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2126_destroying_asteroids --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2126_destroying_asteroids --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2126_destroying_asteroids --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2126_destroying_asteroids --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2126_destroying_asteroids --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2126_destroying_asteroids --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2126_destroying_asteroids --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2126_destroying_asteroids --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2126_destroying_asteroids --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2126_destroying_asteroids --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2126_destroying_asteroids --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm java java 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm c c 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm go go 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm rust rust 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm swift swift 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm scala scala 2126_destroying_asteroids
docker compose -f docker/docker-compose.yml run --rm php php 2126_destroying_asteroids
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2126_destroying_asteroids` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2126_destroying_asteroids` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2126_destroying_asteroids` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2126_destroying_asteroids` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2126_destroying_asteroids` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2126_destroying_asteroids` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2126_destroying_asteroids` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2126_destroying_asteroids` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2126_destroying_asteroids` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2126_destroying_asteroids` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2126_destroying_asteroids` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2126_destroying_asteroids` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2126_destroying_asteroids` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2126_destroying_asteroids` |

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
.\scripts\test.ps1 -Folder 2126_destroying_asteroids -AllLanguages
```

```bash
./scripts/test.sh --folder 2126_destroying_asteroids --all-languages
```

```zsh
./scripts/test.sh --folder 2126_destroying_asteroids --all-languages
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
