#!/bin/bash
set -euo pipefail
export PATH="/usr/local/bin:/opt/scala-2.13.14/bin:$PATH"
SKIP="1809 1811 1821 1831 1841 1843"
fail=0
pass=0
tmpdir=$(mktemp -d)
for num in $(seq 1801 1850); do
  skip=0
  for s in $SKIP; do [ "$num" = "$s" ] && skip=1 && break; done
  [ $skip -eq 1 ] && continue
  folder=$(ls -d /workspace/${num}_* 2>/dev/null | head -1)
  if [ -z "$folder" ]; then
    echo "MISSING $num"
    fail=$((fail+1))
    continue
  fi
  sc="$folder/Solution.scala"
  name=$(basename "$folder")
  if grep -q 'def solve' "$sc"; then
    echo "STUB $name"
    fail=$((fail+1))
    continue
  fi
  if scalac -d "$tmpdir" "$sc" 2>"$tmpdir/${num}.err"; then
    echo "OK $name"
    pass=$((pass+1))
  else
    echo "FAIL $name"
    cat "$tmpdir/${num}.err"
    fail=$((fail+1))
  fi
done
echo "pass=$pass fail=$fail"
[ "$fail" -eq 0 ]
