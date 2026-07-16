# Test harness for 2309_greatest_english_letter_in_upper_and_lower_case

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language python
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language javascript
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language typescript
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language java
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language cpp
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language c
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language go
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language rust
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language kotlin
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language swift
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language ruby
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language csharp
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language scala
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language php
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm java java 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm c c 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm go go 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm rust rust 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm swift swift 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm scala scala 2309_greatest_english_letter_in_upper_and_lower_case
docker compose -f docker/docker-compose.yml run --rm php php 2309_greatest_english_letter_in_upper_and_lower_case
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2309_greatest_english_letter_in_upper_and_lower_case` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2309_greatest_english_letter_in_upper_and_lower_case` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2309_greatest_english_letter_in_upper_and_lower_case` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2309_greatest_english_letter_in_upper_and_lower_case` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2309_greatest_english_letter_in_upper_and_lower_case` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2309_greatest_english_letter_in_upper_and_lower_case` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2309_greatest_english_letter_in_upper_and_lower_case` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2309_greatest_english_letter_in_upper_and_lower_case` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2309_greatest_english_letter_in_upper_and_lower_case` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2309_greatest_english_letter_in_upper_and_lower_case` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2309_greatest_english_letter_in_upper_and_lower_case` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2309_greatest_english_letter_in_upper_and_lower_case` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2309_greatest_english_letter_in_upper_and_lower_case` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2309_greatest_english_letter_in_upper_and_lower_case` |

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
.\scripts\test.ps1 -Folder 2309_greatest_english_letter_in_upper_and_lower_case -AllLanguages
```

```bash
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --all-languages
```

```zsh
./scripts/test.sh --folder 2309_greatest_english_letter_in_upper_and_lower_case --all-languages
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
