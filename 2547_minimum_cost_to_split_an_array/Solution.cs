// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

using System.Collections.Generic;

public class Solution {
    public int MinCost(int[] nums, int k) {
        int n = nums.Length;
        const long INF = 1000000000000000000L;
        long[] dp = new long[n + 1];
        for (int i = 1; i <= n; i++) dp[i] = INF;
        for (int i = 0; i < n; ++i) {
            var freq = new Dictionary<int, int>();
            int trimmed = 0;
            for (int j = i; j < n; ++j) {
                int c = freq.GetValueOrDefault(nums[j], 0) + 1;
                freq[nums[j]] = c;
                if (c == 2) trimmed += 2;
                else if (c > 2) trimmed++;
                long cost = dp[i] + k + trimmed;
                if (cost < dp[j + 1]) dp[j + 1] = cost;
            }
        }
        return (int)dp[n];
    }
}
