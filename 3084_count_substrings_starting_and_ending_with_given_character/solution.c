// LeetCode 3084 - Count Substrings Starting and Ending with Given Character
// https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

#include <string.h>

long long countSubstrings(char* s, char c) {
    long long cnt = 0;
    for (int i = 0; s[i]; i++) if (s[i] == c) cnt++;
    return cnt + cnt * (cnt - 1) / 2;
}
