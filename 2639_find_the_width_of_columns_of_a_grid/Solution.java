// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution {
    public int[] findColumnWidth(int[][] grid) {
        int n = grid[0].length;
        int[] ans = new int[n];
        for (int[] row : grid) {
            for (int j = 0; j < n; j++) {
                int w = width(row[j]);
                if (w > ans[j]) ans[j] = w;
            }
        }
        return ans;
    }

    private int width(int x) {
        if (x == 0) return 1;
        int w = 0;
        if (x < 0) {
            w++;
            x = -x;
        }
        while (x > 0) {
            w++;
            x /= 10;
        }
        return w;
    }
}
