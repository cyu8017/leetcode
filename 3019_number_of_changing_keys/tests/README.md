# Test harness for 3019_number_of_changing_keys

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3019_number_of_changing_keys --language python
./scripts/test.sh --folder 3019_number_of_changing_keys --language javascript
./scripts/test.sh --folder 3019_number_of_changing_keys --language typescript
./scripts/test.sh --folder 3019_number_of_changing_keys --language java
./scripts/test.sh --folder 3019_number_of_changing_keys --language cpp
./scripts/test.sh --folder 3019_number_of_changing_keys --language c
./scripts/test.sh --folder 3019_number_of_changing_keys --language go
./scripts/test.sh --folder 3019_number_of_changing_keys --language rust
./scripts/test.sh --folder 3019_number_of_changing_keys --language kotlin
./scripts/test.sh --folder 3019_number_of_changing_keys --language swift
./scripts/test.sh --folder 3019_number_of_changing_keys --language ruby
./scripts/test.sh --folder 3019_number_of_changing_keys --language csharp
./scripts/test.sh --folder 3019_number_of_changing_keys --language scala
./scripts/test.sh --folder 3019_number_of_changing_keys --language php
./scripts/test.sh --folder 3019_number_of_changing_keys --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3019_number_of_changing_keys --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm java java 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm c c 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm go go 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm rust rust 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm swift swift 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm scala scala 3019_number_of_changing_keys
docker compose -f docker/docker-compose.yml run --rm php php 3019_number_of_changing_keys
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3019_number_of_changing_keys` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3019_number_of_changing_keys` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3019_number_of_changing_keys` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3019_number_of_changing_keys` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3019_number_of_changing_keys` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3019_number_of_changing_keys` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3019_number_of_changing_keys` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3019_number_of_changing_keys` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3019_number_of_changing_keys` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3019_number_of_changing_keys` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3019_number_of_changing_keys` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3019_number_of_changing_keys` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3019_number_of_changing_keys` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3019_number_of_changing_keys` |

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
.\scripts\test.ps1 -Folder 3019_number_of_changing_keys -AllLanguages
```

```bash
./scripts/test.sh --folder 3019_number_of_changing_keys --all-languages
```

```zsh
./scripts/test.sh --folder 3019_number_of_changing_keys --all-languages
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
