# Test harness for 3119_maximum_number_of_potholes_that_can_be_fixed

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language python
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language javascript
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language typescript
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language java
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language cpp
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language c
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language go
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language rust
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language kotlin
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language swift
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language ruby
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language csharp
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language scala
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language php
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm java java 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm c c 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm go go 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm rust rust 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm swift swift 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm scala scala 3119_maximum_number_of_potholes_that_can_be_fixed
docker compose -f docker/docker-compose.yml run --rm php php 3119_maximum_number_of_potholes_that_can_be_fixed
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3119_maximum_number_of_potholes_that_can_be_fixed` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3119_maximum_number_of_potholes_that_can_be_fixed` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3119_maximum_number_of_potholes_that_can_be_fixed` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3119_maximum_number_of_potholes_that_can_be_fixed` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3119_maximum_number_of_potholes_that_can_be_fixed` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3119_maximum_number_of_potholes_that_can_be_fixed` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3119_maximum_number_of_potholes_that_can_be_fixed` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3119_maximum_number_of_potholes_that_can_be_fixed` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3119_maximum_number_of_potholes_that_can_be_fixed` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3119_maximum_number_of_potholes_that_can_be_fixed` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3119_maximum_number_of_potholes_that_can_be_fixed` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3119_maximum_number_of_potholes_that_can_be_fixed` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3119_maximum_number_of_potholes_that_can_be_fixed` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3119_maximum_number_of_potholes_that_can_be_fixed` |

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
.\scripts\test.ps1 -Folder 3119_maximum_number_of_potholes_that_can_be_fixed -AllLanguages
```

```bash
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --all-languages
```

```zsh
./scripts/test.sh --folder 3119_maximum_number_of_potholes_that_can_be_fixed --all-languages
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
