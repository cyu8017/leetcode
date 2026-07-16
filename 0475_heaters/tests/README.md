# Test harness for 0475_heaters

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0475_heaters -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0475_heaters -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0475_heaters -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0475_heaters -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0475_heaters -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0475_heaters -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0475_heaters -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0475_heaters -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0475_heaters -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0475_heaters -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0475_heaters -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0475_heaters -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0475_heaters -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0475_heaters -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0475_heaters --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0475_heaters --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0475_heaters --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0475_heaters --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0475_heaters --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0475_heaters --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0475_heaters --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0475_heaters --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0475_heaters --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0475_heaters --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0475_heaters --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0475_heaters --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0475_heaters --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0475_heaters --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0475_heaters --language python
./scripts/test.sh --folder 0475_heaters --language javascript
./scripts/test.sh --folder 0475_heaters --language typescript
./scripts/test.sh --folder 0475_heaters --language java
./scripts/test.sh --folder 0475_heaters --language cpp
./scripts/test.sh --folder 0475_heaters --language c
./scripts/test.sh --folder 0475_heaters --language go
./scripts/test.sh --folder 0475_heaters --language rust
./scripts/test.sh --folder 0475_heaters --language kotlin
./scripts/test.sh --folder 0475_heaters --language swift
./scripts/test.sh --folder 0475_heaters --language ruby
./scripts/test.sh --folder 0475_heaters --language csharp
./scripts/test.sh --folder 0475_heaters --language scala
./scripts/test.sh --folder 0475_heaters --language php
./scripts/test.sh --folder 0475_heaters --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0475_heaters --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0475_heaters --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0475_heaters --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0475_heaters --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0475_heaters --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0475_heaters --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0475_heaters --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0475_heaters --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0475_heaters --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0475_heaters --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0475_heaters --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0475_heaters --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0475_heaters --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0475_heaters --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0475_heaters
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0475_heaters
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0475_heaters
docker compose -f docker/docker-compose.yml run --rm java java 0475_heaters
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0475_heaters
docker compose -f docker/docker-compose.yml run --rm c c 0475_heaters
docker compose -f docker/docker-compose.yml run --rm go go 0475_heaters
docker compose -f docker/docker-compose.yml run --rm rust rust 0475_heaters
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0475_heaters
docker compose -f docker/docker-compose.yml run --rm swift swift 0475_heaters
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0475_heaters
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0475_heaters
docker compose -f docker/docker-compose.yml run --rm scala scala 0475_heaters
docker compose -f docker/docker-compose.yml run --rm php php 0475_heaters
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0475_heaters` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0475_heaters` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0475_heaters` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0475_heaters` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0475_heaters` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0475_heaters` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0475_heaters` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0475_heaters` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0475_heaters` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0475_heaters` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0475_heaters` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0475_heaters` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0475_heaters` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0475_heaters` |

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
.\scripts\test.ps1 -Folder 0475_heaters -AllLanguages
```

```bash
./scripts/test.sh --folder 0475_heaters --all-languages
```

```zsh
./scripts/test.sh --folder 0475_heaters --all-languages
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
