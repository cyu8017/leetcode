# Test harness for 3327_check_if_dfs_strings_are_palindromes

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language python
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language javascript
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language typescript
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language java
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language cpp
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language c
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language go
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language rust
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language kotlin
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language swift
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language ruby
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language csharp
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language scala
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language php
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm java java 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm c c 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm go go 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm rust rust 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm swift swift 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm scala scala 3327_check_if_dfs_strings_are_palindromes
docker compose -f docker/docker-compose.yml run --rm php php 3327_check_if_dfs_strings_are_palindromes
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3327_check_if_dfs_strings_are_palindromes` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3327_check_if_dfs_strings_are_palindromes` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3327_check_if_dfs_strings_are_palindromes` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3327_check_if_dfs_strings_are_palindromes` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3327_check_if_dfs_strings_are_palindromes` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3327_check_if_dfs_strings_are_palindromes` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3327_check_if_dfs_strings_are_palindromes` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3327_check_if_dfs_strings_are_palindromes` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3327_check_if_dfs_strings_are_palindromes` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3327_check_if_dfs_strings_are_palindromes` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3327_check_if_dfs_strings_are_palindromes` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3327_check_if_dfs_strings_are_palindromes` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3327_check_if_dfs_strings_are_palindromes` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3327_check_if_dfs_strings_are_palindromes` |

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
.\scripts\test.ps1 -Folder 3327_check_if_dfs_strings_are_palindromes -AllLanguages
```

```bash
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --all-languages
```

```zsh
./scripts/test.sh --folder 3327_check_if_dfs_strings_are_palindromes --all-languages
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
