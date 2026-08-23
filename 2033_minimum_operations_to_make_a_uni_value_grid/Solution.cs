// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[][] grid, int x) {
        var vals = new List<int>();
        int bas = grid[0][0] % x;
        foreach (var row in grid) foreach (int v in row) {
            if (v % x != bas) return -1;
            vals.Add(v);
        }
        vals.Sort();
        int median = vals[vals.Count / 2], ans = 0;
        foreach (int v in vals) ans += Math.Abs(v - median) / x;
        return ans;
    }
}
