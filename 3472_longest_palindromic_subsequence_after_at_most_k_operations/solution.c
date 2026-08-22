// LeetCode 3472 - Longest Palindromic Subsequence After At Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

#include <stdlib.h>
#include <string.h>

static char* s3472;
static int*** dp3472;

static int distCirc(char a, char b) {
    int d = (int)a - (int)b;
    if (d < 0) d = -d;
    if (26 - d < d) return 26 - d;
    return d;
}

static int dfs3472(int i, int j, int ops) {
    if (i > j) return 0;
    if (i == j) return 1;
    if (dp3472[i][j][ops] != -1) return dp3472[i][j][ops];
    int best = dfs3472(i + 1, j, ops);
    int v = dfs3472(i, j - 1, ops);
    if (v > best) best = v;
    int cost = distCirc(s3472[i], s3472[j]);
    if (cost <= ops) {
        v = 2 + dfs3472(i + 1, j - 1, ops - cost);
        if (v > best) best = v;
    }
    dp3472[i][j][ops] = best;
    return best;
}

int longestPalindromicSubsequence(char* s, int k) {
    int n = (int)strlen(s);
    s3472 = s;
    dp3472 = (int***)malloc((size_t)n * sizeof(int**));
    for (int i = 0; i < n; i++) {
        dp3472[i] = (int**)malloc((size_t)n * sizeof(int*));
        for (int j = 0; j < n; j++) {
            dp3472[i][j] = (int*)malloc((size_t)(k + 1) * sizeof(int));
            for (int t = 0; t <= k; t++) dp3472[i][j][t] = -1;
        }
    }
    int ans = dfs3472(0, n - 1, k);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) free(dp3472[i][j]);
        free(dp3472[i]);
    }
    free(dp3472);
    return ans;
}
