# Test harness for 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language python
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language javascript
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language typescript
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language java
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language cpp
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language c
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language go
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language rust
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language kotlin
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language swift
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language ruby
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language csharp
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language scala
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language php
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm java java 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm c c 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm go go 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm rust rust 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm swift swift 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm scala scala 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
docker compose -f docker/docker-compose.yml run --rm php php 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate` |

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
.\scripts\test.ps1 -Folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate -AllLanguages
```

```bash
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --all-languages
```

```zsh
./scripts/test.sh --folder 1779_find_nearest_point_that_has_the_same_x_or_y_coordinate --all-languages
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
