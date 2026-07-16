# Test harness for 2280_minimum_lines_to_represent_a_line_chart

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language python
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language javascript
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language typescript
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language java
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language cpp
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language c
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language go
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language rust
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language kotlin
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language swift
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language ruby
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language csharp
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language scala
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language php
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm java java 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm c c 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm go go 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm rust rust 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm swift swift 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm scala scala 2280_minimum_lines_to_represent_a_line_chart
docker compose -f docker/docker-compose.yml run --rm php php 2280_minimum_lines_to_represent_a_line_chart
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2280_minimum_lines_to_represent_a_line_chart` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2280_minimum_lines_to_represent_a_line_chart` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2280_minimum_lines_to_represent_a_line_chart` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2280_minimum_lines_to_represent_a_line_chart` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2280_minimum_lines_to_represent_a_line_chart` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2280_minimum_lines_to_represent_a_line_chart` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2280_minimum_lines_to_represent_a_line_chart` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2280_minimum_lines_to_represent_a_line_chart` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2280_minimum_lines_to_represent_a_line_chart` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2280_minimum_lines_to_represent_a_line_chart` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2280_minimum_lines_to_represent_a_line_chart` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2280_minimum_lines_to_represent_a_line_chart` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2280_minimum_lines_to_represent_a_line_chart` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2280_minimum_lines_to_represent_a_line_chart` |

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
.\scripts\test.ps1 -Folder 2280_minimum_lines_to_represent_a_line_chart -AllLanguages
```

```bash
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --all-languages
```

```zsh
./scripts/test.sh --folder 2280_minimum_lines_to_represent_a_line_chart --all-languages
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
