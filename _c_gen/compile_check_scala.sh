#!/usr/bin/env bash
set -euo pipefail
SKIP="1853 1867 1873 1875 1890 1892"
failed=0
ok=0
for n in $(seq 1851 1900); do
  echo " $SKIP " | grep -q " $n " && continue
  folder=$(ls -d ${n}_* 2>/dev/null | head -1)
  if [[ -z "$folder" ]]; then
    echo "MISSING $n"
    failed=$((failed+1))
    continue
  fi
  tmp=$(mktemp -d)
  if scalac -d "$tmp" "$folder/Solution.scala" 2>"$tmp/err.txt"; then
    echo "OK $folder"
    ok=$((ok+1))
  else
    echo "FAIL $folder"
    cat "$tmp/err.txt"
    failed=$((failed+1))
  fi
  rm -rf "$tmp"
done
echo "Summary: ok=$ok failed=$failed"
exit $failed
