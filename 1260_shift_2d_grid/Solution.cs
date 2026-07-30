// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<int>> ShiftGrid(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;
        var flat = grid.SelectMany(row => row).ToList();
        k %= flat.Count;
        if (k > 0) {
            var tail = flat.GetRange(flat.Count - k, k);
            flat.RemoveRange(flat.Count - k, k);
            flat.InsertRange(0, tail);
        }
        var answer = new List<IList<int>>();
        for (int i = 0; i < m; i++) {
            answer.Add(flat.GetRange(i * n, n));
        }
        return answer;
    }
}
