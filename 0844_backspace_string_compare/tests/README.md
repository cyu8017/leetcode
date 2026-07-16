# Test harness for 0844_backspace_string_compare

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0844_backspace_string_compare -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0844_backspace_string_compare --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0844_backspace_string_compare --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0844_backspace_string_compare --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0844_backspace_string_compare --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0844_backspace_string_compare --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0844_backspace_string_compare --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0844_backspace_string_compare --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0844_backspace_string_compare --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0844_backspace_string_compare --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0844_backspace_string_compare --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0844_backspace_string_compare --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0844_backspace_string_compare --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0844_backspace_string_compare --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0844_backspace_string_compare --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0844_backspace_string_compare --language python
./scripts/test.sh --folder 0844_backspace_string_compare --language javascript
./scripts/test.sh --folder 0844_backspace_string_compare --language typescript
./scripts/test.sh --folder 0844_backspace_string_compare --language java
./scripts/test.sh --folder 0844_backspace_string_compare --language cpp
./scripts/test.sh --folder 0844_backspace_string_compare --language c
./scripts/test.sh --folder 0844_backspace_string_compare --language go
./scripts/test.sh --folder 0844_backspace_string_compare --language rust
./scripts/test.sh --folder 0844_backspace_string_compare --language kotlin
./scripts/test.sh --folder 0844_backspace_string_compare --language swift
./scripts/test.sh --folder 0844_backspace_string_compare --language ruby
./scripts/test.sh --folder 0844_backspace_string_compare --language csharp
./scripts/test.sh --folder 0844_backspace_string_compare --language scala
./scripts/test.sh --folder 0844_backspace_string_compare --language php
./scripts/test.sh --folder 0844_backspace_string_compare --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0844_backspace_string_compare --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0844_backspace_string_compare --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0844_backspace_string_compare --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0844_backspace_string_compare --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0844_backspace_string_compare --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0844_backspace_string_compare --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0844_backspace_string_compare --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0844_backspace_string_compare --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0844_backspace_string_compare --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0844_backspace_string_compare --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0844_backspace_string_compare --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0844_backspace_string_compare --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0844_backspace_string_compare --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0844_backspace_string_compare --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm java java 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm c c 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm go go 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm rust rust 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm swift swift 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm scala scala 0844_backspace_string_compare
docker compose -f docker/docker-compose.yml run --rm php php 0844_backspace_string_compare
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0844_backspace_string_compare` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0844_backspace_string_compare` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0844_backspace_string_compare` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0844_backspace_string_compare` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0844_backspace_string_compare` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0844_backspace_string_compare` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0844_backspace_string_compare` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0844_backspace_string_compare` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0844_backspace_string_compare` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0844_backspace_string_compare` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0844_backspace_string_compare` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0844_backspace_string_compare` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0844_backspace_string_compare` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0844_backspace_string_compare` |

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
.\scripts\test.ps1 -Folder 0844_backspace_string_compare -AllLanguages
```

```bash
./scripts/test.sh --folder 0844_backspace_string_compare --all-languages
```

```zsh
./scripts/test.sh --folder 0844_backspace_string_compare --all-languages
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
