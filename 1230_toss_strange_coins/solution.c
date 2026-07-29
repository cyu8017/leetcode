// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

#include <stdlib.h>

double probabilityOfHeads(double* prob, int probSize, int target) {
    double* dp = (double*)malloc((size_t)(target + 1) * sizeof(double));
    dp[0] = 1.0;
    for (int i = 1; i <= target; i++) dp[i] = 0.0;
    for (int i = 0; i < probSize; i++) {
        double p = prob[i];
        for (int heads = target; heads >= 0; heads--) {
            dp[heads] = dp[heads] * (1.0 - p) + (heads > 0 ? dp[heads - 1] * p : 0.0);
        }
    }
    double ans = dp[target];
    free(dp);
    return ans;
}
