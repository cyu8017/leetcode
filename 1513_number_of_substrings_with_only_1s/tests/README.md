# Test harness for 1513_number_of_substrings_with_only_1s

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language python
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language javascript
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language typescript
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language java
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language cpp
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language c
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language go
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language rust
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language kotlin
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language swift
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language ruby
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language csharp
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language scala
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language php
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm java java 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm c c 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm go go 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm rust rust 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm swift swift 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm scala scala 1513_number_of_substrings_with_only_1s
docker compose -f docker/docker-compose.yml run --rm php php 1513_number_of_substrings_with_only_1s
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1513_number_of_substrings_with_only_1s` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1513_number_of_substrings_with_only_1s` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1513_number_of_substrings_with_only_1s` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1513_number_of_substrings_with_only_1s` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1513_number_of_substrings_with_only_1s` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1513_number_of_substrings_with_only_1s` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1513_number_of_substrings_with_only_1s` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1513_number_of_substrings_with_only_1s` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1513_number_of_substrings_with_only_1s` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1513_number_of_substrings_with_only_1s` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1513_number_of_substrings_with_only_1s` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1513_number_of_substrings_with_only_1s` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1513_number_of_substrings_with_only_1s` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1513_number_of_substrings_with_only_1s` |

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
.\scripts\test.ps1 -Folder 1513_number_of_substrings_with_only_1s -AllLanguages
```

```bash
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --all-languages
```

```zsh
./scripts/test.sh --folder 1513_number_of_substrings_with_only_1s --all-languages
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
