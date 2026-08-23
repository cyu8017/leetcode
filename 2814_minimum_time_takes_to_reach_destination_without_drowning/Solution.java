// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

import java.util.ArrayDeque;
import java.util.List;
import java.util.Queue;

class Solution {
    public int minimumSeconds(List<List<String>> land) {
        int m = land.size(), n = land.get(0).size();
        final int INF = 1 << 30;
        int[][] water = new int[m][n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) water[i][j] = INF;
        Queue<int[]> wq = new ArrayDeque<>();
        int sx = 0, sy = 0, dx = 0, dy = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                String cell = land.get(i).get(j);
                if ("*".equals(cell)) {
                    water[i][j] = 0;
                    wq.offer(new int[]{i, j});
                } else if ("S".equals(cell)) {
                    sx = i;
                    sy = j;
                } else if ("D".equals(cell)) {
                    dx = i;
                    dy = j;
                }
            }
        }
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!wq.isEmpty()) {
            int[] cur = wq.poll();
            int x = cur[0], y = cur[1];
            for (int[] d : dirs) {
                int ni = x + d[0], nj = y + d[1];
                if (ni < 0 || nj < 0 || ni >= m || nj >= n) continue;
                String cell = land.get(ni).get(nj);
                if ("X".equals(cell) || "D".equals(cell)) continue;
                if (water[ni][nj] > water[x][y] + 1) {
                    water[ni][nj] = water[x][y] + 1;
                    wq.offer(new int[]{ni, nj});
                }
            }
        }
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) dist[i][j] = -1;
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{sx, sy});
        dist[sx][sy] = 0;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1];
            if (x == dx && y == dy) return dist[x][y];
            for (int[] d : dirs) {
                int ni = x + d[0], nj = y + d[1];
                if (ni < 0 || nj < 0 || ni >= m || nj >= n || dist[ni][nj] != -1) continue;
                if ("X".equals(land.get(ni).get(nj))) continue;
                int nd = dist[x][y] + 1;
                if (!"D".equals(land.get(ni).get(nj)) && nd >= water[ni][nj]) continue;
                dist[ni][nj] = nd;
                q.offer(new int[]{ni, nj});
            }
        }
        return -1;
    }
}
