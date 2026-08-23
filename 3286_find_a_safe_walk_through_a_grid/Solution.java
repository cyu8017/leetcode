// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

class Solution {
    public boolean findSafeWalk(int[][] grid, int health) {
        int m = grid.length, n = grid[0].length;
        int[][] vis = new int[m][n];
        for (int[] row : vis) Arrays.fill(row, -1);
        int qh = health - grid[0][0];
        if (qh <= 0) return false;
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {0, 0, qh});
        vis[0][0] = qh;
        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            if (cur[0] == m - 1 && cur[1] == n - 1) return true;
            for (int[] d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                int nh = cur[2] - grid[nr][nc];
                if (nh <= 0) continue;
                if (nh > vis[nr][nc]) {
                    vis[nr][nc] = nh;
                    q.offer(new int[] {nr, nc, nh});
                }
            }
        }
        return false;
    }
}
