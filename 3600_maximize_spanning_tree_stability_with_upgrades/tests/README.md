# Test harness for 3600_maximize_spanning_tree_stability_with_upgrades

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language python
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language javascript
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language typescript
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language java
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language cpp
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language c
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language go
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language rust
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language kotlin
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language swift
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language ruby
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language csharp
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language scala
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language php
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm java java 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm c c 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm go go 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm rust rust 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm swift swift 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm scala scala 3600_maximize_spanning_tree_stability_with_upgrades
docker compose -f docker/docker-compose.yml run --rm php php 3600_maximize_spanning_tree_stability_with_upgrades
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3600_maximize_spanning_tree_stability_with_upgrades` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3600_maximize_spanning_tree_stability_with_upgrades` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3600_maximize_spanning_tree_stability_with_upgrades` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3600_maximize_spanning_tree_stability_with_upgrades` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3600_maximize_spanning_tree_stability_with_upgrades` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3600_maximize_spanning_tree_stability_with_upgrades` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3600_maximize_spanning_tree_stability_with_upgrades` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3600_maximize_spanning_tree_stability_with_upgrades` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3600_maximize_spanning_tree_stability_with_upgrades` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3600_maximize_spanning_tree_stability_with_upgrades` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3600_maximize_spanning_tree_stability_with_upgrades` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3600_maximize_spanning_tree_stability_with_upgrades` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3600_maximize_spanning_tree_stability_with_upgrades` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3600_maximize_spanning_tree_stability_with_upgrades` |

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
.\scripts\test.ps1 -Folder 3600_maximize_spanning_tree_stability_with_upgrades -AllLanguages
```

```bash
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --all-languages
```

```zsh
./scripts/test.sh --folder 3600_maximize_spanning_tree_stability_with_upgrades --all-languages
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
