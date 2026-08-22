// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

#include <stdlib.h>

int minimumOperations(int* nums, int numsSize) {
    int n = numsSize;
    int(*dp)[4] = calloc(n + 1, sizeof(int[4]));
    const int INF = 1 << 30;
    for (int i = 0; i <= n; i++) for (int g = 1; g <= 3; g++) dp[i][g] = INF;
    dp[0][1] = dp[0][2] = dp[0][3] = 0;
    for (int i = 1; i <= n; i++) {
        int v = nums[i - 1];
        for (int g = 1; g <= 3; g++) {
            int cost = (v != g);
            for (int prev = 1; prev <= g; prev++) {
                int cand = dp[i - 1][prev] + cost;
                if (cand < dp[i][g]) dp[i][g] = cand;
            }
        }
    }
    int ans = dp[n][1];
    if (dp[n][2] < ans) ans = dp[n][2];
    if (dp[n][3] < ans) ans = dp[n][3];
    free(dp);
    return ans;
}
