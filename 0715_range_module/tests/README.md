# Test harness for 0715_range_module

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0715_range_module -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0715_range_module -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0715_range_module -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0715_range_module -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0715_range_module -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0715_range_module -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0715_range_module -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0715_range_module -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0715_range_module -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0715_range_module -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0715_range_module -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0715_range_module -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0715_range_module -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0715_range_module -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0715_range_module --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0715_range_module --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0715_range_module --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0715_range_module --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0715_range_module --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0715_range_module --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0715_range_module --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0715_range_module --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0715_range_module --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0715_range_module --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0715_range_module --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0715_range_module --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0715_range_module --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0715_range_module --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0715_range_module --language python
./scripts/test.sh --folder 0715_range_module --language javascript
./scripts/test.sh --folder 0715_range_module --language typescript
./scripts/test.sh --folder 0715_range_module --language java
./scripts/test.sh --folder 0715_range_module --language cpp
./scripts/test.sh --folder 0715_range_module --language c
./scripts/test.sh --folder 0715_range_module --language go
./scripts/test.sh --folder 0715_range_module --language rust
./scripts/test.sh --folder 0715_range_module --language kotlin
./scripts/test.sh --folder 0715_range_module --language swift
./scripts/test.sh --folder 0715_range_module --language ruby
./scripts/test.sh --folder 0715_range_module --language csharp
./scripts/test.sh --folder 0715_range_module --language scala
./scripts/test.sh --folder 0715_range_module --language php
./scripts/test.sh --folder 0715_range_module --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0715_range_module --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0715_range_module --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0715_range_module --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0715_range_module --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0715_range_module --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0715_range_module --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0715_range_module --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0715_range_module --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0715_range_module --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0715_range_module --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0715_range_module --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0715_range_module --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0715_range_module --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0715_range_module --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0715_range_module
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0715_range_module
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0715_range_module
docker compose -f docker/docker-compose.yml run --rm java java 0715_range_module
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0715_range_module
docker compose -f docker/docker-compose.yml run --rm c c 0715_range_module
docker compose -f docker/docker-compose.yml run --rm go go 0715_range_module
docker compose -f docker/docker-compose.yml run --rm rust rust 0715_range_module
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0715_range_module
docker compose -f docker/docker-compose.yml run --rm swift swift 0715_range_module
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0715_range_module
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0715_range_module
docker compose -f docker/docker-compose.yml run --rm scala scala 0715_range_module
docker compose -f docker/docker-compose.yml run --rm php php 0715_range_module
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0715_range_module` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0715_range_module` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0715_range_module` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0715_range_module` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0715_range_module` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0715_range_module` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0715_range_module` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0715_range_module` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0715_range_module` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0715_range_module` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0715_range_module` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0715_range_module` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0715_range_module` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0715_range_module` |

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
.\scripts\test.ps1 -Folder 0715_range_module -AllLanguages
```

```bash
./scripts/test.sh --folder 0715_range_module --all-languages
```

```zsh
./scripts/test.sh --folder 0715_range_module --all-languages
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
