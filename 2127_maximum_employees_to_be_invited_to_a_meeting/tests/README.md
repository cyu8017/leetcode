# Test harness for 2127_maximum_employees_to_be_invited_to_a_meeting

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language python
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language javascript
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language typescript
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language java
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language cpp
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language c
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language go
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language rust
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language kotlin
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language swift
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language ruby
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language csharp
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language scala
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language php
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm java java 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm c c 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm go go 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm rust rust 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm swift swift 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm scala scala 2127_maximum_employees_to_be_invited_to_a_meeting
docker compose -f docker/docker-compose.yml run --rm php php 2127_maximum_employees_to_be_invited_to_a_meeting
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2127_maximum_employees_to_be_invited_to_a_meeting` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2127_maximum_employees_to_be_invited_to_a_meeting` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2127_maximum_employees_to_be_invited_to_a_meeting` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2127_maximum_employees_to_be_invited_to_a_meeting` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2127_maximum_employees_to_be_invited_to_a_meeting` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2127_maximum_employees_to_be_invited_to_a_meeting` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2127_maximum_employees_to_be_invited_to_a_meeting` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2127_maximum_employees_to_be_invited_to_a_meeting` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2127_maximum_employees_to_be_invited_to_a_meeting` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2127_maximum_employees_to_be_invited_to_a_meeting` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2127_maximum_employees_to_be_invited_to_a_meeting` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2127_maximum_employees_to_be_invited_to_a_meeting` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2127_maximum_employees_to_be_invited_to_a_meeting` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2127_maximum_employees_to_be_invited_to_a_meeting` |

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
.\scripts\test.ps1 -Folder 2127_maximum_employees_to_be_invited_to_a_meeting -AllLanguages
```

```bash
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --all-languages
```

```zsh
./scripts/test.sh --folder 2127_maximum_employees_to_be_invited_to_a_meeting --all-languages
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
