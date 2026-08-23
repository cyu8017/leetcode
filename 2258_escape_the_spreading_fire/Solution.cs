// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

using System.Collections.Generic;

public class Solution {
    public int MaximumMinutes(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        const int inf = 1000000000;
        int[,] fire = new int[m, n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                fire[i, j] = inf;
        var q = new Queue<(int, int)>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1) { fire[i, j] = 0; q.Enqueue((i, j)); }
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        while (q.Count > 0) {
            var (r, c) = q.Dequeue();
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || fire[nr, nc] != inf) continue;
                fire[nr, nc] = fire[r, c] + 1;
                q.Enqueue((nr, nc));
            }
        }
        bool Can(int wait) {
            if (wait >= fire[0, 0]) return false;
            bool[,] vis = new bool[m, n];
            var qq = new Queue<(int, int, int)>();
            qq.Enqueue((0, 0, wait));
            vis[0, 0] = true;
            while (qq.Count > 0) {
                var (r, c, t) = qq.Dequeue();
                foreach (var d in dirs) {
                    int nr = r + d[0], nc = c + d[1], nt = t + 1;
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || vis[nr, nc]) continue;
                    if (nr == m - 1 && nc == n - 1) {
                        if (nt <= fire[nr, nc]) return true;
                        continue;
                    }
                    if (nt >= fire[nr, nc]) continue;
                    vis[nr, nc] = true;
                    qq.Enqueue((nr, nc, nt));
                }
            }
            return false;
        }
        int lo = 0, hi = m * n + 10, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (Can(mid)) { ans = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        if (ans >= m * n) return inf;
        return ans;
    }
}
