# Test harness for 0923_3sum_with_multiplicity

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language python
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language javascript
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language typescript
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language java
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language cpp
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language c
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language go
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language rust
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language kotlin
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language swift
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language ruby
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language csharp
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language scala
./scripts/test.sh --folder 0923_3sum_with_multiplicity --language php
./scripts/test.sh --folder 0923_3sum_with_multiplicity --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0923_3sum_with_multiplicity --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm java java 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm c c 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm go go 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm rust rust 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm swift swift 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm scala scala 0923_3sum_with_multiplicity
docker compose -f docker/docker-compose.yml run --rm php php 0923_3sum_with_multiplicity
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0923_3sum_with_multiplicity` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0923_3sum_with_multiplicity` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0923_3sum_with_multiplicity` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0923_3sum_with_multiplicity` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0923_3sum_with_multiplicity` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0923_3sum_with_multiplicity` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0923_3sum_with_multiplicity` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0923_3sum_with_multiplicity` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0923_3sum_with_multiplicity` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0923_3sum_with_multiplicity` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0923_3sum_with_multiplicity` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0923_3sum_with_multiplicity` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0923_3sum_with_multiplicity` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0923_3sum_with_multiplicity` |

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
.\scripts\test.ps1 -Folder 0923_3sum_with_multiplicity -AllLanguages
```

```bash
./scripts/test.sh --folder 0923_3sum_with_multiplicity --all-languages
```

```zsh
./scripts/test.sh --folder 0923_3sum_with_multiplicity --all-languages
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
