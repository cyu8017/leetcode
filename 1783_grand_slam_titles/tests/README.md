# Test harness for 1783_grand_slam_titles

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1783_grand_slam_titles -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1783_grand_slam_titles --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1783_grand_slam_titles --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1783_grand_slam_titles --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1783_grand_slam_titles --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1783_grand_slam_titles --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1783_grand_slam_titles --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1783_grand_slam_titles --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1783_grand_slam_titles --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1783_grand_slam_titles --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1783_grand_slam_titles --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1783_grand_slam_titles --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1783_grand_slam_titles --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1783_grand_slam_titles --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1783_grand_slam_titles --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1783_grand_slam_titles --language python
./scripts/test.sh --folder 1783_grand_slam_titles --language javascript
./scripts/test.sh --folder 1783_grand_slam_titles --language typescript
./scripts/test.sh --folder 1783_grand_slam_titles --language java
./scripts/test.sh --folder 1783_grand_slam_titles --language cpp
./scripts/test.sh --folder 1783_grand_slam_titles --language c
./scripts/test.sh --folder 1783_grand_slam_titles --language go
./scripts/test.sh --folder 1783_grand_slam_titles --language rust
./scripts/test.sh --folder 1783_grand_slam_titles --language kotlin
./scripts/test.sh --folder 1783_grand_slam_titles --language swift
./scripts/test.sh --folder 1783_grand_slam_titles --language ruby
./scripts/test.sh --folder 1783_grand_slam_titles --language csharp
./scripts/test.sh --folder 1783_grand_slam_titles --language scala
./scripts/test.sh --folder 1783_grand_slam_titles --language php
./scripts/test.sh --folder 1783_grand_slam_titles --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1783_grand_slam_titles --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1783_grand_slam_titles --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1783_grand_slam_titles --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1783_grand_slam_titles --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1783_grand_slam_titles --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1783_grand_slam_titles --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1783_grand_slam_titles --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1783_grand_slam_titles --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1783_grand_slam_titles --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1783_grand_slam_titles --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1783_grand_slam_titles --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1783_grand_slam_titles --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1783_grand_slam_titles --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1783_grand_slam_titles --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm java java 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm c c 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm go go 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm rust rust 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm swift swift 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm scala scala 1783_grand_slam_titles
docker compose -f docker/docker-compose.yml run --rm php php 1783_grand_slam_titles
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1783_grand_slam_titles` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1783_grand_slam_titles` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1783_grand_slam_titles` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1783_grand_slam_titles` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1783_grand_slam_titles` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1783_grand_slam_titles` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1783_grand_slam_titles` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1783_grand_slam_titles` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1783_grand_slam_titles` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1783_grand_slam_titles` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1783_grand_slam_titles` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1783_grand_slam_titles` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1783_grand_slam_titles` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1783_grand_slam_titles` |

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
.\scripts\test.ps1 -Folder 1783_grand_slam_titles -AllLanguages
```

```bash
./scripts/test.sh --folder 1783_grand_slam_titles --all-languages
```

```zsh
./scripts/test.sh --folder 1783_grand_slam_titles --all-languages
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
