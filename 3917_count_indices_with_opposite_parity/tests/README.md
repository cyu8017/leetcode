# Test harness for 3917_count_indices_with_opposite_parity

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language python
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language javascript
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language typescript
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language java
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language cpp
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language c
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language go
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language rust
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language kotlin
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language swift
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language ruby
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language csharp
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language scala
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language php
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm java java 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm c c 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm go go 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm rust rust 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm swift swift 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm scala scala 3917_count_indices_with_opposite_parity
docker compose -f docker/docker-compose.yml run --rm php php 3917_count_indices_with_opposite_parity
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3917_count_indices_with_opposite_parity` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3917_count_indices_with_opposite_parity` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3917_count_indices_with_opposite_parity` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3917_count_indices_with_opposite_parity` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3917_count_indices_with_opposite_parity` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3917_count_indices_with_opposite_parity` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3917_count_indices_with_opposite_parity` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3917_count_indices_with_opposite_parity` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3917_count_indices_with_opposite_parity` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3917_count_indices_with_opposite_parity` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3917_count_indices_with_opposite_parity` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3917_count_indices_with_opposite_parity` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3917_count_indices_with_opposite_parity` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3917_count_indices_with_opposite_parity` |

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
.\scripts\test.ps1 -Folder 3917_count_indices_with_opposite_parity -AllLanguages
```

```bash
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --all-languages
```

```zsh
./scripts/test.sh --folder 3917_count_indices_with_opposite_parity --all-languages
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
