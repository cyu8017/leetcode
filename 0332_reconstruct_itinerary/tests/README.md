# Test harness for 0332_reconstruct_itinerary

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0332_reconstruct_itinerary --language python
./scripts/test.sh --folder 0332_reconstruct_itinerary --language javascript
./scripts/test.sh --folder 0332_reconstruct_itinerary --language typescript
./scripts/test.sh --folder 0332_reconstruct_itinerary --language java
./scripts/test.sh --folder 0332_reconstruct_itinerary --language cpp
./scripts/test.sh --folder 0332_reconstruct_itinerary --language c
./scripts/test.sh --folder 0332_reconstruct_itinerary --language go
./scripts/test.sh --folder 0332_reconstruct_itinerary --language rust
./scripts/test.sh --folder 0332_reconstruct_itinerary --language kotlin
./scripts/test.sh --folder 0332_reconstruct_itinerary --language swift
./scripts/test.sh --folder 0332_reconstruct_itinerary --language ruby
./scripts/test.sh --folder 0332_reconstruct_itinerary --language csharp
./scripts/test.sh --folder 0332_reconstruct_itinerary --language scala
./scripts/test.sh --folder 0332_reconstruct_itinerary --language php
./scripts/test.sh --folder 0332_reconstruct_itinerary --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0332_reconstruct_itinerary --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm java java 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm c c 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm go go 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm rust rust 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm swift swift 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm scala scala 0332_reconstruct_itinerary
docker compose -f docker/docker-compose.yml run --rm php php 0332_reconstruct_itinerary
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0332_reconstruct_itinerary` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0332_reconstruct_itinerary` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0332_reconstruct_itinerary` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0332_reconstruct_itinerary` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0332_reconstruct_itinerary` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0332_reconstruct_itinerary` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0332_reconstruct_itinerary` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0332_reconstruct_itinerary` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0332_reconstruct_itinerary` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0332_reconstruct_itinerary` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0332_reconstruct_itinerary` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0332_reconstruct_itinerary` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0332_reconstruct_itinerary` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0332_reconstruct_itinerary` |

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
.\scripts\test.ps1 -Folder 0332_reconstruct_itinerary -AllLanguages
```

```bash
./scripts/test.sh --folder 0332_reconstruct_itinerary --all-languages
```

```zsh
./scripts/test.sh --folder 0332_reconstruct_itinerary --all-languages
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
