// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int minTimeToReach(int[][] moveTime) {
        int m = moveTime.length, n = moveTime[0].length;
        int[][] dist = new int[m][n];
        for (int[] row : dist) Arrays.fill(row, 1 << 30);
        PriorityQueue<int[]> h = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        h.offer(new int[] {0, 0, 0});
        dist[0][0] = 0;
        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!h.isEmpty()) {
            int[] cur = h.poll();
            int t = cur[0], r = cur[1], c = cur[2];
            if (t != dist[r][c]) continue;
            if (r == m - 1 && c == n - 1) return t;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                int start = Math.max(t, moveTime[nr][nc]);
                int nt = start + 1;
                if (nt < dist[nr][nc]) {
                    dist[nr][nc] = nt;
                    h.offer(new int[] {nt, nr, nc});
                }
            }
        }
        return -1;
    }
}
