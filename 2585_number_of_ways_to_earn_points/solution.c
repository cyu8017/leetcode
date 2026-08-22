// LeetCode 2585 - Number of Ways to Earn Points
// https://leetcode.com/problems/number-of-ways-to-earn-points/

#include <stdlib.h>
#include <string.h>

int waysToReachTarget(int target, int** types, int typesSize, int* typesColSize) {
    (void)typesColSize;
    const int MOD = 1000000007;
    int* dp = (int*)calloc((size_t)(target + 1), sizeof(int));
    dp[0] = 1;
    for (int t = 0; t < typesSize; t++) {
        int count = types[t][0], marks = types[t][1];
        for (int s = target; s >= 0; s--) {
            for (int k = 1; k <= count && s - k * marks >= 0; k++) {
                dp[s] = (dp[s] + dp[s - k * marks]) % MOD;
            }
        }
    }
    int ans = dp[target];
    free(dp);
    return ans;
}
