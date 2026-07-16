# Test harness for 1282_group_the_people_given_the_group_size_they_belong_to

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language python
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language javascript
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language typescript
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language java
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language cpp
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language c
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language go
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language rust
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language kotlin
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language swift
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language ruby
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language csharp
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language scala
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language php
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm java java 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm c c 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm go go 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm rust rust 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm swift swift 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm scala scala 1282_group_the_people_given_the_group_size_they_belong_to
docker compose -f docker/docker-compose.yml run --rm php php 1282_group_the_people_given_the_group_size_they_belong_to
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1282_group_the_people_given_the_group_size_they_belong_to` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1282_group_the_people_given_the_group_size_they_belong_to` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1282_group_the_people_given_the_group_size_they_belong_to` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1282_group_the_people_given_the_group_size_they_belong_to` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1282_group_the_people_given_the_group_size_they_belong_to` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1282_group_the_people_given_the_group_size_they_belong_to` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1282_group_the_people_given_the_group_size_they_belong_to` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1282_group_the_people_given_the_group_size_they_belong_to` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1282_group_the_people_given_the_group_size_they_belong_to` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1282_group_the_people_given_the_group_size_they_belong_to` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1282_group_the_people_given_the_group_size_they_belong_to` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1282_group_the_people_given_the_group_size_they_belong_to` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1282_group_the_people_given_the_group_size_they_belong_to` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1282_group_the_people_given_the_group_size_they_belong_to` |

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
.\scripts\test.ps1 -Folder 1282_group_the_people_given_the_group_size_they_belong_to -AllLanguages
```

```bash
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --all-languages
```

```zsh
./scripts/test.sh --folder 1282_group_the_people_given_the_group_size_they_belong_to --all-languages
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
