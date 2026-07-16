# Test harness for 3643_flip_square_submatrix_vertically

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language python
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language javascript
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language typescript
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language java
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language cpp
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language c
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language go
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language rust
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language kotlin
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language swift
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language ruby
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language csharp
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language scala
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language php
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm java java 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm c c 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm go go 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm rust rust 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm swift swift 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm scala scala 3643_flip_square_submatrix_vertically
docker compose -f docker/docker-compose.yml run --rm php php 3643_flip_square_submatrix_vertically
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3643_flip_square_submatrix_vertically` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3643_flip_square_submatrix_vertically` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3643_flip_square_submatrix_vertically` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3643_flip_square_submatrix_vertically` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3643_flip_square_submatrix_vertically` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3643_flip_square_submatrix_vertically` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3643_flip_square_submatrix_vertically` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3643_flip_square_submatrix_vertically` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3643_flip_square_submatrix_vertically` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3643_flip_square_submatrix_vertically` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3643_flip_square_submatrix_vertically` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3643_flip_square_submatrix_vertically` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3643_flip_square_submatrix_vertically` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3643_flip_square_submatrix_vertically` |

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
.\scripts\test.ps1 -Folder 3643_flip_square_submatrix_vertically -AllLanguages
```

```bash
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --all-languages
```

```zsh
./scripts/test.sh --folder 3643_flip_square_submatrix_vertically --all-languages
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
