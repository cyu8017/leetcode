# Test harness for 3973_distinct_gate_paths_to_lca

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language python
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language javascript
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language typescript
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language java
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language cpp
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language c
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language go
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language rust
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language kotlin
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language swift
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language ruby
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language csharp
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language scala
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language php
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm java java 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm c c 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm go go 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm rust rust 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm swift swift 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm scala scala 3973_distinct_gate_paths_to_lca
docker compose -f docker/docker-compose.yml run --rm php php 3973_distinct_gate_paths_to_lca
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3973_distinct_gate_paths_to_lca` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3973_distinct_gate_paths_to_lca` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3973_distinct_gate_paths_to_lca` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3973_distinct_gate_paths_to_lca` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3973_distinct_gate_paths_to_lca` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3973_distinct_gate_paths_to_lca` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3973_distinct_gate_paths_to_lca` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3973_distinct_gate_paths_to_lca` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3973_distinct_gate_paths_to_lca` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3973_distinct_gate_paths_to_lca` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3973_distinct_gate_paths_to_lca` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3973_distinct_gate_paths_to_lca` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3973_distinct_gate_paths_to_lca` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3973_distinct_gate_paths_to_lca` |

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
.\scripts\test.ps1 -Folder 3973_distinct_gate_paths_to_lca -AllLanguages
```

```bash
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --all-languages
```

```zsh
./scripts/test.sh --folder 3973_distinct_gate_paths_to_lca --all-languages
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
