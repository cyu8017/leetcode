# Test harness for 2804_array_prototype_foreach

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2804_array_prototype_foreach --language python
./scripts/test.sh --folder 2804_array_prototype_foreach --language javascript
./scripts/test.sh --folder 2804_array_prototype_foreach --language typescript
./scripts/test.sh --folder 2804_array_prototype_foreach --language java
./scripts/test.sh --folder 2804_array_prototype_foreach --language cpp
./scripts/test.sh --folder 2804_array_prototype_foreach --language c
./scripts/test.sh --folder 2804_array_prototype_foreach --language go
./scripts/test.sh --folder 2804_array_prototype_foreach --language rust
./scripts/test.sh --folder 2804_array_prototype_foreach --language kotlin
./scripts/test.sh --folder 2804_array_prototype_foreach --language swift
./scripts/test.sh --folder 2804_array_prototype_foreach --language ruby
./scripts/test.sh --folder 2804_array_prototype_foreach --language csharp
./scripts/test.sh --folder 2804_array_prototype_foreach --language scala
./scripts/test.sh --folder 2804_array_prototype_foreach --language php
./scripts/test.sh --folder 2804_array_prototype_foreach --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2804_array_prototype_foreach --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm java java 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm c c 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm go go 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm rust rust 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm swift swift 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm scala scala 2804_array_prototype_foreach
docker compose -f docker/docker-compose.yml run --rm php php 2804_array_prototype_foreach
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2804_array_prototype_foreach` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2804_array_prototype_foreach` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2804_array_prototype_foreach` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2804_array_prototype_foreach` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2804_array_prototype_foreach` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2804_array_prototype_foreach` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2804_array_prototype_foreach` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2804_array_prototype_foreach` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2804_array_prototype_foreach` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2804_array_prototype_foreach` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2804_array_prototype_foreach` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2804_array_prototype_foreach` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2804_array_prototype_foreach` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2804_array_prototype_foreach` |

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
.\scripts\test.ps1 -Folder 2804_array_prototype_foreach -AllLanguages
```

```bash
./scripts/test.sh --folder 2804_array_prototype_foreach --all-languages
```

```zsh
./scripts/test.sh --folder 2804_array_prototype_foreach --all-languages
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
