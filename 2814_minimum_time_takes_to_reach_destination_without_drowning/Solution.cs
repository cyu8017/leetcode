// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

using System.Collections.Generic;

public class Solution {
    public int MinimumSeconds(IList<IList<string>> land) {
        int m = land.Count, n = land[0].Count;
        const int INF = 1 << 30;
        int[][] water = new int[m][];
        for (int i = 0; i < m; i++) {
            water[i] = new int[n];
            for (int j = 0; j < n; j++) water[i][j] = INF;
        }
        var wq = new Queue<(int, int)>();
        (int, int) start = (0, 0), dest = (0, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (land[i][j] == "*") { water[i][j] = 0; wq.Enqueue((i, j)); }
                else if (land[i][j] == "S") start = (i, j);
                else if (land[i][j] == "D") dest = (i, j);
            }
        }
        int[][] dirs = { new[]{1,0}, new[]{-1,0}, new[]{0,1}, new[]{0,-1} };
        while (wq.Count > 0) {
            var (x, y) = wq.Dequeue();
            foreach (var d in dirs) {
                int ni = x + d[0], nj = y + d[1];
                if (ni < 0 || nj < 0 || ni >= m || nj >= n) continue;
                if (land[ni][nj] == "X" || land[ni][nj] == "D") continue;
                if (water[ni][nj] > water[x][y] + 1) {
                    water[ni][nj] = water[x][y] + 1;
                    wq.Enqueue((ni, nj));
                }
            }
        }
        int[][] dist = new int[m][];
        for (int i = 0; i < m; i++) {
            dist[i] = new int[n];
            for (int j = 0; j < n; j++) dist[i][j] = -1;
        }
        var q = new Queue<(int, int)>();
        q.Enqueue(start);
        dist[start.Item1][start.Item2] = 0;
        while (q.Count > 0) {
            var (x, y) = q.Dequeue();
            if (x == dest.Item1 && y == dest.Item2) return dist[x][y];
            foreach (var d in dirs) {
                int ni = x + d[0], nj = y + d[1];
                if (ni < 0 || nj < 0 || ni >= m || nj >= n || dist[ni][nj] != -1) continue;
                if (land[ni][nj] == "X") continue;
                int nd = dist[x][y] + 1;
                if (land[ni][nj] != "D" && nd >= water[ni][nj]) continue;
                dist[ni][nj] = nd;
                q.Enqueue((ni, nj));
            }
        }
        return -1;
    }
}
