# Test harness for 1123_lowest_common_ancestor_of_deepest_leaves

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language python
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language javascript
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language typescript
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language java
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language cpp
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language c
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language go
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language rust
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language kotlin
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language swift
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language ruby
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language csharp
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language scala
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language php
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm java java 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm c c 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm go go 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm rust rust 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm swift swift 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm scala scala 1123_lowest_common_ancestor_of_deepest_leaves
docker compose -f docker/docker-compose.yml run --rm php php 1123_lowest_common_ancestor_of_deepest_leaves
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1123_lowest_common_ancestor_of_deepest_leaves` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1123_lowest_common_ancestor_of_deepest_leaves` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1123_lowest_common_ancestor_of_deepest_leaves` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1123_lowest_common_ancestor_of_deepest_leaves` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1123_lowest_common_ancestor_of_deepest_leaves` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1123_lowest_common_ancestor_of_deepest_leaves` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1123_lowest_common_ancestor_of_deepest_leaves` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1123_lowest_common_ancestor_of_deepest_leaves` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1123_lowest_common_ancestor_of_deepest_leaves` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1123_lowest_common_ancestor_of_deepest_leaves` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1123_lowest_common_ancestor_of_deepest_leaves` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1123_lowest_common_ancestor_of_deepest_leaves` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1123_lowest_common_ancestor_of_deepest_leaves` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1123_lowest_common_ancestor_of_deepest_leaves` |

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
.\scripts\test.ps1 -Folder 1123_lowest_common_ancestor_of_deepest_leaves -AllLanguages
```

```bash
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --all-languages
```

```zsh
./scripts/test.sh --folder 1123_lowest_common_ancestor_of_deepest_leaves --all-languages
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
