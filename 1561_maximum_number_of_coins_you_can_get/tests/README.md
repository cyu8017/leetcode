# Test harness for 1561_maximum_number_of_coins_you_can_get

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language python
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language javascript
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language typescript
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language java
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language cpp
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language c
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language go
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language rust
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language kotlin
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language swift
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language ruby
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language csharp
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language scala
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language php
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm java java 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm c c 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm go go 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm rust rust 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm swift swift 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm scala scala 1561_maximum_number_of_coins_you_can_get
docker compose -f docker/docker-compose.yml run --rm php php 1561_maximum_number_of_coins_you_can_get
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1561_maximum_number_of_coins_you_can_get` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1561_maximum_number_of_coins_you_can_get` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1561_maximum_number_of_coins_you_can_get` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1561_maximum_number_of_coins_you_can_get` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1561_maximum_number_of_coins_you_can_get` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1561_maximum_number_of_coins_you_can_get` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1561_maximum_number_of_coins_you_can_get` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1561_maximum_number_of_coins_you_can_get` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1561_maximum_number_of_coins_you_can_get` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1561_maximum_number_of_coins_you_can_get` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1561_maximum_number_of_coins_you_can_get` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1561_maximum_number_of_coins_you_can_get` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1561_maximum_number_of_coins_you_can_get` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1561_maximum_number_of_coins_you_can_get` |

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
.\scripts\test.ps1 -Folder 1561_maximum_number_of_coins_you_can_get -AllLanguages
```

```bash
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --all-languages
```

```zsh
./scripts/test.sh --folder 1561_maximum_number_of_coins_you_can_get --all-languages
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
