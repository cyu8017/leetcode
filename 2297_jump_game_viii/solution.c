// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

#include <stdlib.h>

long long minCost(int* nums, int numsSize, int* costs, int costsSize) {
    (void)costsSize;
    int n = numsSize;
    long long* dp = (long long*)malloc((size_t)n * sizeof(long long));
    for (int i = 0; i < n; i++) dp[i] = 1LL << 60;
    dp[0] = 0;
    int* stack1 = (int*)malloc((size_t)n * sizeof(int));
    int* stack2 = (int*)malloc((size_t)n * sizeof(int));
    int t1 = 0, t2 = 0;
    for (int i = 0; i < n; i++) {
        while (t1 > 0 && nums[stack1[t1 - 1]] <= nums[i]) {
            int j = stack1[--t1];
            if (dp[j] + costs[i] < dp[i]) dp[i] = dp[j] + costs[i];
        }
        while (t2 > 0 && nums[stack2[t2 - 1]] > nums[i]) {
            int j = stack2[--t2];
            if (dp[j] + costs[i] < dp[i]) dp[i] = dp[j] + costs[i];
        }
        if (t1 > 0) {
            int j = stack1[t1 - 1];
            if (dp[j] + costs[i] < dp[i]) dp[i] = dp[j] + costs[i];
        }
        if (t2 > 0) {
            int j = stack2[t2 - 1];
            if (dp[j] + costs[i] < dp[i]) dp[i] = dp[j] + costs[i];
        }
        stack1[t1++] = i;
        stack2[t2++] = i;
    }
    long long ans = dp[n - 1];
    free(dp); free(stack1); free(stack2);
    return ans;
}
