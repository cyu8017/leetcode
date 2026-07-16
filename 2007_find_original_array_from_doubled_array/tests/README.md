# Test harness for 2007_find_original_array_from_doubled_array

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language python
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language javascript
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language typescript
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language java
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language cpp
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language c
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language go
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language rust
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language kotlin
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language swift
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language ruby
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language csharp
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language scala
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language php
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm java java 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm c c 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm go go 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm rust rust 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm swift swift 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm scala scala 2007_find_original_array_from_doubled_array
docker compose -f docker/docker-compose.yml run --rm php php 2007_find_original_array_from_doubled_array
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2007_find_original_array_from_doubled_array` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2007_find_original_array_from_doubled_array` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2007_find_original_array_from_doubled_array` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2007_find_original_array_from_doubled_array` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2007_find_original_array_from_doubled_array` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2007_find_original_array_from_doubled_array` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2007_find_original_array_from_doubled_array` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2007_find_original_array_from_doubled_array` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2007_find_original_array_from_doubled_array` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2007_find_original_array_from_doubled_array` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2007_find_original_array_from_doubled_array` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2007_find_original_array_from_doubled_array` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2007_find_original_array_from_doubled_array` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2007_find_original_array_from_doubled_array` |

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
.\scripts\test.ps1 -Folder 2007_find_original_array_from_doubled_array -AllLanguages
```

```bash
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --all-languages
```

```zsh
./scripts/test.sh --folder 2007_find_original_array_from_doubled_array --all-languages
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
