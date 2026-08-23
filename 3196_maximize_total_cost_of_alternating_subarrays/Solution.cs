// LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

using System;

public class Solution {
    public long MaximumTotalCost(int[] nums) {
        int n = nums.Length;
        const long NEG = (long)-1e18;
        long[][] memo = new long[n][];
        for (int i = 0; i < n; i++) memo[i] = new long[] { NEG, NEG };
        long Dfs(int i, int j) {
            if (i >= n) return 0;
            if (memo[i][j] != NEG) return memo[i][j];
            long res = nums[i] + Dfs(i + 1, 1);
            if (j > 0) res = Math.Max(res, -nums[i] + Dfs(i + 1, 0));
            return memo[i][j] = res;
        }
        return Dfs(0, 0);
    }
}
