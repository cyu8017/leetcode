# Test harness for 0458_poor_pigs

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0458_poor_pigs -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0458_poor_pigs --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0458_poor_pigs --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0458_poor_pigs --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0458_poor_pigs --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0458_poor_pigs --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0458_poor_pigs --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0458_poor_pigs --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0458_poor_pigs --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0458_poor_pigs --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0458_poor_pigs --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0458_poor_pigs --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0458_poor_pigs --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0458_poor_pigs --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0458_poor_pigs --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0458_poor_pigs --language python
./scripts/test.sh --folder 0458_poor_pigs --language javascript
./scripts/test.sh --folder 0458_poor_pigs --language typescript
./scripts/test.sh --folder 0458_poor_pigs --language java
./scripts/test.sh --folder 0458_poor_pigs --language cpp
./scripts/test.sh --folder 0458_poor_pigs --language c
./scripts/test.sh --folder 0458_poor_pigs --language go
./scripts/test.sh --folder 0458_poor_pigs --language rust
./scripts/test.sh --folder 0458_poor_pigs --language kotlin
./scripts/test.sh --folder 0458_poor_pigs --language swift
./scripts/test.sh --folder 0458_poor_pigs --language ruby
./scripts/test.sh --folder 0458_poor_pigs --language csharp
./scripts/test.sh --folder 0458_poor_pigs --language scala
./scripts/test.sh --folder 0458_poor_pigs --language php
./scripts/test.sh --folder 0458_poor_pigs --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0458_poor_pigs --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0458_poor_pigs --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0458_poor_pigs --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0458_poor_pigs --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0458_poor_pigs --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0458_poor_pigs --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0458_poor_pigs --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0458_poor_pigs --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0458_poor_pigs --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0458_poor_pigs --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0458_poor_pigs --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0458_poor_pigs --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0458_poor_pigs --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0458_poor_pigs --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm java java 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm c c 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm go go 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm rust rust 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm swift swift 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm scala scala 0458_poor_pigs
docker compose -f docker/docker-compose.yml run --rm php php 0458_poor_pigs
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0458_poor_pigs` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0458_poor_pigs` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0458_poor_pigs` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0458_poor_pigs` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0458_poor_pigs` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0458_poor_pigs` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0458_poor_pigs` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0458_poor_pigs` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0458_poor_pigs` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0458_poor_pigs` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0458_poor_pigs` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0458_poor_pigs` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0458_poor_pigs` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0458_poor_pigs` |

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
.\scripts\test.ps1 -Folder 0458_poor_pigs -AllLanguages
```

```bash
./scripts/test.sh --folder 0458_poor_pigs --all-languages
```

```zsh
./scripts/test.sh --folder 0458_poor_pigs --all-languages
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
