// LeetCode 1682 - Longest Palindromic Subsequence II
// https://leetcode.com/problems/longest-palindromic-subsequence-ii/

#include <stdlib.h>
#include <string.h>

int longestPalindromeSubseq(char* s) {
    int n = (int)strlen(s);
    if (n < 2) return 0;
    // dp[i][j][c] flattened: i*n*26 + j*26 + c — too big for stack; n<=250 -> 250*250*26 ints ~ 6.5MB
    int* dp = (int*)calloc((size_t)n * (size_t)n * 26, sizeof(int));
    #define DP(i,j,c) dp[(((i)*(n)+(j))*26+(c))]
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i + length - 1 < n; i++) {
            int j = i + length - 1;
            for (int c = 0; c < 26; c++) {
                int v = DP(i + 1, j, c);
                int w = DP(i, j - 1, c);
                DP(i, j, c) = v > w ? v : w;
            }
            if (s[i] == s[j]) {
                int c = s[i] - 'a';
                int inner = 0;
                if (length > 2) {
                    for (int x = 0; x < 26; x++) if (x != c) {
                        int v = DP(i + 1, j - 1, x);
                        if (v > inner) inner = v;
                    }
                }
                if (inner + 2 > DP(i, j, c)) DP(i, j, c) = inner + 2;
            }
        }
    }
    int best = 0;
    for (int c = 0; c < 26; c++) if (DP(0, n - 1, c) > best) best = DP(0, n - 1, c);
    free(dp);
    #undef DP
    return best;
}
