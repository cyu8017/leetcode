# Test harness for 2821_delay_the_resolution_of_each_promise

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language python
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language javascript
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language typescript
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language java
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language cpp
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language c
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language go
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language rust
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language kotlin
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language swift
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language ruby
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language csharp
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language scala
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language php
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm java java 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm c c 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm go go 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm rust rust 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm swift swift 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm scala scala 2821_delay_the_resolution_of_each_promise
docker compose -f docker/docker-compose.yml run --rm php php 2821_delay_the_resolution_of_each_promise
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2821_delay_the_resolution_of_each_promise` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2821_delay_the_resolution_of_each_promise` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2821_delay_the_resolution_of_each_promise` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2821_delay_the_resolution_of_each_promise` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2821_delay_the_resolution_of_each_promise` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2821_delay_the_resolution_of_each_promise` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2821_delay_the_resolution_of_each_promise` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2821_delay_the_resolution_of_each_promise` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2821_delay_the_resolution_of_each_promise` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2821_delay_the_resolution_of_each_promise` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2821_delay_the_resolution_of_each_promise` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2821_delay_the_resolution_of_each_promise` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2821_delay_the_resolution_of_each_promise` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2821_delay_the_resolution_of_each_promise` |

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
.\scripts\test.ps1 -Folder 2821_delay_the_resolution_of_each_promise -AllLanguages
```

```bash
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --all-languages
```

```zsh
./scripts/test.sh --folder 2821_delay_the_resolution_of_each_promise --all-languages
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
