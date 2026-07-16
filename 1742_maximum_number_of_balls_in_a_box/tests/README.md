# Test harness for 1742_maximum_number_of_balls_in_a_box

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language python
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language javascript
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language typescript
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language java
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language cpp
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language c
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language go
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language rust
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language kotlin
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language swift
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language ruby
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language csharp
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language scala
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language php
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm java java 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm c c 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm go go 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm rust rust 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm swift swift 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm scala scala 1742_maximum_number_of_balls_in_a_box
docker compose -f docker/docker-compose.yml run --rm php php 1742_maximum_number_of_balls_in_a_box
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1742_maximum_number_of_balls_in_a_box` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1742_maximum_number_of_balls_in_a_box` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1742_maximum_number_of_balls_in_a_box` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1742_maximum_number_of_balls_in_a_box` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1742_maximum_number_of_balls_in_a_box` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1742_maximum_number_of_balls_in_a_box` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1742_maximum_number_of_balls_in_a_box` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1742_maximum_number_of_balls_in_a_box` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1742_maximum_number_of_balls_in_a_box` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1742_maximum_number_of_balls_in_a_box` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1742_maximum_number_of_balls_in_a_box` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1742_maximum_number_of_balls_in_a_box` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1742_maximum_number_of_balls_in_a_box` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1742_maximum_number_of_balls_in_a_box` |

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
.\scripts\test.ps1 -Folder 1742_maximum_number_of_balls_in_a_box -AllLanguages
```

```bash
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --all-languages
```

```zsh
./scripts/test.sh --folder 1742_maximum_number_of_balls_in_a_box --all-languages
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
