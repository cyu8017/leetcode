// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

using System;

public class Solution {
    public int NumMagicSquaresInside(int[][] grid) {
        int rows = grid.Length, cols = grid[0].Length;
        if (rows < 3 || cols < 3) return 0;
        bool Magic(int r, int c) {
            int[] vals = new int[9];
            int p = 0;
            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    vals[p++] = grid[r + i][c + j];
            Array.Sort(vals);
            for (int i = 0; i < 9; i++) if (vals[i] != i + 1) return false;
            var a = grid;
            return a[r][c] + a[r][c + 1] + a[r][c + 2] == 15 &&
                   a[r + 1][c] + a[r + 1][c + 1] + a[r + 1][c + 2] == 15 &&
                   a[r + 2][c] + a[r + 2][c + 1] + a[r + 2][c + 2] == 15 &&
                   a[r][c] + a[r + 1][c] + a[r + 2][c] == 15 &&
                   a[r][c + 1] + a[r + 1][c + 1] + a[r + 2][c + 1] == 15 &&
                   a[r][c + 2] + a[r + 1][c + 2] + a[r + 2][c + 2] == 15 &&
                   a[r][c] + a[r + 1][c + 1] + a[r + 2][c + 2] == 15 &&
                   a[r][c + 2] + a[r + 1][c + 1] + a[r + 2][c] == 15;
        }
        int ans = 0;
        for (int i = 0; i < rows - 2; i++)
            for (int j = 0; j < cols - 2; j++)
                if (Magic(i, j)) ans++;
        return ans;
    }
}
