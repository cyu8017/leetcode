// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int maximumSafenessFactor(List<List<Integer>> grid) {
        int n = grid.size();
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) dist[i][j] = -1;
        Queue<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (grid.get(i).get(j) == 1) {
                    dist[i][j] = 0;
                    q.offer(new int[]{i, j});
                }
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1];
            for (int[] d : dirs) {
                int ni = x + d[0], nj = y + d[1];
                if (ni >= 0 && nj >= 0 && ni < n && nj < n && dist[ni][nj] == -1) {
                    dist[ni][nj] = dist[x][y] + 1;
                    q.offer(new int[]{ni, nj});
                }
            }
        }
        int lo = 0, hi = n * n, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (ok(dist, dirs, mid)) {
                ans = mid;
                lo = mid + 1;
            } else hi = mid - 1;
        }
        return ans;
    }

    private boolean ok(int[][] dist, int[][] dirs, int sf) {
        int n = dist.length;
        if (dist[0][0] < sf) return false;
        boolean[][] seen = new boolean[n][n];
        List<int[]> st = new ArrayList<>();
        st.add(new int[]{0, 0});
        seen[0][0] = true;
        while (!st.isEmpty()) {
            int[] cur = st.remove(st.size() - 1);
            int x = cur[0], y = cur[1];
            if (x == n - 1 && y == n - 1) return true;
            for (int[] d : dirs) {
                int ni = x + d[0], nj = y + d[1];
                if (ni >= 0 && nj >= 0 && ni < n && nj < n && !seen[ni][nj] && dist[ni][nj] >= sf) {
                    seen[ni][nj] = true;
                    st.add(new int[]{ni, nj});
                }
            }
        }
        return false;
    }
}
