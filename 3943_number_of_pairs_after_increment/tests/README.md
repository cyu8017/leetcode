# Test harness for 3943_number_of_pairs_after_increment

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language python
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language javascript
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language typescript
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language java
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language cpp
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language c
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language go
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language rust
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language kotlin
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language swift
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language ruby
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language csharp
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language scala
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language php
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3943_number_of_pairs_after_increment --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm java java 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm c c 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm go go 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm rust rust 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm swift swift 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm scala scala 3943_number_of_pairs_after_increment
docker compose -f docker/docker-compose.yml run --rm php php 3943_number_of_pairs_after_increment
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3943_number_of_pairs_after_increment` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3943_number_of_pairs_after_increment` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3943_number_of_pairs_after_increment` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3943_number_of_pairs_after_increment` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3943_number_of_pairs_after_increment` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3943_number_of_pairs_after_increment` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3943_number_of_pairs_after_increment` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3943_number_of_pairs_after_increment` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3943_number_of_pairs_after_increment` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3943_number_of_pairs_after_increment` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3943_number_of_pairs_after_increment` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3943_number_of_pairs_after_increment` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3943_number_of_pairs_after_increment` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3943_number_of_pairs_after_increment` |

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
.\scripts\test.ps1 -Folder 3943_number_of_pairs_after_increment -AllLanguages
```

```bash
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --all-languages
```

```zsh
./scripts/test.sh --folder 3943_number_of_pairs_after_increment --all-languages
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
