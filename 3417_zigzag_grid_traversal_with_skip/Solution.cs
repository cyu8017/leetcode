// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

using System.Collections.Generic;

public class Solution {
    public int[] ZigzagTraversal(int[][] grid) {
        var ans = new List<int>();
        bool skip = false;
        for (int i = 0; i < grid.Length; i++) {
            var row = grid[i];
            if (i % 2 == 0) {
                foreach (int v in row) {
                    if (!skip) ans.Add(v);
                    skip = !skip;
                }
            } else {
                for (int j = row.Length - 1; j >= 0; j--) {
                    if (!skip) ans.Add(row[j]);
                    skip = !skip;
                }
            }
        }
        return ans.ToArray();
    }
}
