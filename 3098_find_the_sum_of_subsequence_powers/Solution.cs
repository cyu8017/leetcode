// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

using System;
using System.Collections.Generic;

public class Solution {
    public int SumOfPowers(int[] nums, int k) {
        const int Mod = 1000000007;
        Array.Sort(nums);
        int n = nums.Length;
        var f = new Dictionary<long, int>();
        int Dfs(int i, int j, int kk, int mi) {
            if (i >= n) return kk == 0 ? mi : 0;
            if (n - i < kk) return 0;
            long key = ((long)mi << 18) | ((long)i << 12) | ((long)j << 6) | (uint)kk;
            if (f.TryGetValue(key, out int cached)) return cached;
            int ans = Dfs(i + 1, j, kk, mi);
            if (j == n) ans = (ans + Dfs(i + 1, i, kk - 1, mi)) % Mod;
            else ans = (ans + Dfs(i + 1, i, kk - 1, Math.Min(mi, nums[i] - nums[j]))) % Mod;
            return f[key] = ans;
        }
        return Dfs(0, n, k, int.MaxValue);
    }
}
