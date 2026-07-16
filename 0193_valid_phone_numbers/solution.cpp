// LeetCode 0193 - Valid Phone Numbers
// https://leetcode.com/problems/valid-phone-numbers/

const char* SCRIPT = R"(
#!/bin/bash
grep -E '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt
)";
