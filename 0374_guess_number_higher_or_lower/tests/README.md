# Test harness for 0374_guess_number_higher_or_lower

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language python
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language javascript
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language typescript
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language java
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language cpp
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language c
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language go
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language rust
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language kotlin
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language swift
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language ruby
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language csharp
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language scala
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language php
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0374_guess_number_higher_or_lower --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm java java 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm c c 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm go go 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm rust rust 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm swift swift 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm scala scala 0374_guess_number_higher_or_lower
docker compose -f docker/docker-compose.yml run --rm php php 0374_guess_number_higher_or_lower
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0374_guess_number_higher_or_lower` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0374_guess_number_higher_or_lower` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0374_guess_number_higher_or_lower` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0374_guess_number_higher_or_lower` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0374_guess_number_higher_or_lower` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0374_guess_number_higher_or_lower` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0374_guess_number_higher_or_lower` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0374_guess_number_higher_or_lower` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0374_guess_number_higher_or_lower` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0374_guess_number_higher_or_lower` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0374_guess_number_higher_or_lower` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0374_guess_number_higher_or_lower` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0374_guess_number_higher_or_lower` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0374_guess_number_higher_or_lower` |

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
.\scripts\test.ps1 -Folder 0374_guess_number_higher_or_lower -AllLanguages
```

```bash
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --all-languages
```

```zsh
./scripts/test.sh --folder 0374_guess_number_higher_or_lower --all-languages
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
