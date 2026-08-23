// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

using System;
using System.Collections.Generic;

public class Solution {
    public long MinCost(int[] nums, int[] costs) {
        int n = nums.Length;
        long[] dp = new long[n];
        Array.Fill(dp, long.MaxValue / 4);
        dp[0] = 0;
        var stack1 = new List<int>();
        var stack2 = new List<int>();
        for (int i = 0; i < n; i++) {
            while (stack1.Count > 0 && nums[stack1[stack1.Count - 1]] <= nums[i]) {
                int j = stack1[stack1.Count - 1]; stack1.RemoveAt(stack1.Count - 1);
                dp[i] = Math.Min(dp[i], dp[j] + costs[i]);
            }
            while (stack2.Count > 0 && nums[stack2[stack2.Count - 1]] > nums[i]) {
                int j = stack2[stack2.Count - 1]; stack2.RemoveAt(stack2.Count - 1);
                dp[i] = Math.Min(dp[i], dp[j] + costs[i]);
            }
            if (stack1.Count > 0) dp[i] = Math.Min(dp[i], dp[stack1[stack1.Count - 1]] + costs[i]);
            if (stack2.Count > 0) dp[i] = Math.Min(dp[i], dp[stack2[stack2.Count - 1]] + costs[i]);
            stack1.Add(i);
            stack2.Add(i);
        }
        return dp[n - 1];
    }
}
