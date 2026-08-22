// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

#include <stdlib.h>

static int gcd2464(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

int validSubarraySplit(int* nums, int numsSize) {
    int n = numsSize;
    int* dp = (int*)malloc((size_t)(n + 1) * sizeof(int));
    const int INF = 1 << 30;
    for (int i = 0; i <= n; i++) dp[i] = INF;
    dp[0] = 0;
    for (int i = 0; i < n; i++) {
        if (dp[i] >= INF) continue;
        for (int j = i; j < n; j++) {
            if (gcd2464(nums[i], nums[j]) > 1) {
                if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1;
            }
        }
    }
    int ans = dp[n] >= INF ? -1 : dp[n];
    free(dp);
    return ans;
}
