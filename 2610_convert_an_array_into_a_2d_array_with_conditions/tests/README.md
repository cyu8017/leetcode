# Test harness for 2610_convert_an_array_into_a_2d_array_with_conditions

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language python
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language javascript
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language typescript
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language java
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language cpp
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language c
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language go
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language rust
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language kotlin
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language swift
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language ruby
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language csharp
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language scala
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language php
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm java java 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm c c 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm go go 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm rust rust 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm swift swift 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm scala scala 2610_convert_an_array_into_a_2d_array_with_conditions
docker compose -f docker/docker-compose.yml run --rm php php 2610_convert_an_array_into_a_2d_array_with_conditions
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2610_convert_an_array_into_a_2d_array_with_conditions` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2610_convert_an_array_into_a_2d_array_with_conditions` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2610_convert_an_array_into_a_2d_array_with_conditions` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2610_convert_an_array_into_a_2d_array_with_conditions` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2610_convert_an_array_into_a_2d_array_with_conditions` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2610_convert_an_array_into_a_2d_array_with_conditions` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2610_convert_an_array_into_a_2d_array_with_conditions` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2610_convert_an_array_into_a_2d_array_with_conditions` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2610_convert_an_array_into_a_2d_array_with_conditions` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2610_convert_an_array_into_a_2d_array_with_conditions` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2610_convert_an_array_into_a_2d_array_with_conditions` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2610_convert_an_array_into_a_2d_array_with_conditions` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2610_convert_an_array_into_a_2d_array_with_conditions` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2610_convert_an_array_into_a_2d_array_with_conditions` |

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
.\scripts\test.ps1 -Folder 2610_convert_an_array_into_a_2d_array_with_conditions -AllLanguages
```

```bash
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --all-languages
```

```zsh
./scripts/test.sh --folder 2610_convert_an_array_into_a_2d_array_with_conditions --all-languages
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
