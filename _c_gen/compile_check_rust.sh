#!/bin/bash
set -euo pipefail
SKIP="1853 1867 1873 1875 1890 1892"
fail=0
pass=0
tmpdir=$(mktemp -d)
for num in $(seq 1851 1900); do
  skip=0
  for s in $SKIP; do [ "$num" = "$s" ] && skip=1 && break; done
  [ $skip -eq 1 ] && continue
  folder=$(ls -d /workspace/${num}_* 2>/dev/null | head -1)
  if [ -z "$folder" ]; then
    echo "MISSING $num"
    fail=$((fail+1))
    continue
  fi
  rs="$folder/solution.rs"
  out="$tmpdir/${num}.rs"
  name=$(basename "$folder")
  if [ "$num" = "1865" ]; then
    {
      echo '#![allow(dead_code)]'
      cat "$rs"
      echo 'fn main() {}'
    } > "$out"
  else
    {
      echo '#![allow(dead_code)]'
      echo 'struct Solution;'
      cat "$rs"
      echo 'fn main() {}'
    } > "$out"
  fi
  if rustc --edition 2021 "$out" -o "$tmpdir/${num}.bin" 2>"$tmpdir/${num}.err"; then
    echo "OK $name"
    pass=$((pass+1))
  else
    echo "FAIL $name"
    cat "$tmpdir/${num}.err"
    fail=$((fail+1))
  fi
done
echo "SUMMARY pass=$pass fail=$fail"
exit $fail
