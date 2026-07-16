# Test harness for 0447_number_of_boomerangs

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0447_number_of_boomerangs --language python
./scripts/test.sh --folder 0447_number_of_boomerangs --language javascript
./scripts/test.sh --folder 0447_number_of_boomerangs --language typescript
./scripts/test.sh --folder 0447_number_of_boomerangs --language java
./scripts/test.sh --folder 0447_number_of_boomerangs --language cpp
./scripts/test.sh --folder 0447_number_of_boomerangs --language c
./scripts/test.sh --folder 0447_number_of_boomerangs --language go
./scripts/test.sh --folder 0447_number_of_boomerangs --language rust
./scripts/test.sh --folder 0447_number_of_boomerangs --language kotlin
./scripts/test.sh --folder 0447_number_of_boomerangs --language swift
./scripts/test.sh --folder 0447_number_of_boomerangs --language ruby
./scripts/test.sh --folder 0447_number_of_boomerangs --language csharp
./scripts/test.sh --folder 0447_number_of_boomerangs --language scala
./scripts/test.sh --folder 0447_number_of_boomerangs --language php
./scripts/test.sh --folder 0447_number_of_boomerangs --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0447_number_of_boomerangs --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm java java 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm c c 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm go go 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm rust rust 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm swift swift 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm scala scala 0447_number_of_boomerangs
docker compose -f docker/docker-compose.yml run --rm php php 0447_number_of_boomerangs
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0447_number_of_boomerangs` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0447_number_of_boomerangs` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0447_number_of_boomerangs` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0447_number_of_boomerangs` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0447_number_of_boomerangs` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0447_number_of_boomerangs` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0447_number_of_boomerangs` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0447_number_of_boomerangs` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0447_number_of_boomerangs` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0447_number_of_boomerangs` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0447_number_of_boomerangs` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0447_number_of_boomerangs` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0447_number_of_boomerangs` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0447_number_of_boomerangs` |

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
.\scripts\test.ps1 -Folder 0447_number_of_boomerangs -AllLanguages
```

```bash
./scripts/test.sh --folder 0447_number_of_boomerangs --all-languages
```

```zsh
./scripts/test.sh --folder 0447_number_of_boomerangs --all-languages
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
