# Test harness for 1153_string_transforms_into_another_string

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language python
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language javascript
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language typescript
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language java
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language cpp
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language c
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language go
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language rust
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language kotlin
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language swift
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language ruby
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language csharp
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language scala
./scripts/test.sh --folder 1153_string_transforms_into_another_string --language php
./scripts/test.sh --folder 1153_string_transforms_into_another_string --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1153_string_transforms_into_another_string --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm java java 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm c c 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm go go 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm rust rust 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm swift swift 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm scala scala 1153_string_transforms_into_another_string
docker compose -f docker/docker-compose.yml run --rm php php 1153_string_transforms_into_another_string
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1153_string_transforms_into_another_string` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1153_string_transforms_into_another_string` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1153_string_transforms_into_another_string` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1153_string_transforms_into_another_string` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1153_string_transforms_into_another_string` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1153_string_transforms_into_another_string` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1153_string_transforms_into_another_string` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1153_string_transforms_into_another_string` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1153_string_transforms_into_another_string` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1153_string_transforms_into_another_string` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1153_string_transforms_into_another_string` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1153_string_transforms_into_another_string` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1153_string_transforms_into_another_string` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1153_string_transforms_into_another_string` |

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
.\scripts\test.ps1 -Folder 1153_string_transforms_into_another_string -AllLanguages
```

```bash
./scripts/test.sh --folder 1153_string_transforms_into_another_string --all-languages
```

```zsh
./scripts/test.sh --folder 1153_string_transforms_into_another_string --all-languages
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
