// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

#include <stdlib.h>
#include <string.h>

static int semiCost(const char* s, int l, int r) {
    int length = r - l + 1, best = 1 << 20;
    for (int d = 1; d < length; d++) {
        if (length % d != 0) continue;
        int chg = 0;
        for (int start = 0; start < d; start++) {
            char chars[256];
            int cn = 0;
            for (int i = l + start; i <= r; i += d) chars[cn++] = s[i];
            for (int i = 0, j = cn - 1; i < j; i++, j--) if (chars[i] != chars[j]) chg++;
        }
        if (chg < best) best = chg;
    }
    return best;
}

int minimumChanges(char* s, int k) {
    int n = (int)strlen(s);
    int** cost = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        cost[i] = (int*)malloc(n * sizeof(int));
        for (int j = 0; j < n; j++) cost[i][j] = 1 << 20;
    }
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            cost[i][j] = semiCost(s, i, j);
    int** dp = (int**)malloc((k + 1) * sizeof(int*));
    for (int i = 0; i <= k; i++) {
        dp[i] = (int*)malloc((n + 1) * sizeof(int));
        for (int j = 0; j <= n; j++) dp[i][j] = 1 << 20;
    }
    dp[0][0] = 0;
    for (int p = 1; p <= k; p++)
        for (int i = 1; i <= n; i++)
            for (int t = 0; t < i - 1; t++) {
                int cand = dp[p - 1][t] + cost[t][i - 1];
                if (cand < dp[p][i]) dp[p][i] = cand;
            }
    int ans = dp[k][n];
    for (int i = 0; i < n; i++) free(cost[i]);
    free(cost);
    for (int i = 0; i <= k; i++) free(dp[i]);
    free(dp);
    return ans;
}
