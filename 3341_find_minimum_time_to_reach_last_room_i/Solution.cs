// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

using System.Collections.Generic;

public class Solution {
    public int MinTimeToReach(int[][] moveTime) {
        int m = moveTime.Length, n = moveTime[0].Length;
        int[][] dist = new int[m][];
        for (int i = 0; i < m; i++) {
            dist[i] = new int[n];
            for (int j = 0; j < n; j++) dist[i][j] = 1 << 30;
        }
        var pq = new PriorityQueue<(int t, int r, int c), int>();
        pq.Enqueue((0, 0, 0), 0);
        dist[0][0] = 0;
        int[][] dirs = new int[][] {
            new int[] { 0, 1 }, new int[] { 1, 0 },
            new int[] { 0, -1 }, new int[] { -1, 0 }
        };
        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            int t = cur.t, r = cur.r, c = cur.c;
            if (t != dist[r][c]) continue;
            if (r == m - 1 && c == n - 1) return t;
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                int start = t;
                if (moveTime[nr][nc] > start) start = moveTime[nr][nc];
                int nt = start + 1;
                if (nt < dist[nr][nc]) {
                    dist[nr][nc] = nt;
                    pq.Enqueue((nt, nr, nc), nt);
                }
            }
        }
        return -1;
    }
}
