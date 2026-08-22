// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

#include <stdlib.h>
long long minArraySum(int* nums, int numsSize, int k) {
    int n = numsSize;
    int* prefix = (int*)calloc((size_t)n + 1, sizeof(int));
    for (int i = 0; i < n; i++) prefix[i + 1] = (prefix[i] + nums[i]) % k;
    const long long inf = 1LL << 62;
    long long* dp = (long long*)calloc((size_t)n + 1, sizeof(long long));
    long long* best = (long long*)malloc((size_t)k * sizeof(long long));
    for (int i = 0; i < k; i++) best[i] = inf;
    best[0] = 0;
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i - 1] + nums[i - 1];
        if (best[prefix[i]] < dp[i]) dp[i] = best[prefix[i]];
        if (dp[i] < best[prefix[i]]) best[prefix[i]] = dp[i];
    }
    long long ans = dp[n];
    free(prefix); free(dp); free(best);
    return ans;
}
