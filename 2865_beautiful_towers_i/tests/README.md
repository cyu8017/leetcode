# Test harness for 2865_beautiful_towers_i

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2865_beautiful_towers_i --language python
./scripts/test.sh --folder 2865_beautiful_towers_i --language javascript
./scripts/test.sh --folder 2865_beautiful_towers_i --language typescript
./scripts/test.sh --folder 2865_beautiful_towers_i --language java
./scripts/test.sh --folder 2865_beautiful_towers_i --language cpp
./scripts/test.sh --folder 2865_beautiful_towers_i --language c
./scripts/test.sh --folder 2865_beautiful_towers_i --language go
./scripts/test.sh --folder 2865_beautiful_towers_i --language rust
./scripts/test.sh --folder 2865_beautiful_towers_i --language kotlin
./scripts/test.sh --folder 2865_beautiful_towers_i --language swift
./scripts/test.sh --folder 2865_beautiful_towers_i --language ruby
./scripts/test.sh --folder 2865_beautiful_towers_i --language csharp
./scripts/test.sh --folder 2865_beautiful_towers_i --language scala
./scripts/test.sh --folder 2865_beautiful_towers_i --language php
./scripts/test.sh --folder 2865_beautiful_towers_i --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2865_beautiful_towers_i --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm java java 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm c c 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm go go 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm rust rust 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm swift swift 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm scala scala 2865_beautiful_towers_i
docker compose -f docker/docker-compose.yml run --rm php php 2865_beautiful_towers_i
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2865_beautiful_towers_i` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2865_beautiful_towers_i` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2865_beautiful_towers_i` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2865_beautiful_towers_i` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2865_beautiful_towers_i` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2865_beautiful_towers_i` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2865_beautiful_towers_i` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2865_beautiful_towers_i` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2865_beautiful_towers_i` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2865_beautiful_towers_i` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2865_beautiful_towers_i` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2865_beautiful_towers_i` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2865_beautiful_towers_i` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2865_beautiful_towers_i` |

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
.\scripts\test.ps1 -Folder 2865_beautiful_towers_i -AllLanguages
```

```bash
./scripts/test.sh --folder 2865_beautiful_towers_i --all-languages
```

```zsh
./scripts/test.sh --folder 2865_beautiful_towers_i --all-languages
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
