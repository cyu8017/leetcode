// LeetCode 1763 - Longest Nice Substring
// https://leetcode.com/problems/longest-nice-substring/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned string must be malloced, assume caller calls free().
 */
char* longestNiceSubstring(char* s) {
    int n = (int)strlen(s);
    int bestStart = 0;
    int bestLen = 0;
    for (int i = 0; i < n; i++) {
        int lower = 0;
        int upper = 0;
        for (int j = i; j < n; j++) {
            char c = s[j];
            if (c >= 'a' && c <= 'z') {
                lower |= 1 << (c - 'a');
            } else {
                upper |= 1 << (c - 'A');
            }
            if (lower == upper && j - i + 1 > bestLen) {
                bestStart = i;
                bestLen = j - i + 1;
            }
        }
    }
    char* ans = (char*)malloc(bestLen + 1);
    memcpy(ans, s + bestStart, bestLen);
    ans[bestLen] = '\0';
    return ans;
}
