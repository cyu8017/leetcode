// LeetCode 3741 - Minimum Distance Between Three Equal Elements II
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumDistance(int[] nums) {
        var g = new Dictionary<int, List<int>>();
        for (int i = 0; i < nums.Length; i++) {
            if (!g.ContainsKey(nums[i])) g[nums[i]] = new List<int>();
            g[nums[i]].Add(i);
        }
        const int inf = 1 << 30;
        int ans = inf;
        foreach (var ls in g.Values) {
            int m = ls.Count;
            for (int h = 0; h < m - 2; h++) {
                ans = Math.Min(ans, (ls[h + 2] - ls[h]) * 2);
            }
        }
        return ans == inf ? -1 : ans;
    }
}
