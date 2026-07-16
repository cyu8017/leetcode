# Test harness for 0225_implement_stack_using_queues

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0225_implement_stack_using_queues --language python
./scripts/test.sh --folder 0225_implement_stack_using_queues --language javascript
./scripts/test.sh --folder 0225_implement_stack_using_queues --language typescript
./scripts/test.sh --folder 0225_implement_stack_using_queues --language java
./scripts/test.sh --folder 0225_implement_stack_using_queues --language cpp
./scripts/test.sh --folder 0225_implement_stack_using_queues --language c
./scripts/test.sh --folder 0225_implement_stack_using_queues --language go
./scripts/test.sh --folder 0225_implement_stack_using_queues --language rust
./scripts/test.sh --folder 0225_implement_stack_using_queues --language kotlin
./scripts/test.sh --folder 0225_implement_stack_using_queues --language swift
./scripts/test.sh --folder 0225_implement_stack_using_queues --language ruby
./scripts/test.sh --folder 0225_implement_stack_using_queues --language csharp
./scripts/test.sh --folder 0225_implement_stack_using_queues --language scala
./scripts/test.sh --folder 0225_implement_stack_using_queues --language php
./scripts/test.sh --folder 0225_implement_stack_using_queues --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0225_implement_stack_using_queues --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm java java 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm c c 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm go go 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm rust rust 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm swift swift 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm scala scala 0225_implement_stack_using_queues
docker compose -f docker/docker-compose.yml run --rm php php 0225_implement_stack_using_queues
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0225_implement_stack_using_queues` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0225_implement_stack_using_queues` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0225_implement_stack_using_queues` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0225_implement_stack_using_queues` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0225_implement_stack_using_queues` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0225_implement_stack_using_queues` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0225_implement_stack_using_queues` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0225_implement_stack_using_queues` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0225_implement_stack_using_queues` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0225_implement_stack_using_queues` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0225_implement_stack_using_queues` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0225_implement_stack_using_queues` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0225_implement_stack_using_queues` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0225_implement_stack_using_queues` |

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
.\scripts\test.ps1 -Folder 0225_implement_stack_using_queues -AllLanguages
```

```bash
./scripts/test.sh --folder 0225_implement_stack_using_queues --all-languages
```

```zsh
./scripts/test.sh --folder 0225_implement_stack_using_queues --all-languages
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
