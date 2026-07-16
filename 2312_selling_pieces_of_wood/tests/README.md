# Test harness for 2312_selling_pieces_of_wood

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language python
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language javascript
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language typescript
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language java
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language cpp
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language c
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language go
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language rust
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language kotlin
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language swift
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language ruby
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language csharp
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language scala
./scripts/test.sh --folder 2312_selling_pieces_of_wood --language php
./scripts/test.sh --folder 2312_selling_pieces_of_wood --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2312_selling_pieces_of_wood --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm java java 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm c c 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm go go 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm rust rust 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm swift swift 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm scala scala 2312_selling_pieces_of_wood
docker compose -f docker/docker-compose.yml run --rm php php 2312_selling_pieces_of_wood
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2312_selling_pieces_of_wood` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2312_selling_pieces_of_wood` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2312_selling_pieces_of_wood` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2312_selling_pieces_of_wood` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2312_selling_pieces_of_wood` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2312_selling_pieces_of_wood` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2312_selling_pieces_of_wood` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2312_selling_pieces_of_wood` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2312_selling_pieces_of_wood` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2312_selling_pieces_of_wood` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2312_selling_pieces_of_wood` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2312_selling_pieces_of_wood` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2312_selling_pieces_of_wood` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2312_selling_pieces_of_wood` |

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
.\scripts\test.ps1 -Folder 2312_selling_pieces_of_wood -AllLanguages
```

```bash
./scripts/test.sh --folder 2312_selling_pieces_of_wood --all-languages
```

```zsh
./scripts/test.sh --folder 2312_selling_pieces_of_wood --all-languages
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
