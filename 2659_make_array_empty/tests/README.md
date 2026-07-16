# Test harness for 2659_make_array_empty

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2659_make_array_empty -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2659_make_array_empty --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2659_make_array_empty --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2659_make_array_empty --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2659_make_array_empty --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2659_make_array_empty --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2659_make_array_empty --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2659_make_array_empty --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2659_make_array_empty --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2659_make_array_empty --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2659_make_array_empty --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2659_make_array_empty --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2659_make_array_empty --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2659_make_array_empty --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2659_make_array_empty --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2659_make_array_empty --language python
./scripts/test.sh --folder 2659_make_array_empty --language javascript
./scripts/test.sh --folder 2659_make_array_empty --language typescript
./scripts/test.sh --folder 2659_make_array_empty --language java
./scripts/test.sh --folder 2659_make_array_empty --language cpp
./scripts/test.sh --folder 2659_make_array_empty --language c
./scripts/test.sh --folder 2659_make_array_empty --language go
./scripts/test.sh --folder 2659_make_array_empty --language rust
./scripts/test.sh --folder 2659_make_array_empty --language kotlin
./scripts/test.sh --folder 2659_make_array_empty --language swift
./scripts/test.sh --folder 2659_make_array_empty --language ruby
./scripts/test.sh --folder 2659_make_array_empty --language csharp
./scripts/test.sh --folder 2659_make_array_empty --language scala
./scripts/test.sh --folder 2659_make_array_empty --language php
./scripts/test.sh --folder 2659_make_array_empty --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2659_make_array_empty --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2659_make_array_empty --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2659_make_array_empty --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2659_make_array_empty --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2659_make_array_empty --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2659_make_array_empty --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2659_make_array_empty --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2659_make_array_empty --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2659_make_array_empty --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2659_make_array_empty --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2659_make_array_empty --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2659_make_array_empty --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2659_make_array_empty --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2659_make_array_empty --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm java java 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm c c 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm go go 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm rust rust 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm swift swift 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm scala scala 2659_make_array_empty
docker compose -f docker/docker-compose.yml run --rm php php 2659_make_array_empty
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2659_make_array_empty` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2659_make_array_empty` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2659_make_array_empty` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2659_make_array_empty` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2659_make_array_empty` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2659_make_array_empty` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2659_make_array_empty` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2659_make_array_empty` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2659_make_array_empty` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2659_make_array_empty` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2659_make_array_empty` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2659_make_array_empty` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2659_make_array_empty` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2659_make_array_empty` |

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
.\scripts\test.ps1 -Folder 2659_make_array_empty -AllLanguages
```

```bash
./scripts/test.sh --folder 2659_make_array_empty --all-languages
```

```zsh
./scripts/test.sh --folder 2659_make_array_empty --all-languages
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
