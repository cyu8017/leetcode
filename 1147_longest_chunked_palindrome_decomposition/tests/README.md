# Test harness for 1147_longest_chunked_palindrome_decomposition

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language python
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language javascript
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language typescript
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language java
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language cpp
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language c
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language go
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language rust
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language kotlin
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language swift
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language ruby
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language csharp
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language scala
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language php
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm java java 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm c c 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm go go 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm rust rust 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm swift swift 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm scala scala 1147_longest_chunked_palindrome_decomposition
docker compose -f docker/docker-compose.yml run --rm php php 1147_longest_chunked_palindrome_decomposition
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1147_longest_chunked_palindrome_decomposition` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1147_longest_chunked_palindrome_decomposition` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1147_longest_chunked_palindrome_decomposition` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1147_longest_chunked_palindrome_decomposition` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1147_longest_chunked_palindrome_decomposition` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1147_longest_chunked_palindrome_decomposition` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1147_longest_chunked_palindrome_decomposition` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1147_longest_chunked_palindrome_decomposition` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1147_longest_chunked_palindrome_decomposition` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1147_longest_chunked_palindrome_decomposition` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1147_longest_chunked_palindrome_decomposition` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1147_longest_chunked_palindrome_decomposition` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1147_longest_chunked_palindrome_decomposition` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1147_longest_chunked_palindrome_decomposition` |

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
.\scripts\test.ps1 -Folder 1147_longest_chunked_palindrome_decomposition -AllLanguages
```

```bash
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --all-languages
```

```zsh
./scripts/test.sh --folder 1147_longest_chunked_palindrome_decomposition --all-languages
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
