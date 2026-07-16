// LeetCode 0192 - Word Frequency
// https://leetcode.com/problems/word-frequency/

const SCRIPT = `
#!/bin/bash
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
`
