public class Solution {
    public const string SCRIPT = "\n#!/bin/bash\nawk '\n{\n  for (i = 1; i <= NF; i++) {\n    if (NR == 1) {\n      row[i] = $i\n    } else {\n      row[i] = row[i] \" \" $i\n    }\n  }\n}\nEND {\n  for (i = 1; i <= NF; i++) {\n    print row[i]\n  }\n}\n' file.txt\n";
}
