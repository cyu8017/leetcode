// LeetCode 2371 - Minimize Maximum Value in a Grid
// https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

import java.util.Arrays;

class Solution {
    public int[][] minScore(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] arr = new int[m * n][3];
        int idx = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                arr[idx++] = new int[] {grid[i][j], i, j};
        Arrays.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));
        int[] rowMax = new int[m], colMax = new int[n];
        int[][] ans = new int[m][n];
        for (int[] cel : arr) {
            int val = Math.max(rowMax[cel[1]], colMax[cel[2]]) + 1;
            ans[cel[1]][cel[2]] = val;
            rowMax[cel[1]] = val;
            colMax[cel[2]] = val;
        }
        return ans;
    }
}
