# Test harness for 1129_shortest_path_with_alternating_colors

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language python
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language javascript
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language typescript
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language java
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language cpp
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language c
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language go
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language rust
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language kotlin
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language swift
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language ruby
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language csharp
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language scala
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language php
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm java java 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm c c 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm go go 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm rust rust 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm swift swift 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm scala scala 1129_shortest_path_with_alternating_colors
docker compose -f docker/docker-compose.yml run --rm php php 1129_shortest_path_with_alternating_colors
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1129_shortest_path_with_alternating_colors` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1129_shortest_path_with_alternating_colors` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1129_shortest_path_with_alternating_colors` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1129_shortest_path_with_alternating_colors` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1129_shortest_path_with_alternating_colors` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1129_shortest_path_with_alternating_colors` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1129_shortest_path_with_alternating_colors` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1129_shortest_path_with_alternating_colors` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1129_shortest_path_with_alternating_colors` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1129_shortest_path_with_alternating_colors` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1129_shortest_path_with_alternating_colors` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1129_shortest_path_with_alternating_colors` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1129_shortest_path_with_alternating_colors` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1129_shortest_path_with_alternating_colors` |

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
.\scripts\test.ps1 -Folder 1129_shortest_path_with_alternating_colors -AllLanguages
```

```bash
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --all-languages
```

```zsh
./scripts/test.sh --folder 1129_shortest_path_with_alternating_colors --all-languages
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
