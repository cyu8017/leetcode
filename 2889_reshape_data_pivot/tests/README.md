# Test harness for 2889_reshape_data_pivot

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2889_reshape_data_pivot --language python
./scripts/test.sh --folder 2889_reshape_data_pivot --language javascript
./scripts/test.sh --folder 2889_reshape_data_pivot --language typescript
./scripts/test.sh --folder 2889_reshape_data_pivot --language java
./scripts/test.sh --folder 2889_reshape_data_pivot --language cpp
./scripts/test.sh --folder 2889_reshape_data_pivot --language c
./scripts/test.sh --folder 2889_reshape_data_pivot --language go
./scripts/test.sh --folder 2889_reshape_data_pivot --language rust
./scripts/test.sh --folder 2889_reshape_data_pivot --language kotlin
./scripts/test.sh --folder 2889_reshape_data_pivot --language swift
./scripts/test.sh --folder 2889_reshape_data_pivot --language ruby
./scripts/test.sh --folder 2889_reshape_data_pivot --language csharp
./scripts/test.sh --folder 2889_reshape_data_pivot --language scala
./scripts/test.sh --folder 2889_reshape_data_pivot --language php
./scripts/test.sh --folder 2889_reshape_data_pivot --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2889_reshape_data_pivot --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm java java 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm c c 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm go go 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm rust rust 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm swift swift 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm scala scala 2889_reshape_data_pivot
docker compose -f docker/docker-compose.yml run --rm php php 2889_reshape_data_pivot
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2889_reshape_data_pivot` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2889_reshape_data_pivot` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2889_reshape_data_pivot` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2889_reshape_data_pivot` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2889_reshape_data_pivot` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2889_reshape_data_pivot` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2889_reshape_data_pivot` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2889_reshape_data_pivot` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2889_reshape_data_pivot` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2889_reshape_data_pivot` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2889_reshape_data_pivot` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2889_reshape_data_pivot` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2889_reshape_data_pivot` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2889_reshape_data_pivot` |

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
.\scripts\test.ps1 -Folder 2889_reshape_data_pivot -AllLanguages
```

```bash
./scripts/test.sh --folder 2889_reshape_data_pivot --all-languages
```

```zsh
./scripts/test.sh --folder 2889_reshape_data_pivot --all-languages
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
