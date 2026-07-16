# Test harness for 3055_top_percentile_fraud

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3055_top_percentile_fraud --language python
./scripts/test.sh --folder 3055_top_percentile_fraud --language javascript
./scripts/test.sh --folder 3055_top_percentile_fraud --language typescript
./scripts/test.sh --folder 3055_top_percentile_fraud --language java
./scripts/test.sh --folder 3055_top_percentile_fraud --language cpp
./scripts/test.sh --folder 3055_top_percentile_fraud --language c
./scripts/test.sh --folder 3055_top_percentile_fraud --language go
./scripts/test.sh --folder 3055_top_percentile_fraud --language rust
./scripts/test.sh --folder 3055_top_percentile_fraud --language kotlin
./scripts/test.sh --folder 3055_top_percentile_fraud --language swift
./scripts/test.sh --folder 3055_top_percentile_fraud --language ruby
./scripts/test.sh --folder 3055_top_percentile_fraud --language csharp
./scripts/test.sh --folder 3055_top_percentile_fraud --language scala
./scripts/test.sh --folder 3055_top_percentile_fraud --language php
./scripts/test.sh --folder 3055_top_percentile_fraud --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3055_top_percentile_fraud --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm java java 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm c c 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm go go 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm rust rust 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm swift swift 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm scala scala 3055_top_percentile_fraud
docker compose -f docker/docker-compose.yml run --rm php php 3055_top_percentile_fraud
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3055_top_percentile_fraud` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3055_top_percentile_fraud` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3055_top_percentile_fraud` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3055_top_percentile_fraud` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3055_top_percentile_fraud` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3055_top_percentile_fraud` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3055_top_percentile_fraud` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3055_top_percentile_fraud` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3055_top_percentile_fraud` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3055_top_percentile_fraud` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3055_top_percentile_fraud` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3055_top_percentile_fraud` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3055_top_percentile_fraud` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3055_top_percentile_fraud` |

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
.\scripts\test.ps1 -Folder 3055_top_percentile_fraud -AllLanguages
```

```bash
./scripts/test.sh --folder 3055_top_percentile_fraud --all-languages
```

```zsh
./scripts/test.sh --folder 3055_top_percentile_fraud --all-languages
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
