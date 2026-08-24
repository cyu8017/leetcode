// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

class Solution {
    public int maximumMinutes(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        final int inf = 1_000_000_000;
        int[][] fire = new int[m][n];
        for (int i = 0; i < m; i++) Arrays.fill(fire[i], inf);
        Queue<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1) {
                    fire[i][j] = 0;
                    q.offer(new int[] { i, j });
                }
        int[][] dirs = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || fire[nr][nc] != inf)
                    continue;
                fire[nr][nc] = fire[r][c] + 1;
                q.offer(new int[] { nr, nc });
            }
        }
        int lo = 0, hi = m * n + 10, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (can(grid, fire, mid, dirs, inf)) {
                ans = mid;
                lo = mid + 1;
            } else hi = mid - 1;
        }
        if (ans >= m * n) return inf;
        return ans;
    }

    private boolean can(int[][] grid, int[][] fire, int wait, int[][] dirs, int inf) {
        int m = grid.length, n = grid[0].length;
        if (wait >= fire[0][0]) return false;
        boolean[][] vis = new boolean[m][n];
        Queue<int[]> qq = new ArrayDeque<>();
        qq.offer(new int[] { 0, 0, wait });
        vis[0][0] = true;
        while (!qq.isEmpty()) {
            int[] cur = qq.poll();
            int r = cur[0], c = cur[1], t = cur[2];
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1], nt = t + 1;
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || vis[nr][nc])
                    continue;
                if (nr == m - 1 && nc == n - 1) {
                    if (nt <= fire[nr][nc]) return true;
                    continue;
                }
                if (nt >= fire[nr][nc]) continue;
                vis[nr][nc] = true;
                qq.offer(new int[] { nr, nc, nt });
            }
        }
        return false;
    }
}
