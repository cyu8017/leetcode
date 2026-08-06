# Test harness for 3999_minimum_number_of_string_groups_through_transformations

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language python
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language javascript
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language typescript
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language java
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language cpp
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language c
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language go
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language rust
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language kotlin
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language swift
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language ruby
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language csharp
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language scala
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language php
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm java java 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm c c 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm go go 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm rust rust 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm swift swift 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm scala scala 3999_minimum_number_of_string_groups_through_transformations
docker compose -f docker/docker-compose.yml run --rm php php 3999_minimum_number_of_string_groups_through_transformations
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3999_minimum_number_of_string_groups_through_transformations` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3999_minimum_number_of_string_groups_through_transformations` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3999_minimum_number_of_string_groups_through_transformations` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3999_minimum_number_of_string_groups_through_transformations` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3999_minimum_number_of_string_groups_through_transformations` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3999_minimum_number_of_string_groups_through_transformations` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3999_minimum_number_of_string_groups_through_transformations` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3999_minimum_number_of_string_groups_through_transformations` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3999_minimum_number_of_string_groups_through_transformations` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3999_minimum_number_of_string_groups_through_transformations` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3999_minimum_number_of_string_groups_through_transformations` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3999_minimum_number_of_string_groups_through_transformations` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3999_minimum_number_of_string_groups_through_transformations` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3999_minimum_number_of_string_groups_through_transformations` |

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
.\scripts\test.ps1 -Folder 3999_minimum_number_of_string_groups_through_transformations -AllLanguages
```

```bash
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --all-languages
```

```zsh
./scripts/test.sh --folder 3999_minimum_number_of_string_groups_through_transformations --all-languages
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
