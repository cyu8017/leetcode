# Test harness for 3527_find_the_most_common_response

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3527_find_the_most_common_response --language python
./scripts/test.sh --folder 3527_find_the_most_common_response --language javascript
./scripts/test.sh --folder 3527_find_the_most_common_response --language typescript
./scripts/test.sh --folder 3527_find_the_most_common_response --language java
./scripts/test.sh --folder 3527_find_the_most_common_response --language cpp
./scripts/test.sh --folder 3527_find_the_most_common_response --language c
./scripts/test.sh --folder 3527_find_the_most_common_response --language go
./scripts/test.sh --folder 3527_find_the_most_common_response --language rust
./scripts/test.sh --folder 3527_find_the_most_common_response --language kotlin
./scripts/test.sh --folder 3527_find_the_most_common_response --language swift
./scripts/test.sh --folder 3527_find_the_most_common_response --language ruby
./scripts/test.sh --folder 3527_find_the_most_common_response --language csharp
./scripts/test.sh --folder 3527_find_the_most_common_response --language scala
./scripts/test.sh --folder 3527_find_the_most_common_response --language php
./scripts/test.sh --folder 3527_find_the_most_common_response --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3527_find_the_most_common_response --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm java java 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm c c 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm go go 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm rust rust 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm swift swift 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm scala scala 3527_find_the_most_common_response
docker compose -f docker/docker-compose.yml run --rm php php 3527_find_the_most_common_response
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3527_find_the_most_common_response` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3527_find_the_most_common_response` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3527_find_the_most_common_response` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3527_find_the_most_common_response` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3527_find_the_most_common_response` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3527_find_the_most_common_response` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3527_find_the_most_common_response` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3527_find_the_most_common_response` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3527_find_the_most_common_response` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3527_find_the_most_common_response` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3527_find_the_most_common_response` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3527_find_the_most_common_response` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3527_find_the_most_common_response` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3527_find_the_most_common_response` |

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
.\scripts\test.ps1 -Folder 3527_find_the_most_common_response -AllLanguages
```

```bash
./scripts/test.sh --folder 3527_find_the_most_common_response --all-languages
```

```zsh
./scripts/test.sh --folder 3527_find_the_most_common_response --all-languages
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
