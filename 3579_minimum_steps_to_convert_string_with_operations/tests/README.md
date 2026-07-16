# Test harness for 3579_minimum_steps_to_convert_string_with_operations

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language python
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language javascript
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language typescript
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language java
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language cpp
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language c
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language go
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language rust
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language kotlin
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language swift
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language ruby
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language csharp
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language scala
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language php
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm java java 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm c c 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm go go 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm rust rust 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm swift swift 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm scala scala 3579_minimum_steps_to_convert_string_with_operations
docker compose -f docker/docker-compose.yml run --rm php php 3579_minimum_steps_to_convert_string_with_operations
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3579_minimum_steps_to_convert_string_with_operations` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3579_minimum_steps_to_convert_string_with_operations` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3579_minimum_steps_to_convert_string_with_operations` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3579_minimum_steps_to_convert_string_with_operations` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3579_minimum_steps_to_convert_string_with_operations` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3579_minimum_steps_to_convert_string_with_operations` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3579_minimum_steps_to_convert_string_with_operations` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3579_minimum_steps_to_convert_string_with_operations` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3579_minimum_steps_to_convert_string_with_operations` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3579_minimum_steps_to_convert_string_with_operations` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3579_minimum_steps_to_convert_string_with_operations` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3579_minimum_steps_to_convert_string_with_operations` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3579_minimum_steps_to_convert_string_with_operations` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3579_minimum_steps_to_convert_string_with_operations` |

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
.\scripts\test.ps1 -Folder 3579_minimum_steps_to_convert_string_with_operations -AllLanguages
```

```bash
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --all-languages
```

```zsh
./scripts/test.sh --folder 3579_minimum_steps_to_convert_string_with_operations --all-languages
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
