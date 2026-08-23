// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

import java.util.*;

class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        if (rows < 3 || cols < 3) return 0;
        int ans = 0;
        for (int i = 0; i < rows - 2; i++) {
            for (int j = 0; j < cols - 2; j++) {
                if (magic(grid, i, j)) ans++;
            }
        }
        return ans;
    }

    private boolean magic(int[][] a, int r, int c) {
        int[] vals = new int[9];
        int k = 0;
        for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) vals[k++] = a[r + i][c + j];
        Arrays.sort(vals);
        for (int i = 0; i < 9; i++) if (vals[i] != i + 1) return false;
        return a[r][c] + a[r][c + 1] + a[r][c + 2] == 15
            && a[r + 1][c] + a[r + 1][c + 1] + a[r + 1][c + 2] == 15
            && a[r + 2][c] + a[r + 2][c + 1] + a[r + 2][c + 2] == 15
            && a[r][c] + a[r + 1][c] + a[r + 2][c] == 15
            && a[r][c + 1] + a[r + 1][c + 1] + a[r + 2][c + 1] == 15
            && a[r][c + 2] + a[r + 1][c + 2] + a[r + 2][c + 2] == 15
            && a[r][c] + a[r + 1][c + 1] + a[r + 2][c + 2] == 15
            && a[r][c + 2] + a[r + 1][c + 1] + a[r + 2][c] == 15;
    }
}
