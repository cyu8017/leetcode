// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumValueSum(int[] nums, int[] andValues) {
        int n = nums.Length, m = andValues.Length;
        const int Inf = 1 << 29;
        var f = new Dictionary<long, int>();
        int Dfs(int i, int j, int a) {
            if (n - i < m - j) return Inf;
            if (j == m) return i == n ? 0 : Inf;
            a &= nums[i];
            if (a < andValues[j]) return Inf;
            long key = ((long)i << 36) | ((long)j << 32) | (uint)a;
            if (f.TryGetValue(key, out int cached)) return cached;
            int ans = Dfs(i + 1, j, a);
            if (a == andValues[j]) {
                ans = Math.Min(ans, Dfs(i + 1, j + 1, -1) + nums[i]);
            }
            return f[key] = ans;
        }
        int res = Dfs(0, 0, -1);
        return res < Inf ? res : -1;
    }
}
