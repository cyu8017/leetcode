// LeetCode 3891 - Minimum Increase To Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

using System;

public class Solution {
    public long MinIncrease(int[] nums) {
        int n = nums.Length;
        var f = new long[n][];
        for (int i = 0; i < n; i++) { f[i] = new long[2]; f[i][0] = f[i][1] = -1; }

        long Dfs(int i, int j) {
            if (i >= n - 1) return 0;
            if (f[i][j] != -1) return f[i][j];
            int cost = Math.Max(0, Math.Max(nums[i - 1], nums[i + 1]) + 1 - nums[i]);
            long ans = (long)cost + Dfs(i + 2, j);
            if (j > 0) ans = Math.Min(ans, Dfs(i + 1, 0));
            return f[i][j] = ans;
        }

        return Dfs(1, (n & 1) ^ 1);
    }
}
