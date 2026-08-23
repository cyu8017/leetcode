// LeetCode 0750 - Number Of Corner Rectangles
// https://leetcode.com/problems/number-of-corner-rectangles/

public class Solution {
    public int CountCornerRectangles(int[][] grid) {
        int m = grid.Length, n = grid[0].Length, ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = i + 1; j < m; j++) {
                int count = 0;
                for (int c = 0; c < n; c++) if (grid[i][c] == 1 && grid[j][c] == 1) count++;
                ans += count * (count - 1) / 2;
            }
        }
        return ans;
    }
}
