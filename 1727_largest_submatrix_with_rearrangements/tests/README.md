# Test harness for 1727_largest_submatrix_with_rearrangements

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language python
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language javascript
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language typescript
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language java
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language cpp
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language c
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language go
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language rust
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language kotlin
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language swift
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language ruby
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language csharp
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language scala
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language php
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm java java 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm c c 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm go go 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm rust rust 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm swift swift 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm scala scala 1727_largest_submatrix_with_rearrangements
docker compose -f docker/docker-compose.yml run --rm php php 1727_largest_submatrix_with_rearrangements
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1727_largest_submatrix_with_rearrangements` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1727_largest_submatrix_with_rearrangements` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1727_largest_submatrix_with_rearrangements` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1727_largest_submatrix_with_rearrangements` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1727_largest_submatrix_with_rearrangements` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1727_largest_submatrix_with_rearrangements` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1727_largest_submatrix_with_rearrangements` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1727_largest_submatrix_with_rearrangements` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1727_largest_submatrix_with_rearrangements` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1727_largest_submatrix_with_rearrangements` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1727_largest_submatrix_with_rearrangements` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1727_largest_submatrix_with_rearrangements` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1727_largest_submatrix_with_rearrangements` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1727_largest_submatrix_with_rearrangements` |

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
.\scripts\test.ps1 -Folder 1727_largest_submatrix_with_rearrangements -AllLanguages
```

```bash
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --all-languages
```

```zsh
./scripts/test.sh --folder 1727_largest_submatrix_with_rearrangements --all-languages
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
