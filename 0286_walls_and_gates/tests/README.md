# Test harness for 0286_walls_and_gates

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0286_walls_and_gates -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0286_walls_and_gates --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0286_walls_and_gates --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0286_walls_and_gates --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0286_walls_and_gates --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0286_walls_and_gates --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0286_walls_and_gates --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0286_walls_and_gates --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0286_walls_and_gates --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0286_walls_and_gates --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0286_walls_and_gates --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0286_walls_and_gates --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0286_walls_and_gates --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0286_walls_and_gates --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0286_walls_and_gates --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0286_walls_and_gates --language python
./scripts/test.sh --folder 0286_walls_and_gates --language javascript
./scripts/test.sh --folder 0286_walls_and_gates --language typescript
./scripts/test.sh --folder 0286_walls_and_gates --language java
./scripts/test.sh --folder 0286_walls_and_gates --language cpp
./scripts/test.sh --folder 0286_walls_and_gates --language c
./scripts/test.sh --folder 0286_walls_and_gates --language go
./scripts/test.sh --folder 0286_walls_and_gates --language rust
./scripts/test.sh --folder 0286_walls_and_gates --language kotlin
./scripts/test.sh --folder 0286_walls_and_gates --language swift
./scripts/test.sh --folder 0286_walls_and_gates --language ruby
./scripts/test.sh --folder 0286_walls_and_gates --language csharp
./scripts/test.sh --folder 0286_walls_and_gates --language scala
./scripts/test.sh --folder 0286_walls_and_gates --language php
./scripts/test.sh --folder 0286_walls_and_gates --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0286_walls_and_gates --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0286_walls_and_gates --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0286_walls_and_gates --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0286_walls_and_gates --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0286_walls_and_gates --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0286_walls_and_gates --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0286_walls_and_gates --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0286_walls_and_gates --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0286_walls_and_gates --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0286_walls_and_gates --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0286_walls_and_gates --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0286_walls_and_gates --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0286_walls_and_gates --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0286_walls_and_gates --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm java java 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm c c 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm go go 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm rust rust 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm swift swift 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm scala scala 0286_walls_and_gates
docker compose -f docker/docker-compose.yml run --rm php php 0286_walls_and_gates
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0286_walls_and_gates` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0286_walls_and_gates` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0286_walls_and_gates` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0286_walls_and_gates` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0286_walls_and_gates` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0286_walls_and_gates` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0286_walls_and_gates` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0286_walls_and_gates` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0286_walls_and_gates` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0286_walls_and_gates` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0286_walls_and_gates` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0286_walls_and_gates` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0286_walls_and_gates` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0286_walls_and_gates` |

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
.\scripts\test.ps1 -Folder 0286_walls_and_gates -AllLanguages
```

```bash
./scripts/test.sh --folder 0286_walls_and_gates --all-languages
```

```zsh
./scripts/test.sh --folder 0286_walls_and_gates --all-languages
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
