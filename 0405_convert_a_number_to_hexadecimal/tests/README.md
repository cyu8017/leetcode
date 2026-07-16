# Test harness for 0405_convert_a_number_to_hexadecimal

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language python
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language javascript
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language typescript
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language java
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language cpp
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language c
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language go
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language rust
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language kotlin
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language swift
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language ruby
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language csharp
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language scala
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language php
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm java java 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm c c 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm go go 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm rust rust 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm swift swift 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm scala scala 0405_convert_a_number_to_hexadecimal
docker compose -f docker/docker-compose.yml run --rm php php 0405_convert_a_number_to_hexadecimal
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0405_convert_a_number_to_hexadecimal` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0405_convert_a_number_to_hexadecimal` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0405_convert_a_number_to_hexadecimal` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0405_convert_a_number_to_hexadecimal` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0405_convert_a_number_to_hexadecimal` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0405_convert_a_number_to_hexadecimal` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0405_convert_a_number_to_hexadecimal` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0405_convert_a_number_to_hexadecimal` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0405_convert_a_number_to_hexadecimal` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0405_convert_a_number_to_hexadecimal` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0405_convert_a_number_to_hexadecimal` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0405_convert_a_number_to_hexadecimal` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0405_convert_a_number_to_hexadecimal` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0405_convert_a_number_to_hexadecimal` |

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
.\scripts\test.ps1 -Folder 0405_convert_a_number_to_hexadecimal -AllLanguages
```

```bash
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --all-languages
```

```zsh
./scripts/test.sh --folder 0405_convert_a_number_to_hexadecimal --all-languages
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
