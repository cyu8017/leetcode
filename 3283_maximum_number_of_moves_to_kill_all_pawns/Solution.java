// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;

class Solution {
    private static final int[][] DIRS = {
        {1, 2}, {1, -2}, {-1, 2}, {-1, -2},
        {2, 1}, {2, -1}, {-2, 1}, {-2, -1}
    };

    private int[] knightDist(int x, int y, int[][] pts) {
        int np = pts.length;
        int[] ans = new int[np];
        for (int i = 0; i < np; i++) {
            ans[i] = -1;
        }
        boolean[][] vis = new boolean[50][50];
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {x, y, 0});
        vis[x][y] = true;
        Map<Long, List<Integer>> need = new HashMap<>();
        for (int i = 0; i < np; i++) {
            long key = (((long) pts[i][0]) << 32) | (pts[i][1] & 0xffffffffL);
            need.computeIfAbsent(key, z -> new ArrayList<>()).add(i);
        }
        int found = 0;
        while (!q.isEmpty() && found < np) {
            int[] cur = q.poll();
            long key = (((long) cur[0]) << 32) | (cur[1] & 0xffffffffL);
            List<Integer> idxs = need.get(key);
            if (idxs != null) {
                for (int i : idxs) {
                    if (ans[i] == -1) {
                        ans[i] = cur[2];
                        found++;
                    }
                }
            }
            for (int[] d : DIRS) {
                int nx = cur[0] + d[0], ny = cur[1] + d[1];
                if (nx < 0 || ny < 0 || nx >= 50 || ny >= 50 || vis[nx][ny]) {
                    continue;
                }
                vis[nx][ny] = true;
                q.offer(new int[] {nx, ny, cur[2] + 1});
            }
        }
        return ans;
    }

    public int maxMoves(int kx, int ky, int[][] positions) {
        int n = positions.length;
        int[][] pts = new int[n + 1][2];
        pts[0][0] = kx;
        pts[0][1] = ky;
        for (int i = 0; i < n; i++) {
            pts[i + 1][0] = positions[i][0];
            pts[i + 1][1] = positions[i][1];
        }
        int[][] dist = new int[n + 1][];
        for (int i = 0; i <= n; i++) {
            dist[i] = knightDist(pts[i][0], pts[i][1], pts);
        }
        int N = 1 << n;
        int[][] memo = new int[N][n + 1];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= n; j++) {
                memo[i][j] = -1;
            }
        }
        return dfs(0, 0, 0, n, N, dist, memo);
    }

    private int dfs(int mask, int cur, int turn, int n, int N, int[][] dist, int[][] memo) {
        if (mask == N - 1) {
            return 0;
        }
        if (memo[mask][cur] != -1) {
            return memo[mask][cur];
        }
        int best = turn == 0 ? -(1 << 30) : (1 << 30);
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                continue;
            }
            int d = dist[cur][i + 1];
            int v = d + dfs(mask | (1 << i), i + 1, 1 - turn, n, N, dist, memo);
            if (turn == 0) {
                if (v > best) {
                    best = v;
                }
            } else if (v < best) {
                best = v;
            }
        }
        return memo[mask][cur] = best;
    }
}
