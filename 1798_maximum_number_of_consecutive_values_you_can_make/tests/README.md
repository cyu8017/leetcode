# Test harness for 1798_maximum_number_of_consecutive_values_you_can_make

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language python
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language javascript
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language typescript
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language java
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language cpp
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language c
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language go
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language rust
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language kotlin
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language swift
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language ruby
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language csharp
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language scala
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language php
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm java java 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm c c 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm go go 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm rust rust 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm swift swift 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm scala scala 1798_maximum_number_of_consecutive_values_you_can_make
docker compose -f docker/docker-compose.yml run --rm php php 1798_maximum_number_of_consecutive_values_you_can_make
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1798_maximum_number_of_consecutive_values_you_can_make` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1798_maximum_number_of_consecutive_values_you_can_make` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1798_maximum_number_of_consecutive_values_you_can_make` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1798_maximum_number_of_consecutive_values_you_can_make` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1798_maximum_number_of_consecutive_values_you_can_make` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1798_maximum_number_of_consecutive_values_you_can_make` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1798_maximum_number_of_consecutive_values_you_can_make` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1798_maximum_number_of_consecutive_values_you_can_make` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1798_maximum_number_of_consecutive_values_you_can_make` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1798_maximum_number_of_consecutive_values_you_can_make` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1798_maximum_number_of_consecutive_values_you_can_make` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1798_maximum_number_of_consecutive_values_you_can_make` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1798_maximum_number_of_consecutive_values_you_can_make` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1798_maximum_number_of_consecutive_values_you_can_make` |

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
.\scripts\test.ps1 -Folder 1798_maximum_number_of_consecutive_values_you_can_make -AllLanguages
```

```bash
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --all-languages
```

```zsh
./scripts/test.sh --folder 1798_maximum_number_of_consecutive_values_you_can_make --all-languages
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
