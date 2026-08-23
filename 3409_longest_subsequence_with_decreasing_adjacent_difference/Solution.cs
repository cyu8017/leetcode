// LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
// https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

using System;

public class Solution {
    public int LongestSubsequence(int[] nums) {
        int n = nums.Length;
        int ans = 1;
        int[][] dp = new int[n][];
        for (int i = 0; i < n; i++) dp[i] = new int[301];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int d = Math.Abs(nums[i] - nums[j]);
                int best = 1;
                for (int pd = d; pd <= 300; pd++) {
                    if (dp[j][pd] > best) best = dp[j][pd];
                }
                if (best + 1 > dp[i][d]) dp[i][d] = best + 1;
                if (dp[i][d] > ans) ans = dp[i][d];
            }
            if (dp[i][0] < 1) dp[i][0] = 1;
        }
        return ans;
    }
}
