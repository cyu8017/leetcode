# Test harness for 0120_triangle

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0120_triangle -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0120_triangle -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0120_triangle -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0120_triangle -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0120_triangle -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0120_triangle -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0120_triangle -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0120_triangle -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0120_triangle -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0120_triangle -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0120_triangle -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0120_triangle -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0120_triangle -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0120_triangle -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0120_triangle --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0120_triangle --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0120_triangle --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0120_triangle --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0120_triangle --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0120_triangle --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0120_triangle --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0120_triangle --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0120_triangle --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0120_triangle --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0120_triangle --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0120_triangle --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0120_triangle --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0120_triangle --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0120_triangle --language python
./scripts/test.sh --folder 0120_triangle --language javascript
./scripts/test.sh --folder 0120_triangle --language typescript
./scripts/test.sh --folder 0120_triangle --language java
./scripts/test.sh --folder 0120_triangle --language cpp
./scripts/test.sh --folder 0120_triangle --language c
./scripts/test.sh --folder 0120_triangle --language go
./scripts/test.sh --folder 0120_triangle --language rust
./scripts/test.sh --folder 0120_triangle --language kotlin
./scripts/test.sh --folder 0120_triangle --language swift
./scripts/test.sh --folder 0120_triangle --language ruby
./scripts/test.sh --folder 0120_triangle --language csharp
./scripts/test.sh --folder 0120_triangle --language scala
./scripts/test.sh --folder 0120_triangle --language php
./scripts/test.sh --folder 0120_triangle --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0120_triangle --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0120_triangle --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0120_triangle --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0120_triangle --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0120_triangle --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0120_triangle --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0120_triangle --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0120_triangle --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0120_triangle --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0120_triangle --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0120_triangle --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0120_triangle --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0120_triangle --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0120_triangle --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0120_triangle
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0120_triangle
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0120_triangle
docker compose -f docker/docker-compose.yml run --rm java java 0120_triangle
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0120_triangle
docker compose -f docker/docker-compose.yml run --rm c c 0120_triangle
docker compose -f docker/docker-compose.yml run --rm go go 0120_triangle
docker compose -f docker/docker-compose.yml run --rm rust rust 0120_triangle
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0120_triangle
docker compose -f docker/docker-compose.yml run --rm swift swift 0120_triangle
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0120_triangle
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0120_triangle
docker compose -f docker/docker-compose.yml run --rm scala scala 0120_triangle
docker compose -f docker/docker-compose.yml run --rm php php 0120_triangle
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0120_triangle` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0120_triangle` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0120_triangle` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0120_triangle` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0120_triangle` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0120_triangle` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0120_triangle` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0120_triangle` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0120_triangle` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0120_triangle` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0120_triangle` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0120_triangle` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0120_triangle` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0120_triangle` |

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
.\scripts\test.ps1 -Folder 0120_triangle -AllLanguages
```

```bash
./scripts/test.sh --folder 0120_triangle --all-languages
```

```zsh
./scripts/test.sh --folder 0120_triangle --all-languages
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
