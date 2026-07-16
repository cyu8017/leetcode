# Test harness for 1899_merge_triplets_to_form_target_triplet

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language python
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language javascript
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language typescript
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language java
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language cpp
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language c
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language go
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language rust
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language kotlin
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language swift
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language ruby
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language csharp
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language scala
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language php
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm javascript javascript 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm typescript typescript 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm java java 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm cpp cpp 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm c c 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm go go 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm rust rust 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm swift swift 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm ruby ruby 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm csharp csharp 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm scala scala 1899_merge_triplets_to_form_target_triplet
docker compose -f docker/docker-compose.yml run --rm php php 1899_merge_triplets_to_form_target_triplet
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 1899_merge_triplets_to_form_target_triplet` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 1899_merge_triplets_to_form_target_triplet` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 1899_merge_triplets_to_form_target_triplet` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 1899_merge_triplets_to_form_target_triplet` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 1899_merge_triplets_to_form_target_triplet` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 1899_merge_triplets_to_form_target_triplet` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 1899_merge_triplets_to_form_target_triplet` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 1899_merge_triplets_to_form_target_triplet` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 1899_merge_triplets_to_form_target_triplet` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 1899_merge_triplets_to_form_target_triplet` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 1899_merge_triplets_to_form_target_triplet` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 1899_merge_triplets_to_form_target_triplet` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 1899_merge_triplets_to_form_target_triplet` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 1899_merge_triplets_to_form_target_triplet` |

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
.\scripts\test.ps1 -Folder 1899_merge_triplets_to_form_target_triplet -AllLanguages
```

```bash
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --all-languages
```

```zsh
./scripts/test.sh --folder 1899_merge_triplets_to_form_target_triplet --all-languages
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
