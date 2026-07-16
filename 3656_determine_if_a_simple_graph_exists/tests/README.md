# Test harness for 3656_determine_if_a_simple_graph_exists

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language python
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language javascript
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language typescript
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language java
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language cpp
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language c
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language go
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language rust
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language kotlin
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language swift
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language ruby
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language csharp
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language scala
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language php
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm java java 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm c c 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm go go 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm rust rust 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm swift swift 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm scala scala 3656_determine_if_a_simple_graph_exists
docker compose -f docker/docker-compose.yml run --rm php php 3656_determine_if_a_simple_graph_exists
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3656_determine_if_a_simple_graph_exists` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3656_determine_if_a_simple_graph_exists` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3656_determine_if_a_simple_graph_exists` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3656_determine_if_a_simple_graph_exists` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3656_determine_if_a_simple_graph_exists` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3656_determine_if_a_simple_graph_exists` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3656_determine_if_a_simple_graph_exists` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3656_determine_if_a_simple_graph_exists` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3656_determine_if_a_simple_graph_exists` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3656_determine_if_a_simple_graph_exists` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3656_determine_if_a_simple_graph_exists` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3656_determine_if_a_simple_graph_exists` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3656_determine_if_a_simple_graph_exists` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3656_determine_if_a_simple_graph_exists` |

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
.\scripts\test.ps1 -Folder 3656_determine_if_a_simple_graph_exists -AllLanguages
```

```bash
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --all-languages
```

```zsh
./scripts/test.sh --folder 3656_determine_if_a_simple_graph_exists --all-languages
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
