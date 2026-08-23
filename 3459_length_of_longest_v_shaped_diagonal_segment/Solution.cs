// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

using System.Collections.Generic;

public class Solution {
    public int LenOfVDiagonal(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[][] dirs = { new[] { 1, 1 }, new[] { 1, -1 }, new[] { -1, -1 }, new[] { -1, 1 } };
        int[] nextDir = { 1, 2, 3, 0 };
        int ans = 0;
        var memo = new Dictionary<(int, int, int, int, int), int>();
        int Dfs(int i, int j, int d, int turned, int expect) {
            if (i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != expect) return 0;
            var key = (i, j, d, turned, expect);
            if (memo.TryGetValue(key, out int cached)) return cached;
            int ni = i + dirs[d][0], nj = j + dirs[d][1];
            int nx = (expect == 2) ? 0 : 2;
            int best = 1 + Dfs(ni, nj, d, turned, nx);
            if (turned == 0) {
                int nd = nextDir[d];
                int ti = i + dirs[nd][0], tj = j + dirs[nd][1];
                int cand = 1 + Dfs(ti, tj, nd, 1, nx);
                if (cand > best) best = cand;
            }
            return memo[key] = best;
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 1) continue;
                for (int d = 0; d < 4; d++) {
                    int ni = i + dirs[d][0], nj = j + dirs[d][1];
                    int best = 1 + Dfs(ni, nj, d, 0, 2);
                    if (best > ans) ans = best;
                }
                if (ans < 1) ans = 1;
            }
        }
        return ans;
    }
}
