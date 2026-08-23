// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int minTimeToReach(int[][] moveTime) {
        int m = moveTime.length, n = moveTime[0].length;
        final int INF = 1 << 30;
        int[][][] dist = new int[m][n][2];
        for (int[][] a : dist) for (int[] b : a) Arrays.fill(b, INF);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        dist[0][0][0] = 0;
        pq.offer(new int[] {0, 0, 0, 0});
        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int t = cur[0], r = cur[1], c = cur[2], parity = cur[3];
            if (t != dist[r][c][parity]) continue;
            if (r == m - 1 && c == n - 1) return t;
            int cost = parity == 1 ? 2 : 1;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                int start = Math.max(t, moveTime[nr][nc]);
                int nt = start + cost;
                int np = 1 - parity;
                if (nt < dist[nr][nc][np]) {
                    dist[nr][nc][np] = nt;
                    pq.offer(new int[] {nt, nr, nc, np});
                }
            }
        }
        return -1;
    }
}
