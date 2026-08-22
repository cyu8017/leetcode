// LeetCode 0005 - Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

#include <stdlib.h>
#include <string.h>

static int expand(const char* s, int n, int left, int right) {
    while (left >= 0 && right < n && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1;
}

char* longestPalindrome(char* s) {
    int n = (int)strlen(s);
    int bestStart = 0;
    int bestLen = 0;

    for (int i = 0; i < n; i++) {
        int len1 = expand(s, n, i, i);
        int len2 = expand(s, n, i, i + 1);
        int len = len1 > len2 ? len1 : len2;
        if (len > bestLen) {
            bestLen = len;
            bestStart = i - (len - 1) / 2;
        }
    }

    char* result = (char*)malloc((size_t)bestLen + 1);
    memcpy(result, s + bestStart, (size_t)bestLen);
    result[bestLen] = '\0';
    return result;
}
