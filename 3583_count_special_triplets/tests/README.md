# Test harness for 3583_count_special_triplets

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3583_count_special_triplets -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3583_count_special_triplets --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3583_count_special_triplets --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3583_count_special_triplets --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3583_count_special_triplets --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3583_count_special_triplets --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3583_count_special_triplets --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3583_count_special_triplets --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3583_count_special_triplets --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3583_count_special_triplets --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3583_count_special_triplets --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3583_count_special_triplets --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3583_count_special_triplets --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3583_count_special_triplets --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3583_count_special_triplets --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3583_count_special_triplets --language python
./scripts/test.sh --folder 3583_count_special_triplets --language javascript
./scripts/test.sh --folder 3583_count_special_triplets --language typescript
./scripts/test.sh --folder 3583_count_special_triplets --language java
./scripts/test.sh --folder 3583_count_special_triplets --language cpp
./scripts/test.sh --folder 3583_count_special_triplets --language c
./scripts/test.sh --folder 3583_count_special_triplets --language go
./scripts/test.sh --folder 3583_count_special_triplets --language rust
./scripts/test.sh --folder 3583_count_special_triplets --language kotlin
./scripts/test.sh --folder 3583_count_special_triplets --language swift
./scripts/test.sh --folder 3583_count_special_triplets --language ruby
./scripts/test.sh --folder 3583_count_special_triplets --language csharp
./scripts/test.sh --folder 3583_count_special_triplets --language scala
./scripts/test.sh --folder 3583_count_special_triplets --language php
./scripts/test.sh --folder 3583_count_special_triplets --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3583_count_special_triplets --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3583_count_special_triplets --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3583_count_special_triplets --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3583_count_special_triplets --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3583_count_special_triplets --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3583_count_special_triplets --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3583_count_special_triplets --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3583_count_special_triplets --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3583_count_special_triplets --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3583_count_special_triplets --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3583_count_special_triplets --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3583_count_special_triplets --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3583_count_special_triplets --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3583_count_special_triplets --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm java java 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm c c 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm go go 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm rust rust 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm swift swift 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm scala scala 3583_count_special_triplets
docker compose -f docker/docker-compose.yml run --rm php php 3583_count_special_triplets
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3583_count_special_triplets` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3583_count_special_triplets` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3583_count_special_triplets` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3583_count_special_triplets` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3583_count_special_triplets` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3583_count_special_triplets` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3583_count_special_triplets` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3583_count_special_triplets` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3583_count_special_triplets` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3583_count_special_triplets` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3583_count_special_triplets` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3583_count_special_triplets` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3583_count_special_triplets` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3583_count_special_triplets` |

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
.\scripts\test.ps1 -Folder 3583_count_special_triplets -AllLanguages
```

```bash
./scripts/test.sh --folder 3583_count_special_triplets --all-languages
```

```zsh
./scripts/test.sh --folder 3583_count_special_triplets --all-languages
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
