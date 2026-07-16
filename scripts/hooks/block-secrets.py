#!/usr/bin/env python3
from __future__ import annotations

import sys


def main() -> int:
    for path in sys.argv[1:]:
        print(f"Blocked commit of secret file: {path}", file=sys.stderr)
    return 1 if sys.argv[1:] else 0


if __name__ == "__main__":
    raise SystemExit(main())
