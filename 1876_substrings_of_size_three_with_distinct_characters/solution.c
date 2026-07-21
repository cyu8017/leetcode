// LeetCode 1876 - Substrings of Size Three with Distinct Characters
// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

#include <string.h>

int countGoodSubstrings(char* s) {
    int n = (int)strlen(s);
    if (n < 3) return 0;
    int count = 0;
    for (int i = 0; i + 2 < n; i++) {
        if (s[i] != s[i + 1] && s[i] != s[i + 2] && s[i + 1] != s[i + 2]) count++;
    }
    return count;
}
