// LeetCode 0194 - Transpose File
// https://leetcode.com/problems/transpose-file/

var SCRIPT = `
#!/bin/bash
awk '
{
  for (i = 1; i <= NF; i++) {
    if (NR == 1) {
      row[i] = $i
    } else {
      row[i] = row[i] " " $i
    }
  }
}
END {
  for (i = 1; i <= NF; i++) {
    print row[i]
  }
}
' file.txt
`;