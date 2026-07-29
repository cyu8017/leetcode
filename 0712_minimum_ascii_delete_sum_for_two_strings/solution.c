// LeetCode 0712 - Minimum ASCII Delete Sum for Two Strings
// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

#include <stdlib.h>
#include <string.h>

int minimumDeleteSum(char* s1, char* s2) {
    int m = (int)strlen(s1);
    int n = (int)strlen(s2);
    int** dp = (int**)malloc((size_t)(m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) {
        dp[i] = (int*)calloc((size_t)(n + 1), sizeof(int));
    }
    for (int i = 1; i <= m; i++) {
        dp[i][0] = dp[i - 1][0] + (unsigned char)s1[i - 1];
    }
    for (int j = 1; j <= n; j++) {
        dp[0][j] = dp[0][j - 1] + (unsigned char)s2[j - 1];
    }
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                int a = dp[i - 1][j] + (unsigned char)s1[i - 1];
                int b = dp[i][j - 1] + (unsigned char)s2[j - 1];
                dp[i][j] = a < b ? a : b;
            }
        }
    }
    int ans = dp[m][n];
    for (int i = 0; i <= m; i++) {
        free(dp[i]);
    }
    free(dp);
    return ans;
}
