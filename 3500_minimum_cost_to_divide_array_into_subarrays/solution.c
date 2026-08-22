// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

#include <stdlib.h>

#define INF3500 (1LL << 62)

long long minimumCost(int* nums, int numsSize, int* cost, int costSize, int k) {
    (void)costSize;
    int n = numsSize;
    long long* pn = (long long*)calloc((size_t)(n + 1), sizeof(long long));
    long long* pc = (long long*)calloc((size_t)(n + 1), sizeof(long long));
    for (int i = 0; i < n; i++) {
        pn[i + 1] = pn[i] + nums[i];
        pc[i + 1] = pc[i] + cost[i];
    }
    long long* dp = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    for (int i = 0; i < n; i++) dp[i] = INF3500;
    dp[n] = 0;
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i; j < n; j++) {
            long long cand = pn[j + 1] * (pc[j + 1] - pc[i]) + (long long)k * (pc[n] - pc[i]) + dp[j + 1];
            if (cand < dp[i]) dp[i] = cand;
        }
    }
    long long ans = dp[0];
    free(pn); free(pc); free(dp);
    return ans;
}
