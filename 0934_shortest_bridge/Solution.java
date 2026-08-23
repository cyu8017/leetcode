// LeetCode 0934 - Shortest Bridge
// https://leetcode.com/problems/shortest-bridge/

import java.util.*;

class Solution {
    private int n;
    private int[][] grid;
    private final int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int shortestBridge(int[][] grid) {
        this.grid = grid;
        n = grid.length;
        boolean found = false;
        for (int i = 0; i < n && !found; i++)
            for (int j = 0; j < n && !found; j++)
                if (grid[i][j] == 1) { dfs(i, j); found = true; }
        Queue<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 2) q.offer(new int[] {i, j, 0});
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1], dist = cur[2];
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
                if (grid[nr][nc] == 1) return dist;
                if (grid[nr][nc] == 0) {
                    grid[nr][nc] = 2;
                    q.offer(new int[] {nr, nc, dist + 1});
                }
            }
        }
        return -1;
    }

    private void dfs(int r, int c) {
        if (r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1) return;
        grid[r][c] = 2;
        for (int[] d : dirs) dfs(r + d[0], c + d[1]);
    }
}
