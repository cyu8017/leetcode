# Test harness for 1399_count_largest_group

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1399_count_largest_group -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1399_count_largest_group --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1399_count_largest_group --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1399_count_largest_group --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1399_count_largest_group --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1399_count_largest_group --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1399_count_largest_group --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1399_count_largest_group --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1399_count_largest_group --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1399_count_largest_group --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1399_count_largest_group --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1399_count_largest_group --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1399_count_largest_group --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1399_count_largest_group --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1399_count_largest_group --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1399_count_largest_group --language python
./scripts/test.sh --folder 1399_count_largest_group --language javascript
./scripts/test.sh --folder 1399_count_largest_group --language typescript
./scripts/test.sh --folder 1399_count_largest_group --language java
./scripts/test.sh --folder 1399_count_largest_group --language cpp
./scripts/test.sh --folder 1399_count_largest_group --language c
./scripts/test.sh --folder 1399_count_largest_group --language go
./scripts/test.sh --folder 1399_count_largest_group --language rust
./scripts/test.sh --folder 1399_count_largest_group --language kotlin
./scripts/test.sh --folder 1399_count_largest_group --language swift
./scripts/test.sh --folder 1399_count_largest_group --language ruby
./scripts/test.sh --folder 1399_count_largest_group --language csharp
./scripts/test.sh --folder 1399_count_largest_group --language scala
./scripts/test.sh --folder 1399_count_largest_group --language php
./scripts/test.sh --folder 1399_count_largest_group --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1399_count_largest_group --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1399_count_largest_group --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1399_count_largest_group --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1399_count_largest_group --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1399_count_largest_group --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1399_count_largest_group --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1399_count_largest_group --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1399_count_largest_group --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1399_count_largest_group --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1399_count_largest_group --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1399_count_largest_group --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1399_count_largest_group --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1399_count_largest_group --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1399_count_largest_group --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm java java 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm c c 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm go go 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm rust rust 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm swift swift 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm scala scala 1399_count_largest_group
docker compose -f docker/docker-compose.yml run --rm php php 1399_count_largest_group
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1399_count_largest_group` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1399_count_largest_group` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1399_count_largest_group` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1399_count_largest_group` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1399_count_largest_group` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1399_count_largest_group` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1399_count_largest_group` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1399_count_largest_group` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1399_count_largest_group` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1399_count_largest_group` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1399_count_largest_group` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1399_count_largest_group` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1399_count_largest_group` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1399_count_largest_group` |

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
.\scripts\test.ps1 -Folder 1399_count_largest_group -AllLanguages
```

```bash
./scripts/test.sh --folder 1399_count_largest_group --all-languages
```

```zsh
./scripts/test.sh --folder 1399_count_largest_group --all-languages
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
