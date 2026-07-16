# Test harness for 1245_tree_diameter

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1245_tree_diameter -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1245_tree_diameter --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1245_tree_diameter --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1245_tree_diameter --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1245_tree_diameter --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1245_tree_diameter --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1245_tree_diameter --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1245_tree_diameter --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1245_tree_diameter --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1245_tree_diameter --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1245_tree_diameter --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1245_tree_diameter --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1245_tree_diameter --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1245_tree_diameter --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1245_tree_diameter --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1245_tree_diameter --language python
./scripts/test.sh --folder 1245_tree_diameter --language javascript
./scripts/test.sh --folder 1245_tree_diameter --language typescript
./scripts/test.sh --folder 1245_tree_diameter --language java
./scripts/test.sh --folder 1245_tree_diameter --language cpp
./scripts/test.sh --folder 1245_tree_diameter --language c
./scripts/test.sh --folder 1245_tree_diameter --language go
./scripts/test.sh --folder 1245_tree_diameter --language rust
./scripts/test.sh --folder 1245_tree_diameter --language kotlin
./scripts/test.sh --folder 1245_tree_diameter --language swift
./scripts/test.sh --folder 1245_tree_diameter --language ruby
./scripts/test.sh --folder 1245_tree_diameter --language csharp
./scripts/test.sh --folder 1245_tree_diameter --language scala
./scripts/test.sh --folder 1245_tree_diameter --language php
./scripts/test.sh --folder 1245_tree_diameter --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1245_tree_diameter --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1245_tree_diameter --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1245_tree_diameter --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1245_tree_diameter --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1245_tree_diameter --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1245_tree_diameter --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1245_tree_diameter --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1245_tree_diameter --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1245_tree_diameter --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1245_tree_diameter --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1245_tree_diameter --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1245_tree_diameter --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1245_tree_diameter --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1245_tree_diameter --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm java java 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm c c 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm go go 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm rust rust 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm swift swift 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm scala scala 1245_tree_diameter
docker compose -f docker/docker-compose.yml run --rm php php 1245_tree_diameter
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1245_tree_diameter` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1245_tree_diameter` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1245_tree_diameter` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1245_tree_diameter` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1245_tree_diameter` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1245_tree_diameter` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1245_tree_diameter` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1245_tree_diameter` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1245_tree_diameter` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1245_tree_diameter` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1245_tree_diameter` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1245_tree_diameter` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1245_tree_diameter` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1245_tree_diameter` |

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
.\scripts\test.ps1 -Folder 1245_tree_diameter -AllLanguages
```

```bash
./scripts/test.sh --folder 1245_tree_diameter --all-languages
```

```zsh
./scripts/test.sh --folder 1245_tree_diameter --all-languages
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
