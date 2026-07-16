# Test harness for 0354_russian_doll_envelopes

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0354_russian_doll_envelopes --language python
./scripts/test.sh --folder 0354_russian_doll_envelopes --language javascript
./scripts/test.sh --folder 0354_russian_doll_envelopes --language typescript
./scripts/test.sh --folder 0354_russian_doll_envelopes --language java
./scripts/test.sh --folder 0354_russian_doll_envelopes --language cpp
./scripts/test.sh --folder 0354_russian_doll_envelopes --language c
./scripts/test.sh --folder 0354_russian_doll_envelopes --language go
./scripts/test.sh --folder 0354_russian_doll_envelopes --language rust
./scripts/test.sh --folder 0354_russian_doll_envelopes --language kotlin
./scripts/test.sh --folder 0354_russian_doll_envelopes --language swift
./scripts/test.sh --folder 0354_russian_doll_envelopes --language ruby
./scripts/test.sh --folder 0354_russian_doll_envelopes --language csharp
./scripts/test.sh --folder 0354_russian_doll_envelopes --language scala
./scripts/test.sh --folder 0354_russian_doll_envelopes --language php
./scripts/test.sh --folder 0354_russian_doll_envelopes --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0354_russian_doll_envelopes --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm java java 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm c c 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm go go 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm rust rust 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm swift swift 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm scala scala 0354_russian_doll_envelopes
docker compose -f docker/docker-compose.yml run --rm php php 0354_russian_doll_envelopes
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0354_russian_doll_envelopes` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0354_russian_doll_envelopes` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0354_russian_doll_envelopes` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0354_russian_doll_envelopes` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0354_russian_doll_envelopes` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0354_russian_doll_envelopes` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0354_russian_doll_envelopes` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0354_russian_doll_envelopes` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0354_russian_doll_envelopes` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0354_russian_doll_envelopes` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0354_russian_doll_envelopes` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0354_russian_doll_envelopes` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0354_russian_doll_envelopes` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0354_russian_doll_envelopes` |

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
.\scripts\test.ps1 -Folder 0354_russian_doll_envelopes -AllLanguages
```

```bash
./scripts/test.sh --folder 0354_russian_doll_envelopes --all-languages
```

```zsh
./scripts/test.sh --folder 0354_russian_doll_envelopes --all-languages
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
