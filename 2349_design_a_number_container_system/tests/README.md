# Test harness for 2349_design_a_number_container_system

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2349_design_a_number_container_system --language python
./scripts/test.sh --folder 2349_design_a_number_container_system --language javascript
./scripts/test.sh --folder 2349_design_a_number_container_system --language typescript
./scripts/test.sh --folder 2349_design_a_number_container_system --language java
./scripts/test.sh --folder 2349_design_a_number_container_system --language cpp
./scripts/test.sh --folder 2349_design_a_number_container_system --language c
./scripts/test.sh --folder 2349_design_a_number_container_system --language go
./scripts/test.sh --folder 2349_design_a_number_container_system --language rust
./scripts/test.sh --folder 2349_design_a_number_container_system --language kotlin
./scripts/test.sh --folder 2349_design_a_number_container_system --language swift
./scripts/test.sh --folder 2349_design_a_number_container_system --language ruby
./scripts/test.sh --folder 2349_design_a_number_container_system --language csharp
./scripts/test.sh --folder 2349_design_a_number_container_system --language scala
./scripts/test.sh --folder 2349_design_a_number_container_system --language php
./scripts/test.sh --folder 2349_design_a_number_container_system --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2349_design_a_number_container_system --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm java java 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm c c 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm go go 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm rust rust 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm swift swift 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm scala scala 2349_design_a_number_container_system
docker compose -f docker/docker-compose.yml run --rm php php 2349_design_a_number_container_system
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2349_design_a_number_container_system` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2349_design_a_number_container_system` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2349_design_a_number_container_system` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2349_design_a_number_container_system` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2349_design_a_number_container_system` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2349_design_a_number_container_system` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2349_design_a_number_container_system` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2349_design_a_number_container_system` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2349_design_a_number_container_system` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2349_design_a_number_container_system` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2349_design_a_number_container_system` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2349_design_a_number_container_system` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2349_design_a_number_container_system` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2349_design_a_number_container_system` |

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
.\scripts\test.ps1 -Folder 2349_design_a_number_container_system -AllLanguages
```

```bash
./scripts/test.sh --folder 2349_design_a_number_container_system --all-languages
```

```zsh
./scripts/test.sh --folder 2349_design_a_number_container_system --all-languages
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
