// LeetCode 4003 - Minimum Cost Path with Alternating Directions III
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

using System.Collections.Generic;

public class Solution {
    const long INF = 1L << 60;

    public long MinCost(int m, int n, int[][] penalty) {
        long[][][] dist = new long[m][][];
        for (int i = 0; i < m; i++) {
            dist[i] = new long[n][];
            for (int j = 0; j < n; j++) {
                dist[i][j] = new long[] { INF, INF };
            }
        }
        dist[0][0][1] = 1;
        var pq = new PriorityQueue<(int i, int j, int k), long>();
        pq.Enqueue((0, 0, 1), 1);
        int[][] dirs = new int[][] {
            new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 }, new[] { 1, 0 }
        };
        while (pq.Count > 0) {
            pq.TryDequeue(out var state, out long d);
            int i = state.i, j = state.j, k = state.k;
            if (i == m - 1 && j == n - 1) return d;
            if (d > dist[i][j][k]) continue;
            int p = penalty[i][j];
            long nd = d + p;
            if (nd < dist[i][j][k ^ 1]) {
                dist[i][j][k ^ 1] = nd;
                pq.Enqueue((i, j, k ^ 1), nd);
            }
            for (int idx = 0; idx < 4; idx++) {
                int x = i + dirs[idx][0], y = j + dirs[idx][1];
                if (0 <= x && x < m && 0 <= y && y < n) {
                    nd = d + ((long)(x + 1) * (y + 1) + (((idx & 1) ^ k) * p));
                    if (nd < dist[x][y][k ^ 1]) {
                        dist[x][y][k ^ 1] = nd;
                        pq.Enqueue((x, y, k ^ 1), nd);
                    }
                }
            }
        }
        return -1;
    }
}
