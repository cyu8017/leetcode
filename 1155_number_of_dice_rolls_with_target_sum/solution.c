// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

#include <stdlib.h>
#include <string.h>

int numRollsToTarget(int n, int k, int target) {
    const int MOD = 1000000007;
    int* dp = (int*)calloc((size_t)(target + 1), sizeof(int));
    dp[0] = 1;
    for (int dice = 0; dice < n; dice++) {
        int* neu = (int*)calloc((size_t)(target + 1), sizeof(int));
        for (int s = 0; s <= target; s++) {
            if (!dp[s]) continue;
            for (int face = 1; face <= k; face++) {
                if (s + face <= target) neu[s + face] = (neu[s + face] + dp[s]) % MOD;
            }
        }
        free(dp);
        dp = neu;
    }
    int ans = dp[target];
    free(dp);
    return ans;
}
