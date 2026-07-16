# Test harness for 1994_the_number_of_good_subsets

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language python
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language javascript
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language typescript
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language java
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language cpp
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language c
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language go
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language rust
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language kotlin
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language swift
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language ruby
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language csharp
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language scala
./scripts/test.sh --folder 1994_the_number_of_good_subsets --language php
./scripts/test.sh --folder 1994_the_number_of_good_subsets --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1994_the_number_of_good_subsets --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm java java 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm c c 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm go go 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm rust rust 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm swift swift 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm scala scala 1994_the_number_of_good_subsets
docker compose -f docker/docker-compose.yml run --rm php php 1994_the_number_of_good_subsets
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1994_the_number_of_good_subsets` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1994_the_number_of_good_subsets` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1994_the_number_of_good_subsets` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1994_the_number_of_good_subsets` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1994_the_number_of_good_subsets` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1994_the_number_of_good_subsets` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1994_the_number_of_good_subsets` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1994_the_number_of_good_subsets` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1994_the_number_of_good_subsets` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1994_the_number_of_good_subsets` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1994_the_number_of_good_subsets` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1994_the_number_of_good_subsets` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1994_the_number_of_good_subsets` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1994_the_number_of_good_subsets` |

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
.\scripts\test.ps1 -Folder 1994_the_number_of_good_subsets -AllLanguages
```

```bash
./scripts/test.sh --folder 1994_the_number_of_good_subsets --all-languages
```

```zsh
./scripts/test.sh --folder 1994_the_number_of_good_subsets --all-languages
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
