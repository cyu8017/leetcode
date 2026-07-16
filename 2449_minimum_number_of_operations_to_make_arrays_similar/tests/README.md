# Test harness for 2449_minimum_number_of_operations_to_make_arrays_similar

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language python
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language javascript
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language typescript
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language java
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language cpp
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language c
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language go
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language rust
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language kotlin
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language swift
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language ruby
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language csharp
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language scala
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language php
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm java java 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm c c 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm go go 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm rust rust 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm swift swift 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm scala scala 2449_minimum_number_of_operations_to_make_arrays_similar
docker compose -f docker/docker-compose.yml run --rm php php 2449_minimum_number_of_operations_to_make_arrays_similar
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2449_minimum_number_of_operations_to_make_arrays_similar` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2449_minimum_number_of_operations_to_make_arrays_similar` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2449_minimum_number_of_operations_to_make_arrays_similar` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2449_minimum_number_of_operations_to_make_arrays_similar` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2449_minimum_number_of_operations_to_make_arrays_similar` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2449_minimum_number_of_operations_to_make_arrays_similar` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2449_minimum_number_of_operations_to_make_arrays_similar` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2449_minimum_number_of_operations_to_make_arrays_similar` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2449_minimum_number_of_operations_to_make_arrays_similar` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2449_minimum_number_of_operations_to_make_arrays_similar` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2449_minimum_number_of_operations_to_make_arrays_similar` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2449_minimum_number_of_operations_to_make_arrays_similar` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2449_minimum_number_of_operations_to_make_arrays_similar` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2449_minimum_number_of_operations_to_make_arrays_similar` |

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
.\scripts\test.ps1 -Folder 2449_minimum_number_of_operations_to_make_arrays_similar -AllLanguages
```

```bash
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --all-languages
```

```zsh
./scripts/test.sh --folder 2449_minimum_number_of_operations_to_make_arrays_similar --all-languages
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
