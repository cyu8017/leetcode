// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

using System.Collections.Generic;

public class Solution {
    public bool FindSafeWalk(IList<IList<int>> grid, int health) {
        int m = grid.Count, n = grid[0].Count;
        int[][] vis = new int[m][];
        for (int i = 0; i < m; i++) {
            vis[i] = new int[n];
            for (int j = 0; j < n; j++) vis[i][j] = -1;
        }
        int qh = health - grid[0][0];
        if (qh <= 0) return false;
        var q = new Queue<(int, int, int)>();
        q.Enqueue((0, 0, qh));
        vis[0][0] = qh;
        int[][] dirs = new int[][] {
            new int[] { 0, 1 }, new int[] { 1, 0 },
            new int[] { 0, -1 }, new int[] { -1, 0 }
        };
        while (q.Count > 0) {
            var cur = q.Dequeue();
            if (cur.Item1 == m - 1 && cur.Item2 == n - 1) return true;
            foreach (var d in dirs) {
                int nr = cur.Item1 + d[0], nc = cur.Item2 + d[1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                int nh = cur.Item3 - grid[nr][nc];
                if (nh <= 0) continue;
                if (nh > vis[nr][nc]) {
                    vis[nr][nc] = nh;
                    q.Enqueue((nr, nc, nh));
                }
            }
        }
        return false;
    }
}
