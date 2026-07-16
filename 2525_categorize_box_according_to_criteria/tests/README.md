# Test harness for 2525_categorize_box_according_to_criteria

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language python
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language javascript
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language typescript
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language java
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language cpp
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language c
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language go
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language rust
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language kotlin
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language swift
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language ruby
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language csharp
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language scala
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language php
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm java java 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm c c 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm go go 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm rust rust 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm swift swift 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm scala scala 2525_categorize_box_according_to_criteria
docker compose -f docker/docker-compose.yml run --rm php php 2525_categorize_box_according_to_criteria
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2525_categorize_box_according_to_criteria` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2525_categorize_box_according_to_criteria` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2525_categorize_box_according_to_criteria` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2525_categorize_box_according_to_criteria` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2525_categorize_box_according_to_criteria` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2525_categorize_box_according_to_criteria` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2525_categorize_box_according_to_criteria` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2525_categorize_box_according_to_criteria` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2525_categorize_box_according_to_criteria` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2525_categorize_box_according_to_criteria` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2525_categorize_box_according_to_criteria` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2525_categorize_box_according_to_criteria` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2525_categorize_box_according_to_criteria` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2525_categorize_box_according_to_criteria` |

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
.\scripts\test.ps1 -Folder 2525_categorize_box_according_to_criteria -AllLanguages
```

```bash
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --all-languages
```

```zsh
./scripts/test.sh --folder 2525_categorize_box_according_to_criteria --all-languages
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
