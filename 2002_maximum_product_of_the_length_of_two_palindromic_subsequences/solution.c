// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

#include <string.h>
#include <stdbool.h>

static bool isPal2002(const char* s, int n, int mask, int* lenOut) {
    char chars[16];
    int len = 0;
    for (int i = 0; i < n; i++) {
        if (mask & (1 << i)) chars[len++] = s[i];
    }
    for (int l = 0, r = len - 1; l < r; l++, r--) {
        if (chars[l] != chars[r]) return false;
    }
    *lenOut = len;
    return true;
}

int maxProduct(char* s) {
    int n = (int)strlen(s);
    int total = 1 << n;
    int best = 0;
    for (int mask1 = 1; mask1 < total; mask1++) {
        int len1;
        if (!isPal2002(s, n, mask1, &len1)) continue;
        int remain = (total - 1) ^ mask1;
        for (int mask2 = remain; mask2 > 0; mask2 = (mask2 - 1) & remain) {
            int len2;
            if (isPal2002(s, n, mask2, &len2) && len1 * len2 > best) best = len1 * len2;
        }
    }
    return best;
}
