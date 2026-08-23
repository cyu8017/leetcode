// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

using System;

public class Solution {
    public long GridGame(int[][] grid) {
        int n = grid[0].Length;
        long top = 0, bottom = 0, ans = long.MaxValue;
        foreach (int v in grid[0]) top += v;
        for (int i = 0; i < n; i++) {
            top -= grid[0][i];
            ans = Math.Min(ans, Math.Max(top, bottom));
            bottom += grid[1][i];
        }
        return ans;
    }
}
