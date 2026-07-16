# Test harness for 2504_concatenate_the_name_and_the_profession

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language python
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language javascript
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language typescript
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language java
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language cpp
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language c
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language go
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language rust
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language kotlin
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language swift
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language ruby
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language csharp
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language scala
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language php
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm java java 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm c c 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm go go 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm rust rust 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm swift swift 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm scala scala 2504_concatenate_the_name_and_the_profession
docker compose -f docker/docker-compose.yml run --rm php php 2504_concatenate_the_name_and_the_profession
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2504_concatenate_the_name_and_the_profession` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2504_concatenate_the_name_and_the_profession` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2504_concatenate_the_name_and_the_profession` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2504_concatenate_the_name_and_the_profession` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2504_concatenate_the_name_and_the_profession` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2504_concatenate_the_name_and_the_profession` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2504_concatenate_the_name_and_the_profession` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2504_concatenate_the_name_and_the_profession` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2504_concatenate_the_name_and_the_profession` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2504_concatenate_the_name_and_the_profession` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2504_concatenate_the_name_and_the_profession` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2504_concatenate_the_name_and_the_profession` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2504_concatenate_the_name_and_the_profession` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2504_concatenate_the_name_and_the_profession` |

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
.\scripts\test.ps1 -Folder 2504_concatenate_the_name_and_the_profession -AllLanguages
```

```bash
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --all-languages
```

```zsh
./scripts/test.sh --folder 2504_concatenate_the_name_and_the_profession --all-languages
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
