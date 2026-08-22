// LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
// https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

#include <stdlib.h>
#include <string.h>

int longestSubsequence(int* nums, int numsSize) {
    int n = numsSize, ans = 1;
    int** dp = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) { dp[i] = (int*)calloc(301, sizeof(int)); }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            int d = nums[i] - nums[j]; if (d < 0) d = -d;
            int best = 1;
            for (int pd = d; pd <= 300; pd++) if (dp[j][pd] > best) best = dp[j][pd];
            if (best + 1 > dp[i][d]) dp[i][d] = best + 1;
            if (dp[i][d] > ans) ans = dp[i][d];
        }
        if (dp[i][0] < 1) dp[i][0] = 1;
    }
    for (int i = 0; i < n; i++) free(dp[i]); free(dp);
    return ans;
}
