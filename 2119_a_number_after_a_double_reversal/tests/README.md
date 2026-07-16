# Test harness for 2119_a_number_after_a_double_reversal

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language python
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language javascript
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language typescript
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language java
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language cpp
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language c
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language go
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language rust
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language kotlin
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language swift
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language ruby
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language csharp
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language scala
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language php
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm java java 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm c c 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm go go 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm rust rust 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm swift swift 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm scala scala 2119_a_number_after_a_double_reversal
docker compose -f docker/docker-compose.yml run --rm php php 2119_a_number_after_a_double_reversal
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2119_a_number_after_a_double_reversal` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2119_a_number_after_a_double_reversal` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2119_a_number_after_a_double_reversal` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2119_a_number_after_a_double_reversal` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2119_a_number_after_a_double_reversal` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2119_a_number_after_a_double_reversal` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2119_a_number_after_a_double_reversal` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2119_a_number_after_a_double_reversal` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2119_a_number_after_a_double_reversal` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2119_a_number_after_a_double_reversal` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2119_a_number_after_a_double_reversal` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2119_a_number_after_a_double_reversal` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2119_a_number_after_a_double_reversal` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2119_a_number_after_a_double_reversal` |

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
.\scripts\test.ps1 -Folder 2119_a_number_after_a_double_reversal -AllLanguages
```

```bash
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --all-languages
```

```zsh
./scripts/test.sh --folder 2119_a_number_after_a_double_reversal --all-languages
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
