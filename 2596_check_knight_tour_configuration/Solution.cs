// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/

public class Solution {
    public bool CheckValidGrid(int[][] grid) {
        int n = grid.Length;
        if (grid[0][0] != 0) return false;
        var pos = new (int, int)[n * n];
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                pos[grid[i][j]] = (i, j);
        int[][] dirs = {
            new[] { 1, 2 }, new[] { 1, -2 }, new[] { -1, 2 }, new[] { -1, -2 },
            new[] { 2, 1 }, new[] { 2, -1 }, new[] { -2, 1 }, new[] { -2, -1 }
        };
        for (int v = 0; v + 1 < n * n; ++v) {
            int r = pos[v].Item1, c = pos[v].Item2;
            bool ok = false;
            foreach (var d in dirs) {
                if (r + d[0] == pos[v + 1].Item1 && c + d[1] == pos[v + 1].Item2) {
                    ok = true;
                    break;
                }
            }
            if (!ok) return false;
        }
        return true;
    }
}
