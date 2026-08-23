// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

using System;

public class Solution {
    public int MinimumOperations(IList<int> nums) {
        int n = nums.Count;
        const int INF = 1 << 30;
        int[,] dp = new int[n + 1, 4];
        for (int i = 0; i <= n; i++)
            for (int g = 1; g <= 3; g++) dp[i, g] = INF;
        dp[0, 1] = dp[0, 2] = dp[0, 3] = 0;
        for (int i = 1; i <= n; i++) {
            int v = nums[i - 1];
            for (int g = 1; g <= 3; g++) {
                int cost = (v != g) ? 1 : 0;
                for (int prev = 1; prev <= g; prev++)
                    dp[i, g] = Math.Min(dp[i, g], dp[i - 1, prev] + cost);
            }
        }
        return Math.Min(dp[n, 1], Math.Min(dp[n, 2], dp[n, 3]));
    }
}
