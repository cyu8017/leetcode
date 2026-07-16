# Test harness for 2743_count_substrings_without_repeating_character

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language python
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language javascript
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language typescript
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language java
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language cpp
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language c
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language go
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language rust
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language kotlin
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language swift
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language ruby
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language csharp
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language scala
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language php
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm java java 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm c c 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm go go 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm rust rust 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm swift swift 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm scala scala 2743_count_substrings_without_repeating_character
docker compose -f docker/docker-compose.yml run --rm php php 2743_count_substrings_without_repeating_character
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2743_count_substrings_without_repeating_character` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2743_count_substrings_without_repeating_character` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2743_count_substrings_without_repeating_character` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2743_count_substrings_without_repeating_character` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2743_count_substrings_without_repeating_character` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2743_count_substrings_without_repeating_character` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2743_count_substrings_without_repeating_character` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2743_count_substrings_without_repeating_character` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2743_count_substrings_without_repeating_character` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2743_count_substrings_without_repeating_character` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2743_count_substrings_without_repeating_character` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2743_count_substrings_without_repeating_character` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2743_count_substrings_without_repeating_character` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2743_count_substrings_without_repeating_character` |

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
.\scripts\test.ps1 -Folder 2743_count_substrings_without_repeating_character -AllLanguages
```

```bash
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --all-languages
```

```zsh
./scripts/test.sh --folder 2743_count_substrings_without_repeating_character --all-languages
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
