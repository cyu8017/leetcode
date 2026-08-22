// LeetCode 3418 - Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

#include <stdlib.h>

static int max3418(int a, int b) { return a > b ? a : b; }

int maximumAmount(int** coins, int coinsSize, int* coinsColSize) {
    int m = coinsSize, n = coinsColSize[0];
    const int neg = -(1 << 30);
    int*** dp = (int***)malloc(m * sizeof(int**));
    for (int i = 0; i < m; i++) {
        dp[i] = (int**)malloc(n * sizeof(int*));
        for (int j = 0; j < n; j++) {
            dp[i][j] = (int*)malloc(3 * sizeof(int));
            dp[i][j][0] = dp[i][j][1] = dp[i][j][2] = neg;
        }
    }
    if (coins[0][0] < 0) { dp[0][0][0] = coins[0][0]; dp[0][0][1] = 0; dp[0][0][2] = 0; }
    else { dp[0][0][0] = dp[0][0][1] = dp[0][0][2] = coins[0][0]; }
    for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) {
        if (i == 0 && j == 0) continue;
        for (int k = 0; k < 3; k++) {
            int best = neg;
            if (i > 0) best = max3418(best, dp[i - 1][j][k]);
            if (j > 0) best = max3418(best, dp[i][j - 1][k]);
            if (best == neg) continue;
            if (coins[i][j] >= 0) dp[i][j][k] = best + coins[i][j];
            else dp[i][j][k] = max3418(dp[i][j][k], best + coins[i][j]);
        }
        for (int k = 1; k < 3; k++) {
            int best = neg;
            if (i > 0) best = max3418(best, dp[i - 1][j][k - 1]);
            if (j > 0) best = max3418(best, dp[i][j - 1][k - 1]);
            if (best != neg && coins[i][j] < 0) dp[i][j][k] = max3418(dp[i][j][k], best);
        }
    }
    int ans = max3418(dp[m - 1][n - 1][0], max3418(dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]));
    for (int i = 0; i < m; i++) { for (int j = 0; j < n; j++) free(dp[i][j]); free(dp[i]); }
    free(dp);
    return ans;
}
