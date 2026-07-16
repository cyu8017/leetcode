# Test harness for 1990_count_the_number_of_experiments

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language python
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language javascript
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language typescript
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language java
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language cpp
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language c
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language go
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language rust
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language kotlin
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language swift
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language ruby
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language csharp
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language scala
./scripts/test.sh --folder 1990_count_the_number_of_experiments --language php
./scripts/test.sh --folder 1990_count_the_number_of_experiments --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1990_count_the_number_of_experiments --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm java java 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm c c 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm go go 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm rust rust 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm swift swift 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm scala scala 1990_count_the_number_of_experiments
docker compose -f docker/docker-compose.yml run --rm php php 1990_count_the_number_of_experiments
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1990_count_the_number_of_experiments` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1990_count_the_number_of_experiments` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1990_count_the_number_of_experiments` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1990_count_the_number_of_experiments` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1990_count_the_number_of_experiments` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1990_count_the_number_of_experiments` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1990_count_the_number_of_experiments` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1990_count_the_number_of_experiments` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1990_count_the_number_of_experiments` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1990_count_the_number_of_experiments` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1990_count_the_number_of_experiments` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1990_count_the_number_of_experiments` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1990_count_the_number_of_experiments` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1990_count_the_number_of_experiments` |

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
.\scripts\test.ps1 -Folder 1990_count_the_number_of_experiments -AllLanguages
```

```bash
./scripts/test.sh --folder 1990_count_the_number_of_experiments --all-languages
```

```zsh
./scripts/test.sh --folder 1990_count_the_number_of_experiments --all-languages
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
