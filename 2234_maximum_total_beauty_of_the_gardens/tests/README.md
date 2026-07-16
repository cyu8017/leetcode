# Test harness for 2234_maximum_total_beauty_of_the_gardens

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language python
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language javascript
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language typescript
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language java
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language cpp
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language c
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language go
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language rust
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language kotlin
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language swift
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language ruby
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language csharp
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language scala
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language php
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm java java 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm c c 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm go go 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm rust rust 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm swift swift 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm scala scala 2234_maximum_total_beauty_of_the_gardens
docker compose -f docker/docker-compose.yml run --rm php php 2234_maximum_total_beauty_of_the_gardens
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2234_maximum_total_beauty_of_the_gardens` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2234_maximum_total_beauty_of_the_gardens` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2234_maximum_total_beauty_of_the_gardens` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2234_maximum_total_beauty_of_the_gardens` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2234_maximum_total_beauty_of_the_gardens` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2234_maximum_total_beauty_of_the_gardens` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2234_maximum_total_beauty_of_the_gardens` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2234_maximum_total_beauty_of_the_gardens` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2234_maximum_total_beauty_of_the_gardens` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2234_maximum_total_beauty_of_the_gardens` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2234_maximum_total_beauty_of_the_gardens` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2234_maximum_total_beauty_of_the_gardens` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2234_maximum_total_beauty_of_the_gardens` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2234_maximum_total_beauty_of_the_gardens` |

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
.\scripts\test.ps1 -Folder 2234_maximum_total_beauty_of_the_gardens -AllLanguages
```

```bash
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --all-languages
```

```zsh
./scripts/test.sh --folder 2234_maximum_total_beauty_of_the_gardens --all-languages
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
