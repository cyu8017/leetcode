// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

using System;

public class Solution {
    public int MaxTrailingZeros(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        (int, int) Fact(int x) {
            int t = 0, f = 0;
            while (x % 2 == 0) { t++; x /= 2; }
            while (x % 5 == 0) { f++; x /= 5; }
            return (t, f);
        }
        var left = new (int, int)[m, n];
        var up = new (int, int)[m, n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                var p = Fact(grid[i][j]);
                left[i, j] = up[i, j] = p;
                if (j > 0) left[i, j] = (left[i, j].Item1 + left[i, j - 1].Item1, left[i, j].Item2 + left[i, j - 1].Item2);
                if (i > 0) up[i, j] = (up[i, j].Item1 + up[i - 1, j].Item1, up[i, j].Item2 + up[i - 1, j].Item2);
            }
        }
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                var cell = Fact(grid[i][j]);
                var L = left[i, j];
                int Rtwo = left[i, n - 1].Item1 - left[i, j].Item1 + cell.Item1;
                int Rfive = left[i, n - 1].Item2 - left[i, j].Item2 + cell.Item2;
                var U = up[i, j];
                int Dtwo = up[m - 1, j].Item1 - up[i, j].Item1 + cell.Item1;
                int Dfive = up[m - 1, j].Item2 - up[i, j].Item2 + cell.Item2;
                var cands = new (int, int)[] {
                    (L.Item1 + U.Item1 - cell.Item1, L.Item2 + U.Item2 - cell.Item2),
                    (L.Item1 + Dtwo - cell.Item1, L.Item2 + Dfive - cell.Item2),
                    (Rtwo + U.Item1 - cell.Item1, Rfive + U.Item2 - cell.Item2),
                    (Rtwo + Dtwo - cell.Item1, Rfive + Dfive - cell.Item2),
                };
                foreach (var c in cands) ans = Math.Max(ans, Math.Min(c.Item1, c.Item2));
            }
        }
        return ans;
    }
}
