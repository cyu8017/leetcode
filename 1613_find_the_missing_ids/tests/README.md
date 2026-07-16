# Test harness for 1613_find_the_missing_ids

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1613_find_the_missing_ids --language python
./scripts/test.sh --folder 1613_find_the_missing_ids --language javascript
./scripts/test.sh --folder 1613_find_the_missing_ids --language typescript
./scripts/test.sh --folder 1613_find_the_missing_ids --language java
./scripts/test.sh --folder 1613_find_the_missing_ids --language cpp
./scripts/test.sh --folder 1613_find_the_missing_ids --language c
./scripts/test.sh --folder 1613_find_the_missing_ids --language go
./scripts/test.sh --folder 1613_find_the_missing_ids --language rust
./scripts/test.sh --folder 1613_find_the_missing_ids --language kotlin
./scripts/test.sh --folder 1613_find_the_missing_ids --language swift
./scripts/test.sh --folder 1613_find_the_missing_ids --language ruby
./scripts/test.sh --folder 1613_find_the_missing_ids --language csharp
./scripts/test.sh --folder 1613_find_the_missing_ids --language scala
./scripts/test.sh --folder 1613_find_the_missing_ids --language php
./scripts/test.sh --folder 1613_find_the_missing_ids --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1613_find_the_missing_ids --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm java java 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm c c 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm go go 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm rust rust 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm swift swift 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm scala scala 1613_find_the_missing_ids
docker compose -f docker/docker-compose.yml run --rm php php 1613_find_the_missing_ids
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1613_find_the_missing_ids` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1613_find_the_missing_ids` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1613_find_the_missing_ids` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1613_find_the_missing_ids` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1613_find_the_missing_ids` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1613_find_the_missing_ids` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1613_find_the_missing_ids` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1613_find_the_missing_ids` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1613_find_the_missing_ids` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1613_find_the_missing_ids` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1613_find_the_missing_ids` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1613_find_the_missing_ids` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1613_find_the_missing_ids` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1613_find_the_missing_ids` |

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
.\scripts\test.ps1 -Folder 1613_find_the_missing_ids -AllLanguages
```

```bash
./scripts/test.sh --folder 1613_find_the_missing_ids --all-languages
```

```zsh
./scripts/test.sh --folder 1613_find_the_missing_ids --all-languages
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
