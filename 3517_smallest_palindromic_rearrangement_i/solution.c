// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

#include <stdlib.h>
#include <string.h>

char* smallestPalindrome(char* s) {
    int cnt[26] = {0};
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) cnt[s[i] - 'a']++;
    char* t = (char*)malloc((size_t)(n / 2 + 1));
    int tl = 0;
    char ch = 0;
    for (int c = 0; c < 26; c++) {
        int v = cnt[c] / 2;
        for (int i = 0; i < v; i++) t[tl++] = (char)('a' + c);
        cnt[c] -= v * 2;
        if (cnt[c] == 1) ch = (char)('a' + c);
    }
    int total = tl * 2 + (ch ? 1 : 0);
    char* ans = (char*)malloc((size_t)total + 1);
    int oi = 0;
    for (int i = 0; i < tl; i++) ans[oi++] = t[i];
    if (ch) ans[oi++] = ch;
    for (int i = tl - 1; i >= 0; i--) ans[oi++] = t[i];
    ans[oi] = '\0';
    free(t);
    return ans;
}
