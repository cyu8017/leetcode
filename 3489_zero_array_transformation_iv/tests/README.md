# Test harness for 3489_zero_array_transformation_iv

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language python
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language javascript
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language typescript
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language java
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language cpp
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language c
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language go
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language rust
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language kotlin
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language swift
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language ruby
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language csharp
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language scala
./scripts/test.sh --folder 3489_zero_array_transformation_iv --language php
./scripts/test.sh --folder 3489_zero_array_transformation_iv --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3489_zero_array_transformation_iv --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm java java 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm c c 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm go go 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm rust rust 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm swift swift 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm scala scala 3489_zero_array_transformation_iv
docker compose -f docker/docker-compose.yml run --rm php php 3489_zero_array_transformation_iv
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3489_zero_array_transformation_iv` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3489_zero_array_transformation_iv` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3489_zero_array_transformation_iv` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3489_zero_array_transformation_iv` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3489_zero_array_transformation_iv` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3489_zero_array_transformation_iv` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3489_zero_array_transformation_iv` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3489_zero_array_transformation_iv` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3489_zero_array_transformation_iv` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3489_zero_array_transformation_iv` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3489_zero_array_transformation_iv` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3489_zero_array_transformation_iv` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3489_zero_array_transformation_iv` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3489_zero_array_transformation_iv` |

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
.\scripts\test.ps1 -Folder 3489_zero_array_transformation_iv -AllLanguages
```

```bash
./scripts/test.sh --folder 3489_zero_array_transformation_iv --all-languages
```

```zsh
./scripts/test.sh --folder 3489_zero_array_transformation_iv --all-languages
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
