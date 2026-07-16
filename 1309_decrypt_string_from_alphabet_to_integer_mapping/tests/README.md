# Test harness for 1309_decrypt_string_from_alphabet_to_integer_mapping

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language python
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language javascript
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language typescript
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language java
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language cpp
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language c
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language go
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language rust
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language kotlin
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language swift
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language ruby
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language csharp
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language scala
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language php
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm java java 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm c c 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm go go 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm rust rust 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm swift swift 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm scala scala 1309_decrypt_string_from_alphabet_to_integer_mapping
docker compose -f docker/docker-compose.yml run --rm php php 1309_decrypt_string_from_alphabet_to_integer_mapping
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1309_decrypt_string_from_alphabet_to_integer_mapping` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1309_decrypt_string_from_alphabet_to_integer_mapping` |

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
.\scripts\test.ps1 -Folder 1309_decrypt_string_from_alphabet_to_integer_mapping -AllLanguages
```

```bash
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --all-languages
```

```zsh
./scripts/test.sh --folder 1309_decrypt_string_from_alphabet_to_integer_mapping --all-languages
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
