# Test harness for 2502_design_memory_allocator

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2502_design_memory_allocator -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2502_design_memory_allocator --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2502_design_memory_allocator --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2502_design_memory_allocator --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2502_design_memory_allocator --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2502_design_memory_allocator --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2502_design_memory_allocator --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2502_design_memory_allocator --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2502_design_memory_allocator --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2502_design_memory_allocator --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2502_design_memory_allocator --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2502_design_memory_allocator --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2502_design_memory_allocator --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2502_design_memory_allocator --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2502_design_memory_allocator --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2502_design_memory_allocator --language python
./scripts/test.sh --folder 2502_design_memory_allocator --language javascript
./scripts/test.sh --folder 2502_design_memory_allocator --language typescript
./scripts/test.sh --folder 2502_design_memory_allocator --language java
./scripts/test.sh --folder 2502_design_memory_allocator --language cpp
./scripts/test.sh --folder 2502_design_memory_allocator --language c
./scripts/test.sh --folder 2502_design_memory_allocator --language go
./scripts/test.sh --folder 2502_design_memory_allocator --language rust
./scripts/test.sh --folder 2502_design_memory_allocator --language kotlin
./scripts/test.sh --folder 2502_design_memory_allocator --language swift
./scripts/test.sh --folder 2502_design_memory_allocator --language ruby
./scripts/test.sh --folder 2502_design_memory_allocator --language csharp
./scripts/test.sh --folder 2502_design_memory_allocator --language scala
./scripts/test.sh --folder 2502_design_memory_allocator --language php
./scripts/test.sh --folder 2502_design_memory_allocator --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2502_design_memory_allocator --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2502_design_memory_allocator --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2502_design_memory_allocator --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2502_design_memory_allocator --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2502_design_memory_allocator --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2502_design_memory_allocator --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2502_design_memory_allocator --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2502_design_memory_allocator --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2502_design_memory_allocator --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2502_design_memory_allocator --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2502_design_memory_allocator --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2502_design_memory_allocator --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2502_design_memory_allocator --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2502_design_memory_allocator --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm java java 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm c c 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm go go 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm rust rust 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm swift swift 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm scala scala 2502_design_memory_allocator
docker compose -f docker/docker-compose.yml run --rm php php 2502_design_memory_allocator
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2502_design_memory_allocator` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2502_design_memory_allocator` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2502_design_memory_allocator` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2502_design_memory_allocator` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2502_design_memory_allocator` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2502_design_memory_allocator` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2502_design_memory_allocator` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2502_design_memory_allocator` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2502_design_memory_allocator` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2502_design_memory_allocator` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2502_design_memory_allocator` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2502_design_memory_allocator` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2502_design_memory_allocator` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2502_design_memory_allocator` |

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
.\scripts\test.ps1 -Folder 2502_design_memory_allocator -AllLanguages
```

```bash
./scripts/test.sh --folder 2502_design_memory_allocator --all-languages
```

```zsh
./scripts/test.sh --folder 2502_design_memory_allocator --all-languages
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
