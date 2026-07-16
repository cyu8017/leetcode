# Test harness for 0200_number_of_islands

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0200_number_of_islands -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0200_number_of_islands --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0200_number_of_islands --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0200_number_of_islands --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0200_number_of_islands --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0200_number_of_islands --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0200_number_of_islands --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0200_number_of_islands --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0200_number_of_islands --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0200_number_of_islands --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0200_number_of_islands --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0200_number_of_islands --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0200_number_of_islands --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0200_number_of_islands --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0200_number_of_islands --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0200_number_of_islands --language python
./scripts/test.sh --folder 0200_number_of_islands --language javascript
./scripts/test.sh --folder 0200_number_of_islands --language typescript
./scripts/test.sh --folder 0200_number_of_islands --language java
./scripts/test.sh --folder 0200_number_of_islands --language cpp
./scripts/test.sh --folder 0200_number_of_islands --language c
./scripts/test.sh --folder 0200_number_of_islands --language go
./scripts/test.sh --folder 0200_number_of_islands --language rust
./scripts/test.sh --folder 0200_number_of_islands --language kotlin
./scripts/test.sh --folder 0200_number_of_islands --language swift
./scripts/test.sh --folder 0200_number_of_islands --language ruby
./scripts/test.sh --folder 0200_number_of_islands --language csharp
./scripts/test.sh --folder 0200_number_of_islands --language scala
./scripts/test.sh --folder 0200_number_of_islands --language php
./scripts/test.sh --folder 0200_number_of_islands --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0200_number_of_islands --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0200_number_of_islands --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0200_number_of_islands --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0200_number_of_islands --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0200_number_of_islands --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0200_number_of_islands --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0200_number_of_islands --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0200_number_of_islands --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0200_number_of_islands --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0200_number_of_islands --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0200_number_of_islands --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0200_number_of_islands --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0200_number_of_islands --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0200_number_of_islands --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm java java 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm c c 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm go go 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm rust rust 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm swift swift 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm scala scala 0200_number_of_islands
docker compose -f docker/docker-compose.yml run --rm php php 0200_number_of_islands
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0200_number_of_islands` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0200_number_of_islands` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0200_number_of_islands` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0200_number_of_islands` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0200_number_of_islands` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0200_number_of_islands` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0200_number_of_islands` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0200_number_of_islands` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0200_number_of_islands` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0200_number_of_islands` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0200_number_of_islands` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0200_number_of_islands` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0200_number_of_islands` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0200_number_of_islands` |

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
.\scripts\test.ps1 -Folder 0200_number_of_islands -AllLanguages
```

```bash
./scripts/test.sh --folder 0200_number_of_islands --all-languages
```

```zsh
./scripts/test.sh --folder 0200_number_of_islands --all-languages
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
