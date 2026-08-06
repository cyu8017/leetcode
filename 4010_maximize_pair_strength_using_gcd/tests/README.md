# Test harness for 4010_maximize_pair_strength_using_gcd

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language python
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language javascript
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language typescript
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language java
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language cpp
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language c
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language go
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language rust
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language kotlin
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language swift
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language ruby
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language csharp
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language scala
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language php
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm javascript javascript 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm typescript typescript 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm java java 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm cpp cpp 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm c c 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm go go 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm rust rust 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm swift swift 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm ruby ruby 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm csharp csharp 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm scala scala 4010_maximize_pair_strength_using_gcd
docker compose -f docker/docker-compose.yml run --rm php php 4010_maximize_pair_strength_using_gcd
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 4010_maximize_pair_strength_using_gcd` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 4010_maximize_pair_strength_using_gcd` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 4010_maximize_pair_strength_using_gcd` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 4010_maximize_pair_strength_using_gcd` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 4010_maximize_pair_strength_using_gcd` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 4010_maximize_pair_strength_using_gcd` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 4010_maximize_pair_strength_using_gcd` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 4010_maximize_pair_strength_using_gcd` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 4010_maximize_pair_strength_using_gcd` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 4010_maximize_pair_strength_using_gcd` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 4010_maximize_pair_strength_using_gcd` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 4010_maximize_pair_strength_using_gcd` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 4010_maximize_pair_strength_using_gcd` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 4010_maximize_pair_strength_using_gcd` |

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
.\scripts\test.ps1 -Folder 4010_maximize_pair_strength_using_gcd -AllLanguages
```

```bash
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --all-languages
```

```zsh
./scripts/test.sh --folder 4010_maximize_pair_strength_using_gcd --all-languages
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
