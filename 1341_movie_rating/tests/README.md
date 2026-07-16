# Test harness for 1341_movie_rating

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1341_movie_rating -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1341_movie_rating --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1341_movie_rating --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1341_movie_rating --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1341_movie_rating --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1341_movie_rating --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1341_movie_rating --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1341_movie_rating --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1341_movie_rating --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1341_movie_rating --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1341_movie_rating --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1341_movie_rating --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1341_movie_rating --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1341_movie_rating --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1341_movie_rating --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1341_movie_rating --language python
./scripts/test.sh --folder 1341_movie_rating --language javascript
./scripts/test.sh --folder 1341_movie_rating --language typescript
./scripts/test.sh --folder 1341_movie_rating --language java
./scripts/test.sh --folder 1341_movie_rating --language cpp
./scripts/test.sh --folder 1341_movie_rating --language c
./scripts/test.sh --folder 1341_movie_rating --language go
./scripts/test.sh --folder 1341_movie_rating --language rust
./scripts/test.sh --folder 1341_movie_rating --language kotlin
./scripts/test.sh --folder 1341_movie_rating --language swift
./scripts/test.sh --folder 1341_movie_rating --language ruby
./scripts/test.sh --folder 1341_movie_rating --language csharp
./scripts/test.sh --folder 1341_movie_rating --language scala
./scripts/test.sh --folder 1341_movie_rating --language php
./scripts/test.sh --folder 1341_movie_rating --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1341_movie_rating --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1341_movie_rating --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1341_movie_rating --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1341_movie_rating --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1341_movie_rating --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1341_movie_rating --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1341_movie_rating --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1341_movie_rating --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1341_movie_rating --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1341_movie_rating --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1341_movie_rating --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1341_movie_rating --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1341_movie_rating --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1341_movie_rating --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm java java 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm c c 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm go go 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm rust rust 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm swift swift 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm scala scala 1341_movie_rating
docker compose -f docker/docker-compose.yml run --rm php php 1341_movie_rating
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1341_movie_rating` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1341_movie_rating` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1341_movie_rating` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1341_movie_rating` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1341_movie_rating` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1341_movie_rating` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1341_movie_rating` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1341_movie_rating` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1341_movie_rating` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1341_movie_rating` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1341_movie_rating` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1341_movie_rating` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1341_movie_rating` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1341_movie_rating` |

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
.\scripts\test.ps1 -Folder 1341_movie_rating -AllLanguages
```

```bash
./scripts/test.sh --folder 1341_movie_rating --all-languages
```

```zsh
./scripts/test.sh --folder 1341_movie_rating --all-languages
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
