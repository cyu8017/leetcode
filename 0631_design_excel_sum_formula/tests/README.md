# Test harness for 0631_design_excel_sum_formula

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0631_design_excel_sum_formula --language python
./scripts/test.sh --folder 0631_design_excel_sum_formula --language javascript
./scripts/test.sh --folder 0631_design_excel_sum_formula --language typescript
./scripts/test.sh --folder 0631_design_excel_sum_formula --language java
./scripts/test.sh --folder 0631_design_excel_sum_formula --language cpp
./scripts/test.sh --folder 0631_design_excel_sum_formula --language c
./scripts/test.sh --folder 0631_design_excel_sum_formula --language go
./scripts/test.sh --folder 0631_design_excel_sum_formula --language rust
./scripts/test.sh --folder 0631_design_excel_sum_formula --language kotlin
./scripts/test.sh --folder 0631_design_excel_sum_formula --language swift
./scripts/test.sh --folder 0631_design_excel_sum_formula --language ruby
./scripts/test.sh --folder 0631_design_excel_sum_formula --language csharp
./scripts/test.sh --folder 0631_design_excel_sum_formula --language scala
./scripts/test.sh --folder 0631_design_excel_sum_formula --language php
./scripts/test.sh --folder 0631_design_excel_sum_formula --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0631_design_excel_sum_formula --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm java java 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm c c 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm go go 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm rust rust 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm swift swift 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm scala scala 0631_design_excel_sum_formula
docker compose -f docker/docker-compose.yml run --rm php php 0631_design_excel_sum_formula
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0631_design_excel_sum_formula` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0631_design_excel_sum_formula` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0631_design_excel_sum_formula` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0631_design_excel_sum_formula` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0631_design_excel_sum_formula` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0631_design_excel_sum_formula` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0631_design_excel_sum_formula` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0631_design_excel_sum_formula` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0631_design_excel_sum_formula` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0631_design_excel_sum_formula` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0631_design_excel_sum_formula` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0631_design_excel_sum_formula` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0631_design_excel_sum_formula` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0631_design_excel_sum_formula` |

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
.\scripts\test.ps1 -Folder 0631_design_excel_sum_formula -AllLanguages
```

```bash
./scripts/test.sh --folder 0631_design_excel_sum_formula --all-languages
```

```zsh
./scripts/test.sh --folder 0631_design_excel_sum_formula --all-languages
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
