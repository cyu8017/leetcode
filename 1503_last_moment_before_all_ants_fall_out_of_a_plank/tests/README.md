# Test harness for 1503_last_moment_before_all_ants_fall_out_of_a_plank

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language python
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language javascript
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language typescript
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language java
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language cpp
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language c
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language go
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language rust
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language kotlin
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language swift
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language ruby
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language csharp
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language scala
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language php
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm java java 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm c c 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm go go 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm rust rust 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm swift swift 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm scala scala 1503_last_moment_before_all_ants_fall_out_of_a_plank
docker compose -f docker/docker-compose.yml run --rm php php 1503_last_moment_before_all_ants_fall_out_of_a_plank
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1503_last_moment_before_all_ants_fall_out_of_a_plank` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1503_last_moment_before_all_ants_fall_out_of_a_plank` |

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
.\scripts\test.ps1 -Folder 1503_last_moment_before_all_ants_fall_out_of_a_plank -AllLanguages
```

```bash
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --all-languages
```

```zsh
./scripts/test.sh --folder 1503_last_moment_before_all_ants_fall_out_of_a_plank --all-languages
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
