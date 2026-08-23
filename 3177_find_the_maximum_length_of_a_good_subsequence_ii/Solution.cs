// LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumLength(int[] nums, int k) {
        int n = nums.Length;
        int[][] f = new int[n][];
        for (int i = 0; i < n; i++) f[i] = new int[k + 1];
        var mp = new Dictionary<int, int>[k + 1];
        for (int h = 0; h <= k; h++) mp[h] = new Dictionary<int, int>();
        int[][] g = new int[k + 1][];
        for (int h = 0; h <= k; h++) g[h] = new int[3];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int h = 0; h <= k; h++) {
                f[i][h] = mp[h].GetValueOrDefault(nums[i], 0);
                if (h > 0) {
                    if (g[h - 1][0] != nums[i]) f[i][h] = Math.Max(f[i][h], g[h - 1][1]);
                    else f[i][h] = Math.Max(f[i][h], g[h - 1][2]);
                }
                f[i][h]++;
                if (!mp[h].ContainsKey(nums[i]) || f[i][h] > mp[h][nums[i]])
                    mp[h][nums[i]] = f[i][h];
                if (g[h][0] != nums[i]) {
                    if (f[i][h] >= g[h][1]) {
                        g[h][2] = g[h][1];
                        g[h][1] = f[i][h];
                        g[h][0] = nums[i];
                    } else if (f[i][h] > g[h][2]) {
                        g[h][2] = f[i][h];
                    }
                } else if (f[i][h] > g[h][1]) {
                    g[h][1] = f[i][h];
                }
                ans = Math.Max(ans, f[i][h]);
            }
        }
        return ans;
    }
}
