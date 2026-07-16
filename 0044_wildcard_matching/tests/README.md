# Test harness for 0044_wildcard_matching

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0044_wildcard_matching -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0044_wildcard_matching --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0044_wildcard_matching --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0044_wildcard_matching --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0044_wildcard_matching --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0044_wildcard_matching --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0044_wildcard_matching --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0044_wildcard_matching --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0044_wildcard_matching --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0044_wildcard_matching --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0044_wildcard_matching --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0044_wildcard_matching --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0044_wildcard_matching --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0044_wildcard_matching --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0044_wildcard_matching --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0044_wildcard_matching --language python
./scripts/test.sh --folder 0044_wildcard_matching --language javascript
./scripts/test.sh --folder 0044_wildcard_matching --language typescript
./scripts/test.sh --folder 0044_wildcard_matching --language java
./scripts/test.sh --folder 0044_wildcard_matching --language cpp
./scripts/test.sh --folder 0044_wildcard_matching --language c
./scripts/test.sh --folder 0044_wildcard_matching --language go
./scripts/test.sh --folder 0044_wildcard_matching --language rust
./scripts/test.sh --folder 0044_wildcard_matching --language kotlin
./scripts/test.sh --folder 0044_wildcard_matching --language swift
./scripts/test.sh --folder 0044_wildcard_matching --language ruby
./scripts/test.sh --folder 0044_wildcard_matching --language csharp
./scripts/test.sh --folder 0044_wildcard_matching --language scala
./scripts/test.sh --folder 0044_wildcard_matching --language php
./scripts/test.sh --folder 0044_wildcard_matching --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0044_wildcard_matching --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0044_wildcard_matching --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0044_wildcard_matching --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0044_wildcard_matching --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0044_wildcard_matching --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0044_wildcard_matching --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0044_wildcard_matching --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0044_wildcard_matching --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0044_wildcard_matching --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0044_wildcard_matching --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0044_wildcard_matching --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0044_wildcard_matching --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0044_wildcard_matching --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0044_wildcard_matching --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm java java 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm c c 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm go go 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm rust rust 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm swift swift 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm scala scala 0044_wildcard_matching
docker compose -f docker/docker-compose.yml run --rm php php 0044_wildcard_matching
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0044_wildcard_matching` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0044_wildcard_matching` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0044_wildcard_matching` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0044_wildcard_matching` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0044_wildcard_matching` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0044_wildcard_matching` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0044_wildcard_matching` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0044_wildcard_matching` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0044_wildcard_matching` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0044_wildcard_matching` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0044_wildcard_matching` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0044_wildcard_matching` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0044_wildcard_matching` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0044_wildcard_matching` |

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
.\scripts\test.ps1 -Folder 0044_wildcard_matching -AllLanguages
```

```bash
./scripts/test.sh --folder 0044_wildcard_matching --all-languages
```

```zsh
./scripts/test.sh --folder 0044_wildcard_matching --all-languages
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
