// LeetCode 3195 - Find the Minimum Area to Cover All Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

class Solution {
    public int minimumArea(int[][] grid) {
        int x1 = grid.length, y1 = grid[0].length, x2 = 0, y2 = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    x1 = Math.min(x1, i); y1 = Math.min(y1, j);
                    x2 = Math.max(x2, i); y2 = Math.max(y2, j);
                }
            }
        }
        return (x2 - x1 + 1) * (y2 - y1 + 1);
    }
}
