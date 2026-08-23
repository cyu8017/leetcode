// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

using System.Collections.Generic;

public class Solution {
    static readonly int[][] Dirs = {
        new[]{1,2}, new[]{1,-2}, new[]{-1,2}, new[]{-1,-2},
        new[]{2,1}, new[]{2,-1}, new[]{-2,1}, new[]{-2,-1}
    };

    int[] KnightDist(int x, int y, int[][] pts) {
        int np = pts.Length;
        int[] ans = new int[np];
        for (int i = 0; i < np; i++) ans[i] = -1;
        bool[,] vis = new bool[50, 50];
        var q = new Queue<(int, int, int)>();
        q.Enqueue((x, y, 0));
        vis[x, y] = true;
        var need = new Dictionary<(int, int), List<int>>();
        for (int i = 0; i < np; i++) {
            var key = (pts[i][0], pts[i][1]);
            if (!need.ContainsKey(key)) need[key] = new List<int>();
            need[key].Add(i);
        }
        int found = 0;
        while (q.Count > 0 && found < np) {
            var cur = q.Dequeue();
            var key = (cur.Item1, cur.Item2);
            if (need.ContainsKey(key)) {
                foreach (int i in need[key]) {
                    if (ans[i] == -1) {
                        ans[i] = cur.Item3;
                        found++;
                    }
                }
            }
            foreach (var d in Dirs) {
                int nx = cur.Item1 + d[0], ny = cur.Item2 + d[1];
                if (nx < 0 || ny < 0 || nx >= 50 || ny >= 50 || vis[nx, ny]) continue;
                vis[nx, ny] = true;
                q.Enqueue((nx, ny, cur.Item3 + 1));
            }
        }
        return ans;
    }

    public int MaxMoves(int kx, int ky, int[][] positions) {
        int n = positions.Length;
        int[][] pts = new int[n + 1][];
        pts[0] = new[] { kx, ky };
        for (int i = 0; i < n; i++) pts[i + 1] = new[] { positions[i][0], positions[i][1] };
        int[][] dist = new int[n + 1][];
        for (int i = 0; i <= n; i++) dist[i] = KnightDist(pts[i][0], pts[i][1], pts);
        int N = 1 << n;
        int[][] memo = new int[N][];
        for (int i = 0; i < N; i++) {
            memo[i] = new int[n + 1];
            for (int j = 0; j <= n; j++) memo[i][j] = -1;
        }
        int Dfs(int mask, int cur, int turn) {
            if (mask == N - 1) return 0;
            if (memo[mask][cur] != -1) return memo[mask][cur];
            int best = turn == 0 ? -(1 << 30) : (1 << 30);
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) continue;
                int d = dist[cur][i + 1];
                int v = d + Dfs(mask | (1 << i), i + 1, 1 - turn);
                if (turn == 0) {
                    if (v > best) best = v;
                } else if (v < best) best = v;
            }
            return memo[mask][cur] = best;
        }
        return Dfs(0, 0, 0);
    }
}
