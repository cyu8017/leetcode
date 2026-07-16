# Test harness for 0058_length_of_last_word

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0058_length_of_last_word -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0058_length_of_last_word --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0058_length_of_last_word --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0058_length_of_last_word --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0058_length_of_last_word --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0058_length_of_last_word --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0058_length_of_last_word --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0058_length_of_last_word --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0058_length_of_last_word --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0058_length_of_last_word --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0058_length_of_last_word --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0058_length_of_last_word --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0058_length_of_last_word --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0058_length_of_last_word --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0058_length_of_last_word --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0058_length_of_last_word --language python
./scripts/test.sh --folder 0058_length_of_last_word --language javascript
./scripts/test.sh --folder 0058_length_of_last_word --language typescript
./scripts/test.sh --folder 0058_length_of_last_word --language java
./scripts/test.sh --folder 0058_length_of_last_word --language cpp
./scripts/test.sh --folder 0058_length_of_last_word --language c
./scripts/test.sh --folder 0058_length_of_last_word --language go
./scripts/test.sh --folder 0058_length_of_last_word --language rust
./scripts/test.sh --folder 0058_length_of_last_word --language kotlin
./scripts/test.sh --folder 0058_length_of_last_word --language swift
./scripts/test.sh --folder 0058_length_of_last_word --language ruby
./scripts/test.sh --folder 0058_length_of_last_word --language csharp
./scripts/test.sh --folder 0058_length_of_last_word --language scala
./scripts/test.sh --folder 0058_length_of_last_word --language php
./scripts/test.sh --folder 0058_length_of_last_word --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0058_length_of_last_word --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0058_length_of_last_word --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0058_length_of_last_word --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0058_length_of_last_word --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0058_length_of_last_word --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0058_length_of_last_word --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0058_length_of_last_word --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0058_length_of_last_word --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0058_length_of_last_word --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0058_length_of_last_word --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0058_length_of_last_word --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0058_length_of_last_word --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0058_length_of_last_word --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0058_length_of_last_word --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm java java 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm c c 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm go go 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm rust rust 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm swift swift 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm scala scala 0058_length_of_last_word
docker compose -f docker/docker-compose.yml run --rm php php 0058_length_of_last_word
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0058_length_of_last_word` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0058_length_of_last_word` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0058_length_of_last_word` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0058_length_of_last_word` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0058_length_of_last_word` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0058_length_of_last_word` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0058_length_of_last_word` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0058_length_of_last_word` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0058_length_of_last_word` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0058_length_of_last_word` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0058_length_of_last_word` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0058_length_of_last_word` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0058_length_of_last_word` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0058_length_of_last_word` |

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
.\scripts\test.ps1 -Folder 0058_length_of_last_word -AllLanguages
```

```bash
./scripts/test.sh --folder 0058_length_of_last_word --all-languages
```

```zsh
./scripts/test.sh --folder 0058_length_of_last_word --all-languages
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
