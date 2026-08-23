// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

import java.util.Arrays;
import java.util.List;

class Solution {
    public int lengthOfLongestSubsequence(List<Integer> nums, int target) {
        int[] dp = new int[target + 1];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        for (int v : nums)
            for (int s = target; s >= v; s--)
                if (dp[s - v] >= 0 && dp[s - v] + 1 > dp[s]) dp[s] = dp[s - v] + 1;
        return dp[target];
    }
}
