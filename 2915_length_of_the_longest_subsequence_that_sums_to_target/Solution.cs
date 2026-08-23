// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

using System.Collections.Generic;

public class Solution {
    public int LengthOfLongestSubsequence(IList<int> nums, int target) {
        int[] dp = new int[target + 1];
        for (int i = 0; i <= target; i++) dp[i] = -1;
        dp[0] = 0;
        foreach (int v in nums)
            for (int s = target; s >= v; s--)
                if (dp[s - v] >= 0 && dp[s - v] + 1 > dp[s]) dp[s] = dp[s - v] + 1;
        return dp[target];
    }
}
