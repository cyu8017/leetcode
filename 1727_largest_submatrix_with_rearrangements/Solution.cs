// LeetCode 1727 - Largest Submatrix With Rearrangements
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/

using System;

public class Solution {
    public int LargestSubmatrix(int[][] matrix) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        int[] heights = new int[n];
        int best = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                heights[c] = matrix[r][c] == 1 ? heights[c] + 1 : 0;
            }
            int[] sorted = (int[])heights.Clone();
            Array.Sort(sorted);
            for (int width = 1; width <= n; width++) {
                best = Math.Max(best, width * sorted[n - width]);
            }
        }
        return best;
    }
}
