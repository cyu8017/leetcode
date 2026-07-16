# Test harness for 3922_minimum_flips_to_make_binary_string_coherent

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language python
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language javascript
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language typescript
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language java
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language cpp
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language c
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language go
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language rust
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language kotlin
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language swift
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language ruby
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language csharp
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language scala
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language php
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm java java 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm c c 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm go go 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm rust rust 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm swift swift 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm scala scala 3922_minimum_flips_to_make_binary_string_coherent
docker compose -f docker/docker-compose.yml run --rm php php 3922_minimum_flips_to_make_binary_string_coherent
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3922_minimum_flips_to_make_binary_string_coherent` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3922_minimum_flips_to_make_binary_string_coherent` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3922_minimum_flips_to_make_binary_string_coherent` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3922_minimum_flips_to_make_binary_string_coherent` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3922_minimum_flips_to_make_binary_string_coherent` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3922_minimum_flips_to_make_binary_string_coherent` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3922_minimum_flips_to_make_binary_string_coherent` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3922_minimum_flips_to_make_binary_string_coherent` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3922_minimum_flips_to_make_binary_string_coherent` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3922_minimum_flips_to_make_binary_string_coherent` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3922_minimum_flips_to_make_binary_string_coherent` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3922_minimum_flips_to_make_binary_string_coherent` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3922_minimum_flips_to_make_binary_string_coherent` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3922_minimum_flips_to_make_binary_string_coherent` |

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
.\scripts\test.ps1 -Folder 3922_minimum_flips_to_make_binary_string_coherent -AllLanguages
```

```bash
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --all-languages
```

```zsh
./scripts/test.sh --folder 3922_minimum_flips_to_make_binary_string_coherent --all-languages
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
