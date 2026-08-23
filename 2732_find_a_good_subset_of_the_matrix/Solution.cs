// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

using System.Collections.Generic;

public class Solution {
    public IList<int> GoodSubsetofBinaryMatrix(int[][] grid) {
        int n = grid[0].Length;
        var first = new Dictionary<int, int>();
        for (int i = 0; i < grid.Length; i++) {
            int mask = 0;
            for (int j = 0; j < n; j++) if (grid[i][j] == 1) mask |= 1 << j;
            if (mask == 0) return new List<int> { i };
            foreach (var kv in first) {
                if ((kv.Key & mask) == 0) {
                    if (kv.Value < i) return new List<int> { kv.Value, i };
                    return new List<int> { i, kv.Value };
                }
            }
            if (!first.ContainsKey(mask)) first[mask] = i;
        }
        return new List<int>();
    }
}
