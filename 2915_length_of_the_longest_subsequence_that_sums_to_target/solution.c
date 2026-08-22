// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

#include <stdlib.h>

int lengthOfLongestSubsequence(int* nums, int numsSize, int target) {
    int* dp = (int*)malloc((target + 1) * sizeof(int));
    for (int i = 0; i <= target; i++) dp[i] = -1;
    dp[0] = 0;
    for (int i = 0; i < numsSize; i++) {
        int v = nums[i];
        for (int s = target; s >= v; s--) {
            if (dp[s - v] >= 0 && dp[s - v] + 1 > dp[s]) dp[s] = dp[s - v] + 1;
        }
    }
    int ans = dp[target];
    free(dp);
    return ans;
}
