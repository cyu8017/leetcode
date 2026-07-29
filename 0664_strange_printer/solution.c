// LeetCode 0664 - Strange Printer
// https://leetcode.com/problems/strange-printer/

#include <string.h>

int strangePrinter(char* s) {
    int n = (int)strlen(s);
    if (n == 0) return 0;
    int dp[100][100];
    for (int i = 0; i < n; i++) dp[i][i] = 1;
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i + len - 1 < n; i++) {
            int j = i + len - 1;
            dp[i][j] = dp[i][j - 1] + 1;
            for (int k = i; k < j; k++) {
                int cand = dp[i][k] + dp[k + 1][j];
                if (s[k] == s[j]) cand--;
                if (cand < dp[i][j]) dp[i][j] = cand;
            }
        }
    }
    return dp[0][n - 1];
}
