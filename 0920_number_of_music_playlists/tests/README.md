# Test harness for 0920_number_of_music_playlists

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
| Python | `solution.py` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language python` |
| JavaScript | `solution.js` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language javascript` |
| TypeScript | `solution.ts` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language typescript` |
| Java | `Solution.java` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language java` |
| C++ | `solution.cpp` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language cpp` |
| C | `solution.c` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language c` |
| Go | `solution.go` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language go` |
| Rust | `solution.rs` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language rust` |
| Kotlin | `Solution.kt` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language kotlin` |
| Swift | `Solution.swift` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language swift` |
| Ruby | `solution.rb` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language ruby` |
| C# | `Solution.cs` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language csharp` |
| Scala | `Solution.scala` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language scala` |
| PHP | `solution.php` | `.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -Language php` |

### macOS / Linux (`scripts/test.sh`)

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language php` |

### zsh (macOS default shell)

Run from the repository root:

```zsh
./scripts/test.sh --folder 0920_number_of_music_playlists --language python
./scripts/test.sh --folder 0920_number_of_music_playlists --language javascript
./scripts/test.sh --folder 0920_number_of_music_playlists --language typescript
./scripts/test.sh --folder 0920_number_of_music_playlists --language java
./scripts/test.sh --folder 0920_number_of_music_playlists --language cpp
./scripts/test.sh --folder 0920_number_of_music_playlists --language c
./scripts/test.sh --folder 0920_number_of_music_playlists --language go
./scripts/test.sh --folder 0920_number_of_music_playlists --language rust
./scripts/test.sh --folder 0920_number_of_music_playlists --language kotlin
./scripts/test.sh --folder 0920_number_of_music_playlists --language swift
./scripts/test.sh --folder 0920_number_of_music_playlists --language ruby
./scripts/test.sh --folder 0920_number_of_music_playlists --language csharp
./scripts/test.sh --folder 0920_number_of_music_playlists --language scala
./scripts/test.sh --folder 0920_number_of_music_playlists --language php
./scripts/test.sh --folder 0920_number_of_music_playlists --all-languages
```

| Language | Solution file | Command |
|----------|---------------|---------|
| Python | `solution.py` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language python` |
| JavaScript | `solution.js` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language javascript` |
| TypeScript | `solution.ts` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language typescript` |
| Java | `Solution.java` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language java` |
| C++ | `solution.cpp` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language cpp` |
| C | `solution.c` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language c` |
| Go | `solution.go` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language go` |
| Rust | `solution.rs` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language rust` |
| Kotlin | `Solution.kt` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language kotlin` |
| Swift | `Solution.swift` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language swift` |
| Ruby | `solution.rb` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language ruby` |
| C# | `Solution.cs` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language csharp` |
| Scala | `Solution.scala` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language scala` |
| PHP | `solution.php` | `./scripts/test.sh --folder 0920_number_of_music_playlists --language php` |

Direct Docker Compose in zsh:

```zsh
docker compose -f docker/docker-compose.yml run --rm python python 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm javascript javascript 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm typescript typescript 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm java java 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm cpp cpp 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm c c 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm go go 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm rust rust 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm swift swift 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm ruby ruby 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm csharp csharp 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm scala scala 0920_number_of_music_playlists
docker compose -f docker/docker-compose.yml run --rm php php 0920_number_of_music_playlists
```

### Direct Docker Compose (any OS)

From the repository root:

| Language | Command |
|----------|---------|
| Python | `docker compose -f docker/docker-compose.yml run --rm python python 0920_number_of_music_playlists` |
| JavaScript | `docker compose -f docker/docker-compose.yml run --rm javascript javascript 0920_number_of_music_playlists` |
| TypeScript | `docker compose -f docker/docker-compose.yml run --rm typescript typescript 0920_number_of_music_playlists` |
| Java | `docker compose -f docker/docker-compose.yml run --rm java java 0920_number_of_music_playlists` |
| C++ | `docker compose -f docker/docker-compose.yml run --rm cpp cpp 0920_number_of_music_playlists` |
| C | `docker compose -f docker/docker-compose.yml run --rm c c 0920_number_of_music_playlists` |
| Go | `docker compose -f docker/docker-compose.yml run --rm go go 0920_number_of_music_playlists` |
| Rust | `docker compose -f docker/docker-compose.yml run --rm rust rust 0920_number_of_music_playlists` |
| Kotlin | `docker compose -f docker/docker-compose.yml run --rm kotlin kotlin 0920_number_of_music_playlists` |
| Swift | `docker compose -f docker/docker-compose.yml run --rm swift swift 0920_number_of_music_playlists` |
| Ruby | `docker compose -f docker/docker-compose.yml run --rm ruby ruby 0920_number_of_music_playlists` |
| C# | `docker compose -f docker/docker-compose.yml run --rm csharp csharp 0920_number_of_music_playlists` |
| Scala | `docker compose -f docker/docker-compose.yml run --rm scala scala 0920_number_of_music_playlists` |
| PHP | `docker compose -f docker/docker-compose.yml run --rm php php 0920_number_of_music_playlists` |

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
.\scripts\test.ps1 -Folder 0920_number_of_music_playlists -AllLanguages
```

```bash
./scripts/test.sh --folder 0920_number_of_music_playlists --all-languages
```

```zsh
./scripts/test.sh --folder 0920_number_of_music_playlists --all-languages
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
