# Test harness for 2250_count_number_of_rectangles_containing_each_point

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language python
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language javascript
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language typescript
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language java
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language cpp
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language c
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language go
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language rust
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language kotlin
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language swift
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language ruby
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language csharp
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language scala
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language php
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm java java 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm c c 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm go go 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm rust rust 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm swift swift 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm scala scala 2250_count_number_of_rectangles_containing_each_point
docker compose -f docker/docker-compose.yml run --rm php php 2250_count_number_of_rectangles_containing_each_point
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2250_count_number_of_rectangles_containing_each_point` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2250_count_number_of_rectangles_containing_each_point` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2250_count_number_of_rectangles_containing_each_point` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2250_count_number_of_rectangles_containing_each_point` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2250_count_number_of_rectangles_containing_each_point` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2250_count_number_of_rectangles_containing_each_point` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2250_count_number_of_rectangles_containing_each_point` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2250_count_number_of_rectangles_containing_each_point` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2250_count_number_of_rectangles_containing_each_point` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2250_count_number_of_rectangles_containing_each_point` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2250_count_number_of_rectangles_containing_each_point` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2250_count_number_of_rectangles_containing_each_point` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2250_count_number_of_rectangles_containing_each_point` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2250_count_number_of_rectangles_containing_each_point` |

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
.\scripts\test.ps1 -Folder 2250_count_number_of_rectangles_containing_each_point -AllLanguages
```

```bash
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --all-languages
```

```zsh
./scripts/test.sh --folder 2250_count_number_of_rectangles_containing_each_point --all-languages
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
