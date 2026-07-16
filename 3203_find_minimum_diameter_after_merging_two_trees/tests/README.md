# Test harness for 3203_find_minimum_diameter_after_merging_two_trees

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language python
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language javascript
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language typescript
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language java
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language cpp
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language c
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language go
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language rust
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language kotlin
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language swift
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language ruby
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language csharp
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language scala
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language php
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm java java 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm c c 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm go go 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm rust rust 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm swift swift 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm scala scala 3203_find_minimum_diameter_after_merging_two_trees
docker compose -f docker/docker-compose.yml run --rm php php 3203_find_minimum_diameter_after_merging_two_trees
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3203_find_minimum_diameter_after_merging_two_trees` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3203_find_minimum_diameter_after_merging_two_trees` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3203_find_minimum_diameter_after_merging_two_trees` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3203_find_minimum_diameter_after_merging_two_trees` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3203_find_minimum_diameter_after_merging_two_trees` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3203_find_minimum_diameter_after_merging_two_trees` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3203_find_minimum_diameter_after_merging_two_trees` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3203_find_minimum_diameter_after_merging_two_trees` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3203_find_minimum_diameter_after_merging_two_trees` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3203_find_minimum_diameter_after_merging_two_trees` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3203_find_minimum_diameter_after_merging_two_trees` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3203_find_minimum_diameter_after_merging_two_trees` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3203_find_minimum_diameter_after_merging_two_trees` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3203_find_minimum_diameter_after_merging_two_trees` |

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
.\scripts\test.ps1 -Folder 3203_find_minimum_diameter_after_merging_two_trees -AllLanguages
```

```bash
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --all-languages
```

```zsh
./scripts/test.sh --folder 3203_find_minimum_diameter_after_merging_two_trees --all-languages
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
