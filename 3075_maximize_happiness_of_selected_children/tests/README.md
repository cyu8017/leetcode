# Test harness for 3075_maximize_happiness_of_selected_children

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language python
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language javascript
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language typescript
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language java
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language cpp
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language c
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language go
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language rust
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language kotlin
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language swift
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language ruby
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language csharp
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language scala
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language php
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm java java 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm c c 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm go go 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm rust rust 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm swift swift 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm scala scala 3075_maximize_happiness_of_selected_children
docker compose -f docker/docker-compose.yml run --rm php php 3075_maximize_happiness_of_selected_children
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3075_maximize_happiness_of_selected_children` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3075_maximize_happiness_of_selected_children` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3075_maximize_happiness_of_selected_children` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3075_maximize_happiness_of_selected_children` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3075_maximize_happiness_of_selected_children` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3075_maximize_happiness_of_selected_children` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3075_maximize_happiness_of_selected_children` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3075_maximize_happiness_of_selected_children` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3075_maximize_happiness_of_selected_children` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3075_maximize_happiness_of_selected_children` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3075_maximize_happiness_of_selected_children` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3075_maximize_happiness_of_selected_children` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3075_maximize_happiness_of_selected_children` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3075_maximize_happiness_of_selected_children` |

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
.\scripts\test.ps1 -Folder 3075_maximize_happiness_of_selected_children -AllLanguages
```

```bash
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --all-languages
```

```zsh
./scripts/test.sh --folder 3075_maximize_happiness_of_selected_children --all-languages
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
