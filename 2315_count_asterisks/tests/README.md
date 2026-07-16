# Test harness for 2315_count_asterisks

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2315_count_asterisks -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2315_count_asterisks --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2315_count_asterisks --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2315_count_asterisks --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2315_count_asterisks --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2315_count_asterisks --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2315_count_asterisks --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2315_count_asterisks --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2315_count_asterisks --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2315_count_asterisks --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2315_count_asterisks --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2315_count_asterisks --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2315_count_asterisks --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2315_count_asterisks --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2315_count_asterisks --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2315_count_asterisks --language python
./scripts/test.sh --folder 2315_count_asterisks --language javascript
./scripts/test.sh --folder 2315_count_asterisks --language typescript
./scripts/test.sh --folder 2315_count_asterisks --language java
./scripts/test.sh --folder 2315_count_asterisks --language cpp
./scripts/test.sh --folder 2315_count_asterisks --language c
./scripts/test.sh --folder 2315_count_asterisks --language go
./scripts/test.sh --folder 2315_count_asterisks --language rust
./scripts/test.sh --folder 2315_count_asterisks --language kotlin
./scripts/test.sh --folder 2315_count_asterisks --language swift
./scripts/test.sh --folder 2315_count_asterisks --language ruby
./scripts/test.sh --folder 2315_count_asterisks --language csharp
./scripts/test.sh --folder 2315_count_asterisks --language scala
./scripts/test.sh --folder 2315_count_asterisks --language php
./scripts/test.sh --folder 2315_count_asterisks --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2315_count_asterisks --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2315_count_asterisks --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2315_count_asterisks --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2315_count_asterisks --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2315_count_asterisks --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2315_count_asterisks --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2315_count_asterisks --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2315_count_asterisks --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2315_count_asterisks --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2315_count_asterisks --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2315_count_asterisks --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2315_count_asterisks --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2315_count_asterisks --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2315_count_asterisks --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm java java 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm c c 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm go go 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm rust rust 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm swift swift 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm scala scala 2315_count_asterisks
docker compose -f docker/docker-compose.yml run --rm php php 2315_count_asterisks
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2315_count_asterisks` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2315_count_asterisks` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2315_count_asterisks` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2315_count_asterisks` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2315_count_asterisks` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2315_count_asterisks` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2315_count_asterisks` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2315_count_asterisks` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2315_count_asterisks` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2315_count_asterisks` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2315_count_asterisks` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2315_count_asterisks` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2315_count_asterisks` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2315_count_asterisks` |

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
.\scripts\test.ps1 -Folder 2315_count_asterisks -AllLanguages
```

```bash
./scripts/test.sh --folder 2315_count_asterisks --all-languages
```

```zsh
./scripts/test.sh --folder 2315_count_asterisks --all-languages
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
