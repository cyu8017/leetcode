# Test harness for 2704_to_be_or_not_to_be

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language python
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language javascript
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language typescript
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language java
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language cpp
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language c
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language go
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language rust
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language kotlin
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language swift
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language ruby
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language csharp
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language scala
./scripts/test.sh --folder 2704_to_be_or_not_to_be --language php
./scripts/test.sh --folder 2704_to_be_or_not_to_be --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2704_to_be_or_not_to_be --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm java java 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm c c 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm go go 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm rust rust 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm swift swift 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm scala scala 2704_to_be_or_not_to_be
docker compose -f docker/docker-compose.yml run --rm php php 2704_to_be_or_not_to_be
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2704_to_be_or_not_to_be` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2704_to_be_or_not_to_be` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2704_to_be_or_not_to_be` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2704_to_be_or_not_to_be` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2704_to_be_or_not_to_be` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2704_to_be_or_not_to_be` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2704_to_be_or_not_to_be` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2704_to_be_or_not_to_be` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2704_to_be_or_not_to_be` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2704_to_be_or_not_to_be` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2704_to_be_or_not_to_be` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2704_to_be_or_not_to_be` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2704_to_be_or_not_to_be` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2704_to_be_or_not_to_be` |

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
.\scripts\test.ps1 -Folder 2704_to_be_or_not_to_be -AllLanguages
```

```bash
./scripts/test.sh --folder 2704_to_be_or_not_to_be --all-languages
```

```zsh
./scripts/test.sh --folder 2704_to_be_or_not_to_be --all-languages
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
