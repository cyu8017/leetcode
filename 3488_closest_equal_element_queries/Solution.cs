// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] SolveQueries(int[] nums, int[] queries) {
        int n = nums.Length;
        var pos = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!pos.ContainsKey(nums[i])) pos[nums[i]] = new List<int>();
            pos[nums[i]].Add(i);
        }
        int[] ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int idx = queries[qi];
            int x = nums[idx];
            var arr = pos[x];
            if (arr.Count == 1) { ans[qi] = -1; continue; }
            int best = n;
            foreach (int p in arr) {
                if (p == idx) continue;
                int d = Math.Abs(p - idx);
                d = Math.Min(d, n - d);
                if (d < best) best = d;
            }
            ans[qi] = best;
        }
        return ans;
    }
}
