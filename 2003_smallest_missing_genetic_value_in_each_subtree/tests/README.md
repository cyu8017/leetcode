# Test harness for 2003_smallest_missing_genetic_value_in_each_subtree

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language python
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language javascript
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language typescript
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language java
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language cpp
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language c
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language go
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language rust
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language kotlin
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language swift
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language ruby
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language csharp
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language scala
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language php
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm java java 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm c c 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm go go 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm rust rust 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm swift swift 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm scala scala 2003_smallest_missing_genetic_value_in_each_subtree
docker compose -f docker/docker-compose.yml run --rm php php 2003_smallest_missing_genetic_value_in_each_subtree
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2003_smallest_missing_genetic_value_in_each_subtree` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2003_smallest_missing_genetic_value_in_each_subtree` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2003_smallest_missing_genetic_value_in_each_subtree` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2003_smallest_missing_genetic_value_in_each_subtree` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2003_smallest_missing_genetic_value_in_each_subtree` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2003_smallest_missing_genetic_value_in_each_subtree` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2003_smallest_missing_genetic_value_in_each_subtree` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2003_smallest_missing_genetic_value_in_each_subtree` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2003_smallest_missing_genetic_value_in_each_subtree` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2003_smallest_missing_genetic_value_in_each_subtree` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2003_smallest_missing_genetic_value_in_each_subtree` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2003_smallest_missing_genetic_value_in_each_subtree` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2003_smallest_missing_genetic_value_in_each_subtree` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2003_smallest_missing_genetic_value_in_each_subtree` |

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
.\scripts\test.ps1 -Folder 2003_smallest_missing_genetic_value_in_each_subtree -AllLanguages
```

```bash
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --all-languages
```

```zsh
./scripts/test.sh --folder 2003_smallest_missing_genetic_value_in_each_subtree --all-languages
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
