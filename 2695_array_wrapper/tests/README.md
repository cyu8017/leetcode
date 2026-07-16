# Test harness for 2695_array_wrapper

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2695_array_wrapper -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2695_array_wrapper --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2695_array_wrapper --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2695_array_wrapper --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2695_array_wrapper --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2695_array_wrapper --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2695_array_wrapper --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2695_array_wrapper --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2695_array_wrapper --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2695_array_wrapper --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2695_array_wrapper --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2695_array_wrapper --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2695_array_wrapper --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2695_array_wrapper --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2695_array_wrapper --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2695_array_wrapper --language python
./scripts/test.sh --folder 2695_array_wrapper --language javascript
./scripts/test.sh --folder 2695_array_wrapper --language typescript
./scripts/test.sh --folder 2695_array_wrapper --language java
./scripts/test.sh --folder 2695_array_wrapper --language cpp
./scripts/test.sh --folder 2695_array_wrapper --language c
./scripts/test.sh --folder 2695_array_wrapper --language go
./scripts/test.sh --folder 2695_array_wrapper --language rust
./scripts/test.sh --folder 2695_array_wrapper --language kotlin
./scripts/test.sh --folder 2695_array_wrapper --language swift
./scripts/test.sh --folder 2695_array_wrapper --language ruby
./scripts/test.sh --folder 2695_array_wrapper --language csharp
./scripts/test.sh --folder 2695_array_wrapper --language scala
./scripts/test.sh --folder 2695_array_wrapper --language php
./scripts/test.sh --folder 2695_array_wrapper --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2695_array_wrapper --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2695_array_wrapper --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2695_array_wrapper --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2695_array_wrapper --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2695_array_wrapper --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2695_array_wrapper --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2695_array_wrapper --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2695_array_wrapper --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2695_array_wrapper --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2695_array_wrapper --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2695_array_wrapper --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2695_array_wrapper --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2695_array_wrapper --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2695_array_wrapper --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm java java 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm c c 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm go go 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm rust rust 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm swift swift 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm scala scala 2695_array_wrapper
docker compose -f docker/docker-compose.yml run --rm php php 2695_array_wrapper
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2695_array_wrapper` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2695_array_wrapper` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2695_array_wrapper` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2695_array_wrapper` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2695_array_wrapper` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2695_array_wrapper` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2695_array_wrapper` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2695_array_wrapper` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2695_array_wrapper` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2695_array_wrapper` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2695_array_wrapper` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2695_array_wrapper` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2695_array_wrapper` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2695_array_wrapper` |

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
.\scripts\test.ps1 -Folder 2695_array_wrapper -AllLanguages
```

```bash
./scripts/test.sh --folder 2695_array_wrapper --all-languages
```

```zsh
./scripts/test.sh --folder 2695_array_wrapper --all-languages
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
