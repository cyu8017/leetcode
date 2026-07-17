// LeetCode 1727 - Largest Submatrix With Rearrangements
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/

import java.util.Arrays;

class Solution {
    public int largestSubmatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[] heights = new int[n];
        int best = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                heights[c] = matrix[r][c] == 1 ? heights[c] + 1 : 0;
            }
            int[] sorted = heights.clone();
            Arrays.sort(sorted);
            for (int width = 1; width <= n; width++) {
                best = Math.max(best, width * sorted[n - width]);
            }
        }
        return best;
    }
}
