#!/bin/bash
# Compile-check C# Solution.cs for 1801-1850 (non-SQL) inside csharp Docker image.
set -euo pipefail
SKIP="1809 1811 1821 1831 1841 1843"
fail=0
pass=0
tmpdir=$(mktemp -d)
cd "$tmpdir"
dotnet new classlib -n Check -f net8.0 --force >/dev/null
rm -f Check/Class1.cs

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
  sc="$folder/Solution.cs"
  name=$(basename "$folder")
  if grep -q 'void Solve' "$sc"; then
    echo "STUB $name"
    fail=$((fail+1))
    continue
  fi
  cp "$sc" Check/Solution.cs
  if dotnet build Check/Check.csproj -v q >/dev/null 2>"$tmpdir/${num}.err"; then
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
