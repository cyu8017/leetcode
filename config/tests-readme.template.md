# Test harness for {PROBLEM_NAME}

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder {PROBLEM_NAME} -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder {PROBLEM_NAME} --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder {PROBLEM_NAME} --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder {PROBLEM_NAME} --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder {PROBLEM_NAME} --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder {PROBLEM_NAME} --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder {PROBLEM_NAME} --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder {PROBLEM_NAME} --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder {PROBLEM_NAME} --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder {PROBLEM_NAME} --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder {PROBLEM_NAME} --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder {PROBLEM_NAME} --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder {PROBLEM_NAME} --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder {PROBLEM_NAME} --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder {PROBLEM_NAME} --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder {PROBLEM_NAME} --language python
./scripts/test.sh --folder {PROBLEM_NAME} --language javascript
./scripts/test.sh --folder {PROBLEM_NAME} --language typescript
./scripts/test.sh --folder {PROBLEM_NAME} --language java
./scripts/test.sh --folder {PROBLEM_NAME} --language cpp
./scripts/test.sh --folder {PROBLEM_NAME} --language c
./scripts/test.sh --folder {PROBLEM_NAME} --language go
./scripts/test.sh --folder {PROBLEM_NAME} --language rust
./scripts/test.sh --folder {PROBLEM_NAME} --language kotlin
./scripts/test.sh --folder {PROBLEM_NAME} --language swift
./scripts/test.sh --folder {PROBLEM_NAME} --language ruby
./scripts/test.sh --folder {PROBLEM_NAME} --language csharp
./scripts/test.sh --folder {PROBLEM_NAME} --language scala
./scripts/test.sh --folder {PROBLEM_NAME} --language php
./scripts/test.sh --folder {PROBLEM_NAME} --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder {PROBLEM_NAME} --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder {PROBLEM_NAME} --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder {PROBLEM_NAME} --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder {PROBLEM_NAME} --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder {PROBLEM_NAME} --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder {PROBLEM_NAME} --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder {PROBLEM_NAME} --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder {PROBLEM_NAME} --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder {PROBLEM_NAME} --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder {PROBLEM_NAME} --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder {PROBLEM_NAME} --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder {PROBLEM_NAME} --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder {PROBLEM_NAME} --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder {PROBLEM_NAME} --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm javascript javascript {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm typescript typescript {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm java java {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm cpp cpp {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm c c {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm go go {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm rust rust {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm swift swift {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm ruby ruby {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm csharp csharp {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm scala scala {PROBLEM_NAME}
docker compose -f docker/docker-compose.yml run --rm php php {PROBLEM_NAME}
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python {PROBLEM_NAME}` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript {PROBLEM_NAME}` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript {PROBLEM_NAME}` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java {PROBLEM_NAME}` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp {PROBLEM_NAME}` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c {PROBLEM_NAME}` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go {PROBLEM_NAME}` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust {PROBLEM_NAME}` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin {PROBLEM_NAME}` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift {PROBLEM_NAME}` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby {PROBLEM_NAME}` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp {PROBLEM_NAME}` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala {PROBLEM_NAME}` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php {PROBLEM_NAME}` |

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
.\scripts\test.ps1 -Folder {PROBLEM_NAME} -AllLanguages
```

```bash
./scripts/test.sh --folder {PROBLEM_NAME} --all-languages
```

```zsh
./scripts/test.sh --folder {PROBLEM_NAME} --all-languages
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
