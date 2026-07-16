# Test harness for 1995_count_special_quadruplets

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1995_count_special_quadruplets --language python
./scripts/test.sh --folder 1995_count_special_quadruplets --language javascript
./scripts/test.sh --folder 1995_count_special_quadruplets --language typescript
./scripts/test.sh --folder 1995_count_special_quadruplets --language java
./scripts/test.sh --folder 1995_count_special_quadruplets --language cpp
./scripts/test.sh --folder 1995_count_special_quadruplets --language c
./scripts/test.sh --folder 1995_count_special_quadruplets --language go
./scripts/test.sh --folder 1995_count_special_quadruplets --language rust
./scripts/test.sh --folder 1995_count_special_quadruplets --language kotlin
./scripts/test.sh --folder 1995_count_special_quadruplets --language swift
./scripts/test.sh --folder 1995_count_special_quadruplets --language ruby
./scripts/test.sh --folder 1995_count_special_quadruplets --language csharp
./scripts/test.sh --folder 1995_count_special_quadruplets --language scala
./scripts/test.sh --folder 1995_count_special_quadruplets --language php
./scripts/test.sh --folder 1995_count_special_quadruplets --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1995_count_special_quadruplets --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm java java 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm c c 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm go go 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm rust rust 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm swift swift 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm scala scala 1995_count_special_quadruplets
docker compose -f docker/docker-compose.yml run --rm php php 1995_count_special_quadruplets
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1995_count_special_quadruplets` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1995_count_special_quadruplets` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1995_count_special_quadruplets` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1995_count_special_quadruplets` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1995_count_special_quadruplets` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1995_count_special_quadruplets` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1995_count_special_quadruplets` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1995_count_special_quadruplets` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1995_count_special_quadruplets` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1995_count_special_quadruplets` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1995_count_special_quadruplets` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1995_count_special_quadruplets` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1995_count_special_quadruplets` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1995_count_special_quadruplets` |

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
.\scripts\test.ps1 -Folder 1995_count_special_quadruplets -AllLanguages
```

```bash
./scripts/test.sh --folder 1995_count_special_quadruplets --all-languages
```

```zsh
./scripts/test.sh --folder 1995_count_special_quadruplets --all-languages
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
