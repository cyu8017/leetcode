# Test harness for 2691_immutability_helper

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2691_immutability_helper -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2691_immutability_helper --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2691_immutability_helper --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2691_immutability_helper --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2691_immutability_helper --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2691_immutability_helper --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2691_immutability_helper --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2691_immutability_helper --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2691_immutability_helper --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2691_immutability_helper --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2691_immutability_helper --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2691_immutability_helper --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2691_immutability_helper --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2691_immutability_helper --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2691_immutability_helper --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2691_immutability_helper --language python
./scripts/test.sh --folder 2691_immutability_helper --language javascript
./scripts/test.sh --folder 2691_immutability_helper --language typescript
./scripts/test.sh --folder 2691_immutability_helper --language java
./scripts/test.sh --folder 2691_immutability_helper --language cpp
./scripts/test.sh --folder 2691_immutability_helper --language c
./scripts/test.sh --folder 2691_immutability_helper --language go
./scripts/test.sh --folder 2691_immutability_helper --language rust
./scripts/test.sh --folder 2691_immutability_helper --language kotlin
./scripts/test.sh --folder 2691_immutability_helper --language swift
./scripts/test.sh --folder 2691_immutability_helper --language ruby
./scripts/test.sh --folder 2691_immutability_helper --language csharp
./scripts/test.sh --folder 2691_immutability_helper --language scala
./scripts/test.sh --folder 2691_immutability_helper --language php
./scripts/test.sh --folder 2691_immutability_helper --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2691_immutability_helper --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2691_immutability_helper --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2691_immutability_helper --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2691_immutability_helper --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2691_immutability_helper --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2691_immutability_helper --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2691_immutability_helper --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2691_immutability_helper --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2691_immutability_helper --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2691_immutability_helper --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2691_immutability_helper --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2691_immutability_helper --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2691_immutability_helper --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2691_immutability_helper --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm java java 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm c c 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm go go 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm rust rust 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm swift swift 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm scala scala 2691_immutability_helper
docker compose -f docker/docker-compose.yml run --rm php php 2691_immutability_helper
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2691_immutability_helper` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2691_immutability_helper` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2691_immutability_helper` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2691_immutability_helper` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2691_immutability_helper` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2691_immutability_helper` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2691_immutability_helper` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2691_immutability_helper` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2691_immutability_helper` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2691_immutability_helper` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2691_immutability_helper` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2691_immutability_helper` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2691_immutability_helper` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2691_immutability_helper` |

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
.\scripts\test.ps1 -Folder 2691_immutability_helper -AllLanguages
```

```bash
./scripts/test.sh --folder 2691_immutability_helper --all-languages
```

```zsh
./scripts/test.sh --folder 2691_immutability_helper --all-languages
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
