// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

using System;
using System.Collections.Generic;

public class Solution {
    public int[][] SortMatrix(int[][] grid) {
        int n = grid.Length;
        var diags = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int key = i - j;
                if (!diags.ContainsKey(key)) diags[key] = new List<int>();
                diags[key].Add(grid[i][j]);
            }
        }
        foreach (var kv in diags) {
            if (kv.Key >= 0) kv.Value.Sort((a, b) => b.CompareTo(a));
            else kv.Value.Sort();
        }
        var idx = new Dictionary<int, int>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int key = i - j;
                if (!idx.ContainsKey(key)) idx[key] = 0;
                grid[i][j] = diags[key][idx[key]++];
            }
        }
        return grid;
    }
}
