// LeetCode 3643 - Flip Square Submatrix Vertically
// https://leetcode.com/problems/flip-square-submatrix-vertically/

class Solution {
    public int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {
        for (int i = x; i < x + k / 2; i++) {
            int i2 = x + k - 1 - (i - x);
            for (int j = y; j < y + k; j++) {
                int tmp = grid[i][j];
                grid[i][j] = grid[i2][j];
                grid[i2][j] = tmp;
            }
        }
        return grid;
    }
}
