# Test harness for 1904_the_number_of_full_rounds_you_have_played

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language python
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language javascript
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language typescript
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language java
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language cpp
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language c
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language go
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language rust
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language kotlin
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language swift
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language ruby
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language csharp
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language scala
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language php
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm java java 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm c c 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm go go 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm rust rust 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm swift swift 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm scala scala 1904_the_number_of_full_rounds_you_have_played
docker compose -f docker/docker-compose.yml run --rm php php 1904_the_number_of_full_rounds_you_have_played
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1904_the_number_of_full_rounds_you_have_played` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1904_the_number_of_full_rounds_you_have_played` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1904_the_number_of_full_rounds_you_have_played` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1904_the_number_of_full_rounds_you_have_played` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1904_the_number_of_full_rounds_you_have_played` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1904_the_number_of_full_rounds_you_have_played` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1904_the_number_of_full_rounds_you_have_played` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1904_the_number_of_full_rounds_you_have_played` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1904_the_number_of_full_rounds_you_have_played` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1904_the_number_of_full_rounds_you_have_played` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1904_the_number_of_full_rounds_you_have_played` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1904_the_number_of_full_rounds_you_have_played` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1904_the_number_of_full_rounds_you_have_played` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1904_the_number_of_full_rounds_you_have_played` |

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
.\scripts\test.ps1 -Folder 1904_the_number_of_full_rounds_you_have_played -AllLanguages
```

```bash
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --all-languages
```

```zsh
./scripts/test.sh --folder 1904_the_number_of_full_rounds_you_have_played --all-languages
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
