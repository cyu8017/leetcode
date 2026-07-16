# Test harness for 2296_design_a_text_editor

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2296_design_a_text_editor -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2296_design_a_text_editor --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2296_design_a_text_editor --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2296_design_a_text_editor --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2296_design_a_text_editor --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2296_design_a_text_editor --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2296_design_a_text_editor --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2296_design_a_text_editor --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2296_design_a_text_editor --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2296_design_a_text_editor --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2296_design_a_text_editor --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2296_design_a_text_editor --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2296_design_a_text_editor --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2296_design_a_text_editor --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2296_design_a_text_editor --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2296_design_a_text_editor --language python
./scripts/test.sh --folder 2296_design_a_text_editor --language javascript
./scripts/test.sh --folder 2296_design_a_text_editor --language typescript
./scripts/test.sh --folder 2296_design_a_text_editor --language java
./scripts/test.sh --folder 2296_design_a_text_editor --language cpp
./scripts/test.sh --folder 2296_design_a_text_editor --language c
./scripts/test.sh --folder 2296_design_a_text_editor --language go
./scripts/test.sh --folder 2296_design_a_text_editor --language rust
./scripts/test.sh --folder 2296_design_a_text_editor --language kotlin
./scripts/test.sh --folder 2296_design_a_text_editor --language swift
./scripts/test.sh --folder 2296_design_a_text_editor --language ruby
./scripts/test.sh --folder 2296_design_a_text_editor --language csharp
./scripts/test.sh --folder 2296_design_a_text_editor --language scala
./scripts/test.sh --folder 2296_design_a_text_editor --language php
./scripts/test.sh --folder 2296_design_a_text_editor --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2296_design_a_text_editor --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2296_design_a_text_editor --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2296_design_a_text_editor --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2296_design_a_text_editor --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2296_design_a_text_editor --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2296_design_a_text_editor --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2296_design_a_text_editor --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2296_design_a_text_editor --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2296_design_a_text_editor --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2296_design_a_text_editor --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2296_design_a_text_editor --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2296_design_a_text_editor --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2296_design_a_text_editor --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2296_design_a_text_editor --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm java java 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm c c 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm go go 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm rust rust 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm swift swift 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm scala scala 2296_design_a_text_editor
docker compose -f docker/docker-compose.yml run --rm php php 2296_design_a_text_editor
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2296_design_a_text_editor` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2296_design_a_text_editor` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2296_design_a_text_editor` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2296_design_a_text_editor` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2296_design_a_text_editor` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2296_design_a_text_editor` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2296_design_a_text_editor` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2296_design_a_text_editor` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2296_design_a_text_editor` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2296_design_a_text_editor` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2296_design_a_text_editor` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2296_design_a_text_editor` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2296_design_a_text_editor` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2296_design_a_text_editor` |

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
.\scripts\test.ps1 -Folder 2296_design_a_text_editor -AllLanguages
```

```bash
./scripts/test.sh --folder 2296_design_a_text_editor --all-languages
```

```zsh
./scripts/test.sh --folder 2296_design_a_text_editor --all-languages
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
