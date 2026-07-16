# Test harness for 0089_gray_code

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0089_gray_code -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0089_gray_code --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0089_gray_code --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0089_gray_code --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0089_gray_code --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0089_gray_code --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0089_gray_code --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0089_gray_code --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0089_gray_code --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0089_gray_code --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0089_gray_code --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0089_gray_code --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0089_gray_code --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0089_gray_code --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0089_gray_code --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0089_gray_code --language python
./scripts/test.sh --folder 0089_gray_code --language javascript
./scripts/test.sh --folder 0089_gray_code --language typescript
./scripts/test.sh --folder 0089_gray_code --language java
./scripts/test.sh --folder 0089_gray_code --language cpp
./scripts/test.sh --folder 0089_gray_code --language c
./scripts/test.sh --folder 0089_gray_code --language go
./scripts/test.sh --folder 0089_gray_code --language rust
./scripts/test.sh --folder 0089_gray_code --language kotlin
./scripts/test.sh --folder 0089_gray_code --language swift
./scripts/test.sh --folder 0089_gray_code --language ruby
./scripts/test.sh --folder 0089_gray_code --language csharp
./scripts/test.sh --folder 0089_gray_code --language scala
./scripts/test.sh --folder 0089_gray_code --language php
./scripts/test.sh --folder 0089_gray_code --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0089_gray_code --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0089_gray_code --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0089_gray_code --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0089_gray_code --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0089_gray_code --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0089_gray_code --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0089_gray_code --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0089_gray_code --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0089_gray_code --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0089_gray_code --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0089_gray_code --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0089_gray_code --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0089_gray_code --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0089_gray_code --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm java java 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm c c 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm go go 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm rust rust 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm swift swift 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm scala scala 0089_gray_code
docker compose -f docker/docker-compose.yml run --rm php php 0089_gray_code
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0089_gray_code` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0089_gray_code` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0089_gray_code` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0089_gray_code` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0089_gray_code` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0089_gray_code` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0089_gray_code` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0089_gray_code` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0089_gray_code` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0089_gray_code` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0089_gray_code` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0089_gray_code` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0089_gray_code` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0089_gray_code` |

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
.\scripts\test.ps1 -Folder 0089_gray_code -AllLanguages
```

```bash
./scripts/test.sh --folder 0089_gray_code --all-languages
```

```zsh
./scripts/test.sh --folder 0089_gray_code --all-languages
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
