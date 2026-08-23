// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumMoves(int[][] grid) {
        var extras = new List<(int, int)>();
        var zeros = new List<(int, int)>();
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[i][j] == 0) zeros.Add((i, j));
                else if (grid[i][j] > 1) {
                    for (int k = 0; k < grid[i][j] - 1; k++) extras.Add((i, j));
                }
            }
        }
        if (zeros.Count == 0) return 0;
        int best = 1 << 30;
        void Dfs(int i, int cost) {
            if (cost >= best) return;
            if (i == zeros.Count) { best = cost; return; }
            for (int j = 0; j < extras.Count; j++) {
                if (extras[j].Item1 < 0) continue;
                var e = extras[j];
                extras[j] = (-1, e.Item2);
                int d = Math.Abs(e.Item1 - zeros[i].Item1) + Math.Abs(e.Item2 - zeros[i].Item2);
                Dfs(i + 1, cost + d);
                extras[j] = e;
            }
        }
        Dfs(0, 0);
        return best;
    }
}
