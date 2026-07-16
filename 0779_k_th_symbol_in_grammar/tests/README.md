# Test harness for 0779_k_th_symbol_in_grammar

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language python
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language javascript
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language typescript
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language java
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language cpp
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language c
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language go
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language rust
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language kotlin
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language swift
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language ruby
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language csharp
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language scala
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language php
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm java java 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm c c 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm go go 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm rust rust 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm swift swift 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm scala scala 0779_k_th_symbol_in_grammar
docker compose -f docker/docker-compose.yml run --rm php php 0779_k_th_symbol_in_grammar
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0779_k_th_symbol_in_grammar` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0779_k_th_symbol_in_grammar` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0779_k_th_symbol_in_grammar` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0779_k_th_symbol_in_grammar` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0779_k_th_symbol_in_grammar` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0779_k_th_symbol_in_grammar` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0779_k_th_symbol_in_grammar` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0779_k_th_symbol_in_grammar` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0779_k_th_symbol_in_grammar` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0779_k_th_symbol_in_grammar` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0779_k_th_symbol_in_grammar` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0779_k_th_symbol_in_grammar` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0779_k_th_symbol_in_grammar` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0779_k_th_symbol_in_grammar` |

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
.\scripts\test.ps1 -Folder 0779_k_th_symbol_in_grammar -AllLanguages
```

```bash
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --all-languages
```

```zsh
./scripts/test.sh --folder 0779_k_th_symbol_in_grammar --all-languages
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
