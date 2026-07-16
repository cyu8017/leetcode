# Test harness for 1016_binary_string_with_substrings_representing_1_to_n

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language python
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language javascript
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language typescript
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language java
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language cpp
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language c
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language go
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language rust
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language kotlin
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language swift
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language ruby
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language csharp
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language scala
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language php
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm java java 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm c c 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm go go 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm rust rust 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm swift swift 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm scala scala 1016_binary_string_with_substrings_representing_1_to_n
docker compose -f docker/docker-compose.yml run --rm php php 1016_binary_string_with_substrings_representing_1_to_n
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1016_binary_string_with_substrings_representing_1_to_n` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1016_binary_string_with_substrings_representing_1_to_n` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1016_binary_string_with_substrings_representing_1_to_n` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1016_binary_string_with_substrings_representing_1_to_n` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1016_binary_string_with_substrings_representing_1_to_n` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1016_binary_string_with_substrings_representing_1_to_n` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1016_binary_string_with_substrings_representing_1_to_n` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1016_binary_string_with_substrings_representing_1_to_n` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1016_binary_string_with_substrings_representing_1_to_n` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1016_binary_string_with_substrings_representing_1_to_n` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1016_binary_string_with_substrings_representing_1_to_n` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1016_binary_string_with_substrings_representing_1_to_n` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1016_binary_string_with_substrings_representing_1_to_n` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1016_binary_string_with_substrings_representing_1_to_n` |

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
.\scripts\test.ps1 -Folder 1016_binary_string_with_substrings_representing_1_to_n -AllLanguages
```

```bash
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --all-languages
```

```zsh
./scripts/test.sh --folder 1016_binary_string_with_substrings_representing_1_to_n --all-languages
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
