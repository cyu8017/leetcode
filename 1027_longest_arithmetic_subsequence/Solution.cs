// LeetCode 1027 - Longest Arithmetic Subsequence
// https://leetcode.com/problems/longest-arithmetic-subsequence/

using System.Collections.Generic;

public class Solution {
    public int LongestArithSeqLength(int[] nums) {
        var dp = new Dictionary<int, int>[nums.Length];
        for (int i = 0; i < nums.Length; i++) dp[i] = new Dictionary<int, int>();
        int ans = 1;
        for (int j = 1; j < nums.Length; j++) {
            for (int i = 0; i < j; i++) {
                int d = nums[j] - nums[i];
                int prev = dp[i].TryGetValue(d, out int v) ? v : 1;
                dp[j][d] = prev + 1;
                ans = Math.Max(ans, dp[j][d]);
            }
        }
        return ans;
    }
}
