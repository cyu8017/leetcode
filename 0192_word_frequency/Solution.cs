public class Solution {
    public const string SCRIPT = "\n#!/bin/bash\ncat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'\n";
}
