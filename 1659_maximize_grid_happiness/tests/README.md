# Test harness for 1659_maximize_grid_happiness

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1659_maximize_grid_happiness --language python
./scripts/test.sh --folder 1659_maximize_grid_happiness --language javascript
./scripts/test.sh --folder 1659_maximize_grid_happiness --language typescript
./scripts/test.sh --folder 1659_maximize_grid_happiness --language java
./scripts/test.sh --folder 1659_maximize_grid_happiness --language cpp
./scripts/test.sh --folder 1659_maximize_grid_happiness --language c
./scripts/test.sh --folder 1659_maximize_grid_happiness --language go
./scripts/test.sh --folder 1659_maximize_grid_happiness --language rust
./scripts/test.sh --folder 1659_maximize_grid_happiness --language kotlin
./scripts/test.sh --folder 1659_maximize_grid_happiness --language swift
./scripts/test.sh --folder 1659_maximize_grid_happiness --language ruby
./scripts/test.sh --folder 1659_maximize_grid_happiness --language csharp
./scripts/test.sh --folder 1659_maximize_grid_happiness --language scala
./scripts/test.sh --folder 1659_maximize_grid_happiness --language php
./scripts/test.sh --folder 1659_maximize_grid_happiness --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1659_maximize_grid_happiness --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm java java 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm c c 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm go go 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm rust rust 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm swift swift 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm scala scala 1659_maximize_grid_happiness
docker compose -f docker/docker-compose.yml run --rm php php 1659_maximize_grid_happiness
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1659_maximize_grid_happiness` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1659_maximize_grid_happiness` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1659_maximize_grid_happiness` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1659_maximize_grid_happiness` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1659_maximize_grid_happiness` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1659_maximize_grid_happiness` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1659_maximize_grid_happiness` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1659_maximize_grid_happiness` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1659_maximize_grid_happiness` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1659_maximize_grid_happiness` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1659_maximize_grid_happiness` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1659_maximize_grid_happiness` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1659_maximize_grid_happiness` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1659_maximize_grid_happiness` |

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
.\scripts\test.ps1 -Folder 1659_maximize_grid_happiness -AllLanguages
```

```bash
./scripts/test.sh --folder 1659_maximize_grid_happiness --all-languages
```

```zsh
./scripts/test.sh --folder 1659_maximize_grid_happiness --all-languages
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
