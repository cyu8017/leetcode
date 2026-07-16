# Test harness for 3417_zigzag_grid_traversal_with_skip

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language python
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language javascript
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language typescript
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language java
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language cpp
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language c
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language go
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language rust
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language kotlin
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language swift
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language ruby
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language csharp
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language scala
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language php
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm java java 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm c c 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm go go 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm rust rust 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm swift swift 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm scala scala 3417_zigzag_grid_traversal_with_skip
docker compose -f docker/docker-compose.yml run --rm php php 3417_zigzag_grid_traversal_with_skip
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3417_zigzag_grid_traversal_with_skip` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3417_zigzag_grid_traversal_with_skip` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3417_zigzag_grid_traversal_with_skip` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3417_zigzag_grid_traversal_with_skip` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3417_zigzag_grid_traversal_with_skip` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3417_zigzag_grid_traversal_with_skip` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3417_zigzag_grid_traversal_with_skip` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3417_zigzag_grid_traversal_with_skip` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3417_zigzag_grid_traversal_with_skip` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3417_zigzag_grid_traversal_with_skip` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3417_zigzag_grid_traversal_with_skip` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3417_zigzag_grid_traversal_with_skip` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3417_zigzag_grid_traversal_with_skip` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3417_zigzag_grid_traversal_with_skip` |

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
.\scripts\test.ps1 -Folder 3417_zigzag_grid_traversal_with_skip -AllLanguages
```

```bash
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --all-languages
```

```zsh
./scripts/test.sh --folder 3417_zigzag_grid_traversal_with_skip --all-languages
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
