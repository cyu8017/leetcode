# Test harness for 2092_find_all_people_with_secret

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 2092_find_all_people_with_secret --language python
./scripts/test.sh --folder 2092_find_all_people_with_secret --language javascript
./scripts/test.sh --folder 2092_find_all_people_with_secret --language typescript
./scripts/test.sh --folder 2092_find_all_people_with_secret --language java
./scripts/test.sh --folder 2092_find_all_people_with_secret --language cpp
./scripts/test.sh --folder 2092_find_all_people_with_secret --language c
./scripts/test.sh --folder 2092_find_all_people_with_secret --language go
./scripts/test.sh --folder 2092_find_all_people_with_secret --language rust
./scripts/test.sh --folder 2092_find_all_people_with_secret --language kotlin
./scripts/test.sh --folder 2092_find_all_people_with_secret --language swift
./scripts/test.sh --folder 2092_find_all_people_with_secret --language ruby
./scripts/test.sh --folder 2092_find_all_people_with_secret --language csharp
./scripts/test.sh --folder 2092_find_all_people_with_secret --language scala
./scripts/test.sh --folder 2092_find_all_people_with_secret --language php
./scripts/test.sh --folder 2092_find_all_people_with_secret --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 2092_find_all_people_with_secret --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm javascript javascript 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm typescript typescript 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm java java 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm cpp cpp 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm c c 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm go go 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm rust rust 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm swift swift 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm ruby ruby 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm csharp csharp 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm scala scala 2092_find_all_people_with_secret
docker compose -f docker/docker-compose.yml run --rm php php 2092_find_all_people_with_secret
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 2092_find_all_people_with_secret` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 2092_find_all_people_with_secret` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 2092_find_all_people_with_secret` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 2092_find_all_people_with_secret` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 2092_find_all_people_with_secret` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 2092_find_all_people_with_secret` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 2092_find_all_people_with_secret` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 2092_find_all_people_with_secret` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 2092_find_all_people_with_secret` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 2092_find_all_people_with_secret` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 2092_find_all_people_with_secret` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 2092_find_all_people_with_secret` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 2092_find_all_people_with_secret` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 2092_find_all_people_with_secret` |

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
.\scripts\test.ps1 -Folder 2092_find_all_people_with_secret -AllLanguages
```

```bash
./scripts/test.sh --folder 2092_find_all_people_with_secret --all-languages
```

```zsh
./scripts/test.sh --folder 2092_find_all_people_with_secret --all-languages
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
