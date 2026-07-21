#!/usr/bin/env bash
set -euo pipefail
cd /workspace
fail=0
ok=0
sql_skip="1809 1811 1821 1831 1841 1843"
for dir in 18{01..50}_*/; do
  [ -d "$dir" ] || continue
  num="${dir:0:4}"
  if [[ " $sql_skip " == *" $num "* ]]; then continue; fi
  if [[ "$num" == "1800" ]]; then continue; fi
  file="${dir}Solution.swift"
  if out=$(swiftc -typecheck "$file" 2>&1); then
    ok=$((ok + 1))
  else
    echo "FAIL: $file"
    echo "$out"
    fail=$((fail + 1))
  fi
done
echo "OK=$ok FAIL=$fail"
exit $fail