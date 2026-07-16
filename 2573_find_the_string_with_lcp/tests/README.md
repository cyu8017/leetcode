# Test harness for 2573_find_the_string_with_lcp

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language python
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language javascript
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language typescript
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language java
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language cpp
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language c
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language go
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language rust
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language kotlin
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language swift
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language ruby
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language csharp
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language scala
./scripts/test.sh --folder 2573_find_the_string_with_lcp --language php
./scripts/test.sh --folder 2573_find_the_string_with_lcp --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2573_find_the_string_with_lcp --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm java java 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm c c 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm go go 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm rust rust 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm swift swift 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm scala scala 2573_find_the_string_with_lcp
docker compose -f docker/docker-compose.yml run --rm php php 2573_find_the_string_with_lcp
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2573_find_the_string_with_lcp` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2573_find_the_string_with_lcp` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2573_find_the_string_with_lcp` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2573_find_the_string_with_lcp` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2573_find_the_string_with_lcp` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2573_find_the_string_with_lcp` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2573_find_the_string_with_lcp` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2573_find_the_string_with_lcp` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2573_find_the_string_with_lcp` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2573_find_the_string_with_lcp` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2573_find_the_string_with_lcp` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2573_find_the_string_with_lcp` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2573_find_the_string_with_lcp` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2573_find_the_string_with_lcp` |

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
.\scripts\test.ps1 -Folder 2573_find_the_string_with_lcp -AllLanguages
```

```bash
./scripts/test.sh --folder 2573_find_the_string_with_lcp --all-languages
```

```zsh
./scripts/test.sh --folder 2573_find_the_string_with_lcp --all-languages
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
