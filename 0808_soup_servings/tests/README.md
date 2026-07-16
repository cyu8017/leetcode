# Test harness for 0808_soup_servings

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0808_soup_servings -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0808_soup_servings --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0808_soup_servings --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0808_soup_servings --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0808_soup_servings --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0808_soup_servings --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0808_soup_servings --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0808_soup_servings --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0808_soup_servings --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0808_soup_servings --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0808_soup_servings --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0808_soup_servings --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0808_soup_servings --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0808_soup_servings --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0808_soup_servings --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0808_soup_servings --language python
./scripts/test.sh --folder 0808_soup_servings --language javascript
./scripts/test.sh --folder 0808_soup_servings --language typescript
./scripts/test.sh --folder 0808_soup_servings --language java
./scripts/test.sh --folder 0808_soup_servings --language cpp
./scripts/test.sh --folder 0808_soup_servings --language c
./scripts/test.sh --folder 0808_soup_servings --language go
./scripts/test.sh --folder 0808_soup_servings --language rust
./scripts/test.sh --folder 0808_soup_servings --language kotlin
./scripts/test.sh --folder 0808_soup_servings --language swift
./scripts/test.sh --folder 0808_soup_servings --language ruby
./scripts/test.sh --folder 0808_soup_servings --language csharp
./scripts/test.sh --folder 0808_soup_servings --language scala
./scripts/test.sh --folder 0808_soup_servings --language php
./scripts/test.sh --folder 0808_soup_servings --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0808_soup_servings --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0808_soup_servings --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0808_soup_servings --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0808_soup_servings --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0808_soup_servings --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0808_soup_servings --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0808_soup_servings --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0808_soup_servings --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0808_soup_servings --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0808_soup_servings --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0808_soup_servings --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0808_soup_servings --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0808_soup_servings --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0808_soup_servings --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm java java 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm c c 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm go go 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm rust rust 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm swift swift 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm scala scala 0808_soup_servings
docker compose -f docker/docker-compose.yml run --rm php php 0808_soup_servings
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0808_soup_servings` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0808_soup_servings` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0808_soup_servings` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0808_soup_servings` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0808_soup_servings` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0808_soup_servings` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0808_soup_servings` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0808_soup_servings` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0808_soup_servings` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0808_soup_servings` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0808_soup_servings` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0808_soup_servings` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0808_soup_servings` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0808_soup_servings` |

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
.\scripts\test.ps1 -Folder 0808_soup_servings -AllLanguages
```

```bash
./scripts/test.sh --folder 0808_soup_servings --all-languages
```

```zsh
./scripts/test.sh --folder 0808_soup_servings --all-languages
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
