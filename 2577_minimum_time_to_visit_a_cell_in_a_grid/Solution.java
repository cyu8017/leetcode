// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

import java.util.PriorityQueue;

class Solution {
    public int minimumTime(int[][] grid) {
        if (grid[0][1] > 1 && grid[1][0] > 1) return -1;
        int m = grid.length, n = grid[0].length;
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) dist[i][j] = 1 << 30;
        PriorityQueue<int[]> h = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        h.offer(new int[] {0, 0, 0});
        dist[0][0] = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!h.isEmpty()) {
            int[] cur = h.poll();
            int t = cur[0], r = cur[1], c = cur[2];
            if (r == m - 1 && c == n - 1) return t;
            if (t > dist[r][c]) continue;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int nt = t + 1;
                if (nt < grid[nr][nc]) {
                    int wait = grid[nr][nc] - nt;
                    if (wait % 2 == 1) wait++;
                    nt += wait;
                }
                if (nt < dist[nr][nc]) {
                    dist[nr][nc] = nt;
                    h.offer(new int[] {nt, nr, nc});
                }
            }
        }
        return -1;
    }
}
