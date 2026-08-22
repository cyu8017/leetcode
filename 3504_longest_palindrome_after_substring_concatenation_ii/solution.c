// LeetCode 3504 - Longest Palindrome After Substring Concatenation II
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

#include <stdlib.h>
#include <string.h>

static int max2(int a, int b) { return a > b ? a : b; }

static void expand(const char* s, int* g, int n, int l, int r) {
    while (l >= 0 && r < n && s[l] == s[r]) {
        g[l] = max2(g[l], r - l + 1);
        l--; r++;
    }
}

static int* calc(const char* s, int n) {
    int* g = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) {
        expand(s, g, n, i, i);
        expand(s, g, n, i, i + 1);
    }
    return g;
}

static char* revstr(const char* t, int n) {
    char* r = (char*)malloc((size_t)n + 1);
    for (int i = 0; i < n; i++) r[i] = t[n - 1 - i];
    r[n] = '\0';
    return r;
}

int longestPalindrome(char* s, char* t) {
    int m = (int)strlen(s), n = (int)strlen(t);
    char* tr = revstr(t, n);
    int* g1 = calc(s, m);
    int* g2 = calc(tr, n);
    int ans = 0;
    for (int i = 0; i < m; i++) ans = max2(ans, g1[i]);
    for (int i = 0; i < n; i++) ans = max2(ans, g2[i]);
    int** f = (int**)malloc((size_t)(m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) f[i] = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s[i - 1] == tr[j - 1]) {
                f[i][j] = f[i - 1][j - 1] + 1;
                int a = (i < m) ? g1[i] : 0;
                int b = (j < n) ? g2[j] : 0;
                ans = max2(ans, f[i][j] * 2 + a);
                ans = max2(ans, f[i][j] * 2 + b);
            }
        }
    }
    for (int i = 0; i <= m; i++) free(f[i]);
    free(f); free(g1); free(g2); free(tr);
    return ans;
}
