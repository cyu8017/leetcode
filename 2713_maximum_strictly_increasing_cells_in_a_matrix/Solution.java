// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

import java.util.*;

class Solution {
    public int maxIncreasingCells(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        List<int[]> cells = new ArrayList<>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                cells.add(new int[] {mat[i][j], i, j});
        cells.sort(Comparator.comparingInt(a -> a[0]));
        int[] rowMax = new int[m], colMax = new int[n];
        int[][] dp = new int[m][n];
        int ans = 0;
        for (int i = 0; i < cells.size(); ) {
            int j = i;
            while (j < cells.size() && cells.get(j)[0] == cells.get(i)[0]) j++;
            List<int[]> buf = new ArrayList<>();
            for (int k = i; k < j; k++) {
                int r = cells.get(k)[1], c = cells.get(k)[2];
                int best = Math.max(rowMax[r], colMax[c]);
                dp[r][c] = best + 1;
                ans = Math.max(ans, dp[r][c]);
                buf.add(new int[] {r, c, dp[r][c]});
            }
            for (int[] b : buf) {
                rowMax[b[0]] = Math.max(rowMax[b[0]], b[2]);
                colMax[b[1]] = Math.max(colMax[b[1]], b[2]);
            }
            i = j;
        }
        return ans;
    }
}
