// LeetCode 0296 - Best Meeting Point
// https://leetcode.com/problems/best-meeting-point/

using System;
using System.Linq;

public class Solution {
    public int MinTotalDistance(int[][] grid) {
        var rows = new System.Collections.Generic.List<int>();
        var cols = new System.Collections.Generic.List<int>();
        for (int rowIndex = 0; rowIndex < grid.Length; rowIndex++) {
            for (int colIndex = 0; colIndex < grid[rowIndex].Length; colIndex++) {
                if (grid[rowIndex][colIndex] == 1) {
                    rows.Add(rowIndex);
                    cols.Add(colIndex);
                }
            }
        }
        cols.Sort();
        int rowMedian = rows[rows.Count / 2];
        int colMedian = cols[cols.Count / 2];
        return rows.Sum(row => Math.Abs(row - rowMedian)) + cols.Sum(col => Math.Abs(col - colMedian));
    }
}
