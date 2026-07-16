# Test harness for 0155_min_stack

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0155_min_stack -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0155_min_stack --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0155_min_stack --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0155_min_stack --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0155_min_stack --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0155_min_stack --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0155_min_stack --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0155_min_stack --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0155_min_stack --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0155_min_stack --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0155_min_stack --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0155_min_stack --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0155_min_stack --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0155_min_stack --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0155_min_stack --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0155_min_stack --language python
./scripts/test.sh --folder 0155_min_stack --language javascript
./scripts/test.sh --folder 0155_min_stack --language typescript
./scripts/test.sh --folder 0155_min_stack --language java
./scripts/test.sh --folder 0155_min_stack --language cpp
./scripts/test.sh --folder 0155_min_stack --language c
./scripts/test.sh --folder 0155_min_stack --language go
./scripts/test.sh --folder 0155_min_stack --language rust
./scripts/test.sh --folder 0155_min_stack --language kotlin
./scripts/test.sh --folder 0155_min_stack --language swift
./scripts/test.sh --folder 0155_min_stack --language ruby
./scripts/test.sh --folder 0155_min_stack --language csharp
./scripts/test.sh --folder 0155_min_stack --language scala
./scripts/test.sh --folder 0155_min_stack --language php
./scripts/test.sh --folder 0155_min_stack --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0155_min_stack --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0155_min_stack --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0155_min_stack --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0155_min_stack --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0155_min_stack --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0155_min_stack --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0155_min_stack --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0155_min_stack --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0155_min_stack --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0155_min_stack --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0155_min_stack --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0155_min_stack --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0155_min_stack --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0155_min_stack --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm java java 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm c c 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm go go 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm rust rust 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm swift swift 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm scala scala 0155_min_stack
docker compose -f docker/docker-compose.yml run --rm php php 0155_min_stack
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0155_min_stack` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0155_min_stack` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0155_min_stack` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0155_min_stack` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0155_min_stack` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0155_min_stack` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0155_min_stack` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0155_min_stack` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0155_min_stack` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0155_min_stack` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0155_min_stack` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0155_min_stack` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0155_min_stack` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0155_min_stack` |

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
.\scripts\test.ps1 -Folder 0155_min_stack -AllLanguages
```

```bash
./scripts/test.sh --folder 0155_min_stack --all-languages
```

```zsh
./scripts/test.sh --folder 0155_min_stack --all-languages
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
