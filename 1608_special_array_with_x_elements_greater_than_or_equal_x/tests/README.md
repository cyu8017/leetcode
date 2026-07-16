# Test harness for 1608_special_array_with_x_elements_greater_than_or_equal_x

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language python
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language javascript
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language typescript
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language java
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language cpp
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language c
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language go
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language rust
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language kotlin
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language swift
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language ruby
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language csharp
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language scala
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language php
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm java java 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm c c 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm go go 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm rust rust 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm swift swift 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm scala scala 1608_special_array_with_x_elements_greater_than_or_equal_x
docker compose -f docker/docker-compose.yml run --rm php php 1608_special_array_with_x_elements_greater_than_or_equal_x
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1608_special_array_with_x_elements_greater_than_or_equal_x` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1608_special_array_with_x_elements_greater_than_or_equal_x` |

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
.\scripts\test.ps1 -Folder 1608_special_array_with_x_elements_greater_than_or_equal_x -AllLanguages
```

```bash
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --all-languages
```

```zsh
./scripts/test.sh --folder 1608_special_array_with_x_elements_greater_than_or_equal_x --all-languages
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
