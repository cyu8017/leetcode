# Test harness for 1902_depth_of_bst_given_insertion_order

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language python
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language javascript
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language typescript
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language java
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language cpp
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language c
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language go
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language rust
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language kotlin
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language swift
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language ruby
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language csharp
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language scala
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language php
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm java java 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm c c 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm go go 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm rust rust 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm swift swift 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm scala scala 1902_depth_of_bst_given_insertion_order
docker compose -f docker/docker-compose.yml run --rm php php 1902_depth_of_bst_given_insertion_order
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1902_depth_of_bst_given_insertion_order` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1902_depth_of_bst_given_insertion_order` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1902_depth_of_bst_given_insertion_order` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1902_depth_of_bst_given_insertion_order` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1902_depth_of_bst_given_insertion_order` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1902_depth_of_bst_given_insertion_order` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1902_depth_of_bst_given_insertion_order` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1902_depth_of_bst_given_insertion_order` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1902_depth_of_bst_given_insertion_order` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1902_depth_of_bst_given_insertion_order` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1902_depth_of_bst_given_insertion_order` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1902_depth_of_bst_given_insertion_order` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1902_depth_of_bst_given_insertion_order` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1902_depth_of_bst_given_insertion_order` |

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
.\scripts\test.ps1 -Folder 1902_depth_of_bst_given_insertion_order -AllLanguages
```

```bash
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --all-languages
```

```zsh
./scripts/test.sh --folder 1902_depth_of_bst_given_insertion_order --all-languages
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
