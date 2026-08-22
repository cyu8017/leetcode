// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

#include <string.h>

int longestSemiRepetitiveSubstring(char* s) {
    int ans = 0, left = 0, lastPair = -1, n = (int)strlen(s);
    for (int right = 0; right < n; right++) {
        if (right > 0 && s[right] == s[right - 1]) {
            if (lastPair >= left) left = lastPair + 1;
            lastPair = right - 1;
        }
        if (right - left + 1 > ans) ans = right - left + 1;
    }
    return ans;
}
