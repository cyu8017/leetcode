// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

#include <stdlib.h>
#include <string.h>

int maxValueOfCoins(int** piles, int pilesSize, int* pilesColSize, int k) {
    int* dp = (int*)calloc((size_t)k + 1, sizeof(int));
    for (int p = 0; p < pilesSize; p++) {
        int* ndp = (int*)malloc((size_t)(k + 1) * sizeof(int));
        memcpy(ndp, dp, (size_t)(k + 1) * sizeof(int));
        int sum = 0;
        int plen = pilesColSize[p];
        for (int take = 1; take <= plen && take <= k; take++) {
            sum += piles[p][take - 1];
            for (int j = take; j <= k; j++) {
                if (dp[j - take] + sum > ndp[j]) ndp[j] = dp[j - take] + sum;
            }
        }
        free(dp); dp = ndp;
    }
    int ans = dp[k];
    free(dp);
    return ans;
}
