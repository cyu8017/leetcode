# Test harness for 0526_beautiful_arrangement

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0526_beautiful_arrangement --language python
./scripts/test.sh --folder 0526_beautiful_arrangement --language javascript
./scripts/test.sh --folder 0526_beautiful_arrangement --language typescript
./scripts/test.sh --folder 0526_beautiful_arrangement --language java
./scripts/test.sh --folder 0526_beautiful_arrangement --language cpp
./scripts/test.sh --folder 0526_beautiful_arrangement --language c
./scripts/test.sh --folder 0526_beautiful_arrangement --language go
./scripts/test.sh --folder 0526_beautiful_arrangement --language rust
./scripts/test.sh --folder 0526_beautiful_arrangement --language kotlin
./scripts/test.sh --folder 0526_beautiful_arrangement --language swift
./scripts/test.sh --folder 0526_beautiful_arrangement --language ruby
./scripts/test.sh --folder 0526_beautiful_arrangement --language csharp
./scripts/test.sh --folder 0526_beautiful_arrangement --language scala
./scripts/test.sh --folder 0526_beautiful_arrangement --language php
./scripts/test.sh --folder 0526_beautiful_arrangement --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0526_beautiful_arrangement --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm java java 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm c c 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm go go 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm rust rust 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm swift swift 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm scala scala 0526_beautiful_arrangement
docker compose -f docker/docker-compose.yml run --rm php php 0526_beautiful_arrangement
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0526_beautiful_arrangement` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0526_beautiful_arrangement` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0526_beautiful_arrangement` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0526_beautiful_arrangement` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0526_beautiful_arrangement` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0526_beautiful_arrangement` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0526_beautiful_arrangement` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0526_beautiful_arrangement` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0526_beautiful_arrangement` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0526_beautiful_arrangement` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0526_beautiful_arrangement` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0526_beautiful_arrangement` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0526_beautiful_arrangement` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0526_beautiful_arrangement` |

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
.\scripts\test.ps1 -Folder 0526_beautiful_arrangement -AllLanguages
```

```bash
./scripts/test.sh --folder 0526_beautiful_arrangement --all-languages
```

```zsh
./scripts/test.sh --folder 0526_beautiful_arrangement --all-languages
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
