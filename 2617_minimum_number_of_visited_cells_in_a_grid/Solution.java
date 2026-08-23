// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

class Solution {
    public int minimumVisitedCells(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++) Arrays.fill(dist[i], -1);
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {0, 0});
        dist[0][0] = 1;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            if (r == m - 1 && c == n - 1) return dist[r][c];
            for (int nc = c + 1; nc <= c + grid[r][c] && nc < n; ++nc) {
                if (dist[r][nc] == -1) {
                    dist[r][nc] = dist[r][c] + 1;
                    q.offer(new int[] {r, nc});
                }
            }
            for (int nr = r + 1; nr <= r + grid[r][c] && nr < m; ++nr) {
                if (dist[nr][c] == -1) {
                    dist[nr][c] = dist[r][c] + 1;
                    q.offer(new int[] {nr, c});
                }
            }
        }
        return -1;
    }
}
