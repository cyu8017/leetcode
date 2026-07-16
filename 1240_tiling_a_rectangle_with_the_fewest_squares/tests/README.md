# Test harness for 1240_tiling_a_rectangle_with_the_fewest_squares

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language python
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language javascript
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language typescript
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language java
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language cpp
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language c
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language go
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language rust
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language kotlin
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language swift
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language ruby
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language csharp
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language scala
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language php
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm java java 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm c c 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm go go 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm rust rust 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm swift swift 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm scala scala 1240_tiling_a_rectangle_with_the_fewest_squares
docker compose -f docker/docker-compose.yml run --rm php php 1240_tiling_a_rectangle_with_the_fewest_squares
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1240_tiling_a_rectangle_with_the_fewest_squares` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1240_tiling_a_rectangle_with_the_fewest_squares` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1240_tiling_a_rectangle_with_the_fewest_squares` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1240_tiling_a_rectangle_with_the_fewest_squares` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1240_tiling_a_rectangle_with_the_fewest_squares` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1240_tiling_a_rectangle_with_the_fewest_squares` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1240_tiling_a_rectangle_with_the_fewest_squares` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1240_tiling_a_rectangle_with_the_fewest_squares` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1240_tiling_a_rectangle_with_the_fewest_squares` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1240_tiling_a_rectangle_with_the_fewest_squares` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1240_tiling_a_rectangle_with_the_fewest_squares` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1240_tiling_a_rectangle_with_the_fewest_squares` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1240_tiling_a_rectangle_with_the_fewest_squares` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1240_tiling_a_rectangle_with_the_fewest_squares` |

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
.\scripts\test.ps1 -Folder 1240_tiling_a_rectangle_with_the_fewest_squares -AllLanguages
```

```bash
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --all-languages
```

```zsh
./scripts/test.sh --folder 1240_tiling_a_rectangle_with_the_fewest_squares --all-languages
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
