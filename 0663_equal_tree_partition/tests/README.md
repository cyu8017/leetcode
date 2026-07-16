# Test harness for 0663_equal_tree_partition

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0663_equal_tree_partition -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0663_equal_tree_partition --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0663_equal_tree_partition --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0663_equal_tree_partition --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0663_equal_tree_partition --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0663_equal_tree_partition --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0663_equal_tree_partition --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0663_equal_tree_partition --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0663_equal_tree_partition --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0663_equal_tree_partition --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0663_equal_tree_partition --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0663_equal_tree_partition --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0663_equal_tree_partition --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0663_equal_tree_partition --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0663_equal_tree_partition --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0663_equal_tree_partition --language python
./scripts/test.sh --folder 0663_equal_tree_partition --language javascript
./scripts/test.sh --folder 0663_equal_tree_partition --language typescript
./scripts/test.sh --folder 0663_equal_tree_partition --language java
./scripts/test.sh --folder 0663_equal_tree_partition --language cpp
./scripts/test.sh --folder 0663_equal_tree_partition --language c
./scripts/test.sh --folder 0663_equal_tree_partition --language go
./scripts/test.sh --folder 0663_equal_tree_partition --language rust
./scripts/test.sh --folder 0663_equal_tree_partition --language kotlin
./scripts/test.sh --folder 0663_equal_tree_partition --language swift
./scripts/test.sh --folder 0663_equal_tree_partition --language ruby
./scripts/test.sh --folder 0663_equal_tree_partition --language csharp
./scripts/test.sh --folder 0663_equal_tree_partition --language scala
./scripts/test.sh --folder 0663_equal_tree_partition --language php
./scripts/test.sh --folder 0663_equal_tree_partition --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0663_equal_tree_partition --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0663_equal_tree_partition --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0663_equal_tree_partition --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0663_equal_tree_partition --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0663_equal_tree_partition --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0663_equal_tree_partition --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0663_equal_tree_partition --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0663_equal_tree_partition --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0663_equal_tree_partition --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0663_equal_tree_partition --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0663_equal_tree_partition --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0663_equal_tree_partition --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0663_equal_tree_partition --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0663_equal_tree_partition --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm java java 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm c c 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm go go 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm rust rust 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm swift swift 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm scala scala 0663_equal_tree_partition
docker compose -f docker/docker-compose.yml run --rm php php 0663_equal_tree_partition
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0663_equal_tree_partition` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0663_equal_tree_partition` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0663_equal_tree_partition` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0663_equal_tree_partition` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0663_equal_tree_partition` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0663_equal_tree_partition` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0663_equal_tree_partition` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0663_equal_tree_partition` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0663_equal_tree_partition` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0663_equal_tree_partition` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0663_equal_tree_partition` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0663_equal_tree_partition` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0663_equal_tree_partition` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0663_equal_tree_partition` |

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
.\scripts\test.ps1 -Folder 0663_equal_tree_partition -AllLanguages
```

```bash
./scripts/test.sh --folder 0663_equal_tree_partition --all-languages
```

```zsh
./scripts/test.sh --folder 0663_equal_tree_partition --all-languages
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
