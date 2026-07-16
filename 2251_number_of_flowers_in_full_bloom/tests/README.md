# Test harness for 2251_number_of_flowers_in_full_bloom

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language python
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language javascript
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language typescript
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language java
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language cpp
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language c
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language go
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language rust
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language kotlin
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language swift
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language ruby
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language csharp
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language scala
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language php
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm java java 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm c c 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm go go 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm rust rust 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm swift swift 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm scala scala 2251_number_of_flowers_in_full_bloom
docker compose -f docker/docker-compose.yml run --rm php php 2251_number_of_flowers_in_full_bloom
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2251_number_of_flowers_in_full_bloom` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2251_number_of_flowers_in_full_bloom` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2251_number_of_flowers_in_full_bloom` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2251_number_of_flowers_in_full_bloom` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2251_number_of_flowers_in_full_bloom` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2251_number_of_flowers_in_full_bloom` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2251_number_of_flowers_in_full_bloom` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2251_number_of_flowers_in_full_bloom` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2251_number_of_flowers_in_full_bloom` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2251_number_of_flowers_in_full_bloom` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2251_number_of_flowers_in_full_bloom` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2251_number_of_flowers_in_full_bloom` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2251_number_of_flowers_in_full_bloom` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2251_number_of_flowers_in_full_bloom` |

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
.\scripts\test.ps1 -Folder 2251_number_of_flowers_in_full_bloom -AllLanguages
```

```bash
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --all-languages
```

```zsh
./scripts/test.sh --folder 2251_number_of_flowers_in_full_bloom --all-languages
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
