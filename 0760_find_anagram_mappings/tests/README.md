# Test harness for 0760_find_anagram_mappings

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0760_find_anagram_mappings --language python
./scripts/test.sh --folder 0760_find_anagram_mappings --language javascript
./scripts/test.sh --folder 0760_find_anagram_mappings --language typescript
./scripts/test.sh --folder 0760_find_anagram_mappings --language java
./scripts/test.sh --folder 0760_find_anagram_mappings --language cpp
./scripts/test.sh --folder 0760_find_anagram_mappings --language c
./scripts/test.sh --folder 0760_find_anagram_mappings --language go
./scripts/test.sh --folder 0760_find_anagram_mappings --language rust
./scripts/test.sh --folder 0760_find_anagram_mappings --language kotlin
./scripts/test.sh --folder 0760_find_anagram_mappings --language swift
./scripts/test.sh --folder 0760_find_anagram_mappings --language ruby
./scripts/test.sh --folder 0760_find_anagram_mappings --language csharp
./scripts/test.sh --folder 0760_find_anagram_mappings --language scala
./scripts/test.sh --folder 0760_find_anagram_mappings --language php
./scripts/test.sh --folder 0760_find_anagram_mappings --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0760_find_anagram_mappings --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm java java 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm c c 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm go go 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm rust rust 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm swift swift 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm scala scala 0760_find_anagram_mappings
docker compose -f docker/docker-compose.yml run --rm php php 0760_find_anagram_mappings
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0760_find_anagram_mappings` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0760_find_anagram_mappings` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0760_find_anagram_mappings` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0760_find_anagram_mappings` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0760_find_anagram_mappings` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0760_find_anagram_mappings` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0760_find_anagram_mappings` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0760_find_anagram_mappings` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0760_find_anagram_mappings` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0760_find_anagram_mappings` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0760_find_anagram_mappings` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0760_find_anagram_mappings` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0760_find_anagram_mappings` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0760_find_anagram_mappings` |

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
.\scripts\test.ps1 -Folder 0760_find_anagram_mappings -AllLanguages
```

```bash
./scripts/test.sh --folder 0760_find_anagram_mappings --all-languages
```

```zsh
./scripts/test.sh --folder 0760_find_anagram_mappings --all-languages
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
