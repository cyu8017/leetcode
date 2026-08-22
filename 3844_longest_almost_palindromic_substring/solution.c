// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

#include <string.h>

static int f3844(char* s, int n, int l, int r) {
    while (l >= 0 && r < n && s[l] == s[r]) { l--; r++; }
    int l1 = l - 1, r1 = r, l2 = l, r2 = r + 1;
    while (l1 >= 0 && r1 < n && s[l1] == s[r1]) { l1--; r1++; }
    while (l2 >= 0 && r2 < n && s[l2] == s[r2]) { l2--; r2++; }
    int a = r1 - l1 - 1, b = r2 - l2 - 1;
    int m = a > b ? a : b;
    return m < n ? m : n;
}

int almostPalindromic(char* s) {
    int n = (int)strlen(s);
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int a = f3844(s, n, i, i);
        int b = f3844(s, n, i, i + 1);
        if (a > ans) ans = a;
        if (b > ans) ans = b;
    }
    return ans;
}
