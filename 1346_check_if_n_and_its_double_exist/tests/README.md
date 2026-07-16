# Test harness for 1346_check_if_n_and_its_double_exist

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language python
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language javascript
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language typescript
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language java
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language cpp
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language c
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language go
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language rust
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language kotlin
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language swift
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language ruby
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language csharp
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language scala
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language php
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm java java 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm c c 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm go go 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm rust rust 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm swift swift 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm scala scala 1346_check_if_n_and_its_double_exist
docker compose -f docker/docker-compose.yml run --rm php php 1346_check_if_n_and_its_double_exist
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1346_check_if_n_and_its_double_exist` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1346_check_if_n_and_its_double_exist` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1346_check_if_n_and_its_double_exist` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1346_check_if_n_and_its_double_exist` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1346_check_if_n_and_its_double_exist` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1346_check_if_n_and_its_double_exist` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1346_check_if_n_and_its_double_exist` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1346_check_if_n_and_its_double_exist` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1346_check_if_n_and_its_double_exist` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1346_check_if_n_and_its_double_exist` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1346_check_if_n_and_its_double_exist` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1346_check_if_n_and_its_double_exist` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1346_check_if_n_and_its_double_exist` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1346_check_if_n_and_its_double_exist` |

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
.\scripts\test.ps1 -Folder 1346_check_if_n_and_its_double_exist -AllLanguages
```

```bash
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --all-languages
```

```zsh
./scripts/test.sh --folder 1346_check_if_n_and_its_double_exist --all-languages
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
