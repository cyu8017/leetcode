// LeetCode 0192 - Word Frequency
// https://leetcode.com/problems/word-frequency/

const char *SCRIPT = "\n#!/bin/bash\ncat words.txt | tr -s ' ' '\\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'\n";
