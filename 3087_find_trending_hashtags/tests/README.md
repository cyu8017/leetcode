# Test harness for 3087_find_trending_hashtags

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3087_find_trending_hashtags --language python
./scripts/test.sh --folder 3087_find_trending_hashtags --language javascript
./scripts/test.sh --folder 3087_find_trending_hashtags --language typescript
./scripts/test.sh --folder 3087_find_trending_hashtags --language java
./scripts/test.sh --folder 3087_find_trending_hashtags --language cpp
./scripts/test.sh --folder 3087_find_trending_hashtags --language c
./scripts/test.sh --folder 3087_find_trending_hashtags --language go
./scripts/test.sh --folder 3087_find_trending_hashtags --language rust
./scripts/test.sh --folder 3087_find_trending_hashtags --language kotlin
./scripts/test.sh --folder 3087_find_trending_hashtags --language swift
./scripts/test.sh --folder 3087_find_trending_hashtags --language ruby
./scripts/test.sh --folder 3087_find_trending_hashtags --language csharp
./scripts/test.sh --folder 3087_find_trending_hashtags --language scala
./scripts/test.sh --folder 3087_find_trending_hashtags --language php
./scripts/test.sh --folder 3087_find_trending_hashtags --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3087_find_trending_hashtags --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm java java 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm c c 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm go go 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm rust rust 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm swift swift 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm scala scala 3087_find_trending_hashtags
docker compose -f docker/docker-compose.yml run --rm php php 3087_find_trending_hashtags
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3087_find_trending_hashtags` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3087_find_trending_hashtags` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3087_find_trending_hashtags` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3087_find_trending_hashtags` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3087_find_trending_hashtags` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3087_find_trending_hashtags` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3087_find_trending_hashtags` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3087_find_trending_hashtags` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3087_find_trending_hashtags` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3087_find_trending_hashtags` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3087_find_trending_hashtags` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3087_find_trending_hashtags` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3087_find_trending_hashtags` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3087_find_trending_hashtags` |

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
.\scripts\test.ps1 -Folder 3087_find_trending_hashtags -AllLanguages
```

```bash
./scripts/test.sh --folder 3087_find_trending_hashtags --all-languages
```

```zsh
./scripts/test.sh --folder 3087_find_trending_hashtags --all-languages
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
