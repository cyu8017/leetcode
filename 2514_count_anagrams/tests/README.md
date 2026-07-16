# Test harness for 2514_count_anagrams

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2514_count_anagrams -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2514_count_anagrams --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2514_count_anagrams --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2514_count_anagrams --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2514_count_anagrams --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2514_count_anagrams --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2514_count_anagrams --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2514_count_anagrams --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2514_count_anagrams --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2514_count_anagrams --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2514_count_anagrams --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2514_count_anagrams --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2514_count_anagrams --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2514_count_anagrams --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2514_count_anagrams --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2514_count_anagrams --language python
./scripts/test.sh --folder 2514_count_anagrams --language javascript
./scripts/test.sh --folder 2514_count_anagrams --language typescript
./scripts/test.sh --folder 2514_count_anagrams --language java
./scripts/test.sh --folder 2514_count_anagrams --language cpp
./scripts/test.sh --folder 2514_count_anagrams --language c
./scripts/test.sh --folder 2514_count_anagrams --language go
./scripts/test.sh --folder 2514_count_anagrams --language rust
./scripts/test.sh --folder 2514_count_anagrams --language kotlin
./scripts/test.sh --folder 2514_count_anagrams --language swift
./scripts/test.sh --folder 2514_count_anagrams --language ruby
./scripts/test.sh --folder 2514_count_anagrams --language csharp
./scripts/test.sh --folder 2514_count_anagrams --language scala
./scripts/test.sh --folder 2514_count_anagrams --language php
./scripts/test.sh --folder 2514_count_anagrams --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2514_count_anagrams --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2514_count_anagrams --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2514_count_anagrams --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2514_count_anagrams --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2514_count_anagrams --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2514_count_anagrams --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2514_count_anagrams --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2514_count_anagrams --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2514_count_anagrams --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2514_count_anagrams --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2514_count_anagrams --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2514_count_anagrams --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2514_count_anagrams --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2514_count_anagrams --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm java java 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm c c 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm go go 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm rust rust 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm swift swift 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm scala scala 2514_count_anagrams
docker compose -f docker/docker-compose.yml run --rm php php 2514_count_anagrams
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2514_count_anagrams` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2514_count_anagrams` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2514_count_anagrams` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2514_count_anagrams` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2514_count_anagrams` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2514_count_anagrams` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2514_count_anagrams` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2514_count_anagrams` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2514_count_anagrams` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2514_count_anagrams` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2514_count_anagrams` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2514_count_anagrams` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2514_count_anagrams` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2514_count_anagrams` |

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
.\scripts\test.ps1 -Folder 2514_count_anagrams -AllLanguages
```

```bash
./scripts/test.sh --folder 2514_count_anagrams --all-languages
```

```zsh
./scripts/test.sh --folder 2514_count_anagrams --all-languages
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
