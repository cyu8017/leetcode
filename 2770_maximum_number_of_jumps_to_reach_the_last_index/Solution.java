// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

import java.util.Arrays;

class Solution {
    public int maximumJumps(int[] nums, int target) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] < 0) continue;
            for (int j = i + 1; j < n; j++) {
                if (Math.abs(nums[j] - nums[i]) <= target)
                    dp[j] = Math.max(dp[j], dp[i] + 1);
            }
        }
        return dp[n - 1];
    }
}
