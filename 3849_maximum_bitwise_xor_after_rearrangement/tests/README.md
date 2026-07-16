# Test harness for 3849_maximum_bitwise_xor_after_rearrangement

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language python
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language javascript
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language typescript
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language java
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language cpp
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language c
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language go
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language rust
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language kotlin
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language swift
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language ruby
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language csharp
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language scala
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language php
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm java java 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm c c 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm go go 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm rust rust 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm swift swift 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm scala scala 3849_maximum_bitwise_xor_after_rearrangement
docker compose -f docker/docker-compose.yml run --rm php php 3849_maximum_bitwise_xor_after_rearrangement
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3849_maximum_bitwise_xor_after_rearrangement` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3849_maximum_bitwise_xor_after_rearrangement` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3849_maximum_bitwise_xor_after_rearrangement` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3849_maximum_bitwise_xor_after_rearrangement` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3849_maximum_bitwise_xor_after_rearrangement` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3849_maximum_bitwise_xor_after_rearrangement` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3849_maximum_bitwise_xor_after_rearrangement` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3849_maximum_bitwise_xor_after_rearrangement` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3849_maximum_bitwise_xor_after_rearrangement` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3849_maximum_bitwise_xor_after_rearrangement` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3849_maximum_bitwise_xor_after_rearrangement` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3849_maximum_bitwise_xor_after_rearrangement` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3849_maximum_bitwise_xor_after_rearrangement` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3849_maximum_bitwise_xor_after_rearrangement` |

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
.\scripts\test.ps1 -Folder 3849_maximum_bitwise_xor_after_rearrangement -AllLanguages
```

```bash
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --all-languages
```

```zsh
./scripts/test.sh --folder 3849_maximum_bitwise_xor_after_rearrangement --all-languages
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
