# Test harness for 2028_find_missing_observations

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2028_find_missing_observations -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2028_find_missing_observations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2028_find_missing_observations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2028_find_missing_observations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2028_find_missing_observations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2028_find_missing_observations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2028_find_missing_observations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2028_find_missing_observations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2028_find_missing_observations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2028_find_missing_observations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2028_find_missing_observations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2028_find_missing_observations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2028_find_missing_observations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2028_find_missing_observations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2028_find_missing_observations --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2028_find_missing_observations --language python
./scripts/test.sh --folder 2028_find_missing_observations --language javascript
./scripts/test.sh --folder 2028_find_missing_observations --language typescript
./scripts/test.sh --folder 2028_find_missing_observations --language java
./scripts/test.sh --folder 2028_find_missing_observations --language cpp
./scripts/test.sh --folder 2028_find_missing_observations --language c
./scripts/test.sh --folder 2028_find_missing_observations --language go
./scripts/test.sh --folder 2028_find_missing_observations --language rust
./scripts/test.sh --folder 2028_find_missing_observations --language kotlin
./scripts/test.sh --folder 2028_find_missing_observations --language swift
./scripts/test.sh --folder 2028_find_missing_observations --language ruby
./scripts/test.sh --folder 2028_find_missing_observations --language csharp
./scripts/test.sh --folder 2028_find_missing_observations --language scala
./scripts/test.sh --folder 2028_find_missing_observations --language php
./scripts/test.sh --folder 2028_find_missing_observations --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2028_find_missing_observations --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2028_find_missing_observations --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2028_find_missing_observations --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2028_find_missing_observations --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2028_find_missing_observations --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2028_find_missing_observations --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2028_find_missing_observations --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2028_find_missing_observations --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2028_find_missing_observations --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2028_find_missing_observations --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2028_find_missing_observations --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2028_find_missing_observations --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2028_find_missing_observations --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2028_find_missing_observations --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm java java 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm c c 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm go go 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm rust rust 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm swift swift 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm scala scala 2028_find_missing_observations
docker compose -f docker/docker-compose.yml run --rm php php 2028_find_missing_observations
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2028_find_missing_observations` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2028_find_missing_observations` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2028_find_missing_observations` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2028_find_missing_observations` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2028_find_missing_observations` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2028_find_missing_observations` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2028_find_missing_observations` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2028_find_missing_observations` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2028_find_missing_observations` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2028_find_missing_observations` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2028_find_missing_observations` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2028_find_missing_observations` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2028_find_missing_observations` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2028_find_missing_observations` |

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
.\scripts\test.ps1 -Folder 2028_find_missing_observations -AllLanguages
```

```bash
./scripts/test.sh --folder 2028_find_missing_observations --all-languages
```

```zsh
./scripts/test.sh --folder 2028_find_missing_observations --all-languages
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
