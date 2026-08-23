// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

using System;

public class Solution {
    public int MaximumJumps(int[] nums, int target) {
        int n = nums.Length;
        int[] dp = new int[n];
        Array.Fill(dp, -1);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] < 0) continue;
            for (int j = i + 1; j < n; j++) {
                if (Math.Abs(nums[j] - nums[i]) <= target)
                    dp[j] = Math.Max(dp[j], dp[i] + 1);
            }
        }
        return dp[n - 1];
    }
}
