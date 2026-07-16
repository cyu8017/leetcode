# Test harness for 3475_dna_pattern_recognition

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 3475_dna_pattern_recognition --language python
./scripts/test.sh --folder 3475_dna_pattern_recognition --language javascript
./scripts/test.sh --folder 3475_dna_pattern_recognition --language typescript
./scripts/test.sh --folder 3475_dna_pattern_recognition --language java
./scripts/test.sh --folder 3475_dna_pattern_recognition --language cpp
./scripts/test.sh --folder 3475_dna_pattern_recognition --language c
./scripts/test.sh --folder 3475_dna_pattern_recognition --language go
./scripts/test.sh --folder 3475_dna_pattern_recognition --language rust
./scripts/test.sh --folder 3475_dna_pattern_recognition --language kotlin
./scripts/test.sh --folder 3475_dna_pattern_recognition --language swift
./scripts/test.sh --folder 3475_dna_pattern_recognition --language ruby
./scripts/test.sh --folder 3475_dna_pattern_recognition --language csharp
./scripts/test.sh --folder 3475_dna_pattern_recognition --language scala
./scripts/test.sh --folder 3475_dna_pattern_recognition --language php
./scripts/test.sh --folder 3475_dna_pattern_recognition --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 3475_dna_pattern_recognition --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm javascript javascript 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm typescript typescript 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm java java 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm cpp cpp 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm c c 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm go go 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm rust rust 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm swift swift 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm ruby ruby 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm csharp csharp 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm scala scala 3475_dna_pattern_recognition
docker compose -f docker/docker-compose.yml run --rm php php 3475_dna_pattern_recognition
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 3475_dna_pattern_recognition` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 3475_dna_pattern_recognition` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 3475_dna_pattern_recognition` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 3475_dna_pattern_recognition` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 3475_dna_pattern_recognition` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 3475_dna_pattern_recognition` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 3475_dna_pattern_recognition` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 3475_dna_pattern_recognition` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 3475_dna_pattern_recognition` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 3475_dna_pattern_recognition` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 3475_dna_pattern_recognition` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 3475_dna_pattern_recognition` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 3475_dna_pattern_recognition` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 3475_dna_pattern_recognition` |

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
.\scripts\test.ps1 -Folder 3475_dna_pattern_recognition -AllLanguages
```

```bash
./scripts/test.sh --folder 3475_dna_pattern_recognition --all-languages
```

```zsh
./scripts/test.sh --folder 3475_dna_pattern_recognition --all-languages
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
