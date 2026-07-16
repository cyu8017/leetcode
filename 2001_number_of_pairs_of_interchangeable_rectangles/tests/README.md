# Test harness for 2001_number_of_pairs_of_interchangeable_rectangles

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language python
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language javascript
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language typescript
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language java
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language cpp
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language c
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language go
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language rust
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language kotlin
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language swift
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language ruby
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language csharp
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language scala
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language php
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm java java 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm c c 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm go go 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm rust rust 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm swift swift 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm scala scala 2001_number_of_pairs_of_interchangeable_rectangles
docker compose -f docker/docker-compose.yml run --rm php php 2001_number_of_pairs_of_interchangeable_rectangles
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2001_number_of_pairs_of_interchangeable_rectangles` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2001_number_of_pairs_of_interchangeable_rectangles` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2001_number_of_pairs_of_interchangeable_rectangles` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2001_number_of_pairs_of_interchangeable_rectangles` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2001_number_of_pairs_of_interchangeable_rectangles` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2001_number_of_pairs_of_interchangeable_rectangles` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2001_number_of_pairs_of_interchangeable_rectangles` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2001_number_of_pairs_of_interchangeable_rectangles` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2001_number_of_pairs_of_interchangeable_rectangles` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2001_number_of_pairs_of_interchangeable_rectangles` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2001_number_of_pairs_of_interchangeable_rectangles` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2001_number_of_pairs_of_interchangeable_rectangles` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2001_number_of_pairs_of_interchangeable_rectangles` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2001_number_of_pairs_of_interchangeable_rectangles` |

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
.\scripts\test.ps1 -Folder 2001_number_of_pairs_of_interchangeable_rectangles -AllLanguages
```

```bash
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --all-languages
```

```zsh
./scripts/test.sh --folder 2001_number_of_pairs_of_interchangeable_rectangles --all-languages
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
