# Test harness for 1820_maximum_number_of_accepted_invitations

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language python
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language javascript
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language typescript
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language java
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language cpp
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language c
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language go
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language rust
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language kotlin
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language swift
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language ruby
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language csharp
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language scala
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language php
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm java java 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm c c 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm go go 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm rust rust 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm swift swift 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm scala scala 1820_maximum_number_of_accepted_invitations
docker compose -f docker/docker-compose.yml run --rm php php 1820_maximum_number_of_accepted_invitations
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1820_maximum_number_of_accepted_invitations` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1820_maximum_number_of_accepted_invitations` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1820_maximum_number_of_accepted_invitations` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1820_maximum_number_of_accepted_invitations` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1820_maximum_number_of_accepted_invitations` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1820_maximum_number_of_accepted_invitations` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1820_maximum_number_of_accepted_invitations` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1820_maximum_number_of_accepted_invitations` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1820_maximum_number_of_accepted_invitations` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1820_maximum_number_of_accepted_invitations` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1820_maximum_number_of_accepted_invitations` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1820_maximum_number_of_accepted_invitations` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1820_maximum_number_of_accepted_invitations` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1820_maximum_number_of_accepted_invitations` |

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
.\scripts\test.ps1 -Folder 1820_maximum_number_of_accepted_invitations -AllLanguages
```

```bash
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --all-languages
```

```zsh
./scripts/test.sh --folder 1820_maximum_number_of_accepted_invitations --all-languages
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
