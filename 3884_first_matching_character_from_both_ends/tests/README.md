# Test harness for 3884_first_matching_character_from_both_ends

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language python
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language javascript
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language typescript
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language java
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language cpp
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language c
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language go
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language rust
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language kotlin
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language swift
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language ruby
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language csharp
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language scala
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language php
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm java java 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm c c 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm go go 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm rust rust 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm swift swift 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm scala scala 3884_first_matching_character_from_both_ends
docker compose -f docker/docker-compose.yml run --rm php php 3884_first_matching_character_from_both_ends
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3884_first_matching_character_from_both_ends` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3884_first_matching_character_from_both_ends` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3884_first_matching_character_from_both_ends` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3884_first_matching_character_from_both_ends` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3884_first_matching_character_from_both_ends` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3884_first_matching_character_from_both_ends` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3884_first_matching_character_from_both_ends` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3884_first_matching_character_from_both_ends` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3884_first_matching_character_from_both_ends` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3884_first_matching_character_from_both_ends` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3884_first_matching_character_from_both_ends` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3884_first_matching_character_from_both_ends` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3884_first_matching_character_from_both_ends` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3884_first_matching_character_from_both_ends` |

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
.\scripts\test.ps1 -Folder 3884_first_matching_character_from_both_ends -AllLanguages
```

```bash
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --all-languages
```

```zsh
./scripts/test.sh --folder 3884_first_matching_character_from_both_ends --all-languages
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
