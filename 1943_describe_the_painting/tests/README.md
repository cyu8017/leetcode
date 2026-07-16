# Test harness for 1943_describe_the_painting

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1943_describe_the_painting -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1943_describe_the_painting --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1943_describe_the_painting --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1943_describe_the_painting --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1943_describe_the_painting --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1943_describe_the_painting --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1943_describe_the_painting --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1943_describe_the_painting --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1943_describe_the_painting --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1943_describe_the_painting --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1943_describe_the_painting --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1943_describe_the_painting --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1943_describe_the_painting --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1943_describe_the_painting --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1943_describe_the_painting --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1943_describe_the_painting --language python
./scripts/test.sh --folder 1943_describe_the_painting --language javascript
./scripts/test.sh --folder 1943_describe_the_painting --language typescript
./scripts/test.sh --folder 1943_describe_the_painting --language java
./scripts/test.sh --folder 1943_describe_the_painting --language cpp
./scripts/test.sh --folder 1943_describe_the_painting --language c
./scripts/test.sh --folder 1943_describe_the_painting --language go
./scripts/test.sh --folder 1943_describe_the_painting --language rust
./scripts/test.sh --folder 1943_describe_the_painting --language kotlin
./scripts/test.sh --folder 1943_describe_the_painting --language swift
./scripts/test.sh --folder 1943_describe_the_painting --language ruby
./scripts/test.sh --folder 1943_describe_the_painting --language csharp
./scripts/test.sh --folder 1943_describe_the_painting --language scala
./scripts/test.sh --folder 1943_describe_the_painting --language php
./scripts/test.sh --folder 1943_describe_the_painting --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1943_describe_the_painting --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1943_describe_the_painting --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1943_describe_the_painting --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1943_describe_the_painting --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1943_describe_the_painting --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1943_describe_the_painting --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1943_describe_the_painting --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1943_describe_the_painting --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1943_describe_the_painting --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1943_describe_the_painting --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1943_describe_the_painting --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1943_describe_the_painting --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1943_describe_the_painting --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1943_describe_the_painting --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm java java 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm c c 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm go go 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm rust rust 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm swift swift 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm scala scala 1943_describe_the_painting
docker compose -f docker/docker-compose.yml run --rm php php 1943_describe_the_painting
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1943_describe_the_painting` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1943_describe_the_painting` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1943_describe_the_painting` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1943_describe_the_painting` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1943_describe_the_painting` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1943_describe_the_painting` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1943_describe_the_painting` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1943_describe_the_painting` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1943_describe_the_painting` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1943_describe_the_painting` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1943_describe_the_painting` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1943_describe_the_painting` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1943_describe_the_painting` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1943_describe_the_painting` |

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
.\scripts\test.ps1 -Folder 1943_describe_the_painting -AllLanguages
```

```bash
./scripts/test.sh --folder 1943_describe_the_painting --all-languages
```

```zsh
./scripts/test.sh --folder 1943_describe_the_painting --all-languages
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
