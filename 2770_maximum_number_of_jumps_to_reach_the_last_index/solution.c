// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

#include <stdlib.h>

int maximumJumps(int* nums, int numsSize, int target) {
    int n = numsSize;
    int* dp = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) dp[i] = -1;
    dp[0] = 0;
    for (int i = 0; i < n; i++) {
        if (dp[i] < 0) continue;
        for (int j = i + 1; j < n; j++) {
            long long diff = (long long)nums[j] - nums[i];
            if (diff < 0) diff = -diff;
            if (diff <= target) {
                if (dp[i] + 1 > dp[j]) dp[j] = dp[i] + 1;
            }
        }
    }
    int ans = dp[n - 1];
    free(dp);
    return ans;
}
