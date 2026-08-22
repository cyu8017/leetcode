// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

#include <stdlib.h>
#include <string.h>

int minCost(int* nums, int numsSize, int k) {
    const long long INF = 1000000000000000000LL;
    long long* dp = (long long*)malloc((size_t)(numsSize + 1) * sizeof(long long));
    dp[0] = 0;
    for (int i = 1; i <= numsSize; i++) dp[i] = INF;
    for (int i = 0; i < numsSize; i++) {
        int* freq = (int*)calloc(1001, sizeof(int));
        int trimmed = 0;
        for (int j = i; j < numsSize; j++) {
            freq[nums[j]]++;
            int c = freq[nums[j]];
            if (c == 2) trimmed += 2;
            else if (c > 2) trimmed++;
            long long cost = dp[i] + k + trimmed;
            if (cost < dp[j + 1]) dp[j + 1] = cost;
        }
        free(freq);
    }
    int ans = (int)dp[numsSize];
    free(dp);
    return ans;
}
