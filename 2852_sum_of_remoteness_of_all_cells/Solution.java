// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public long sumRemoteness(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        boolean[][] seen = new boolean[m][n];
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        long total = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] != -1) total += grid[i][j];
        long ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == -1 || seen[i][j]) continue;
                Queue<int[]> q = new ArrayDeque<>();
                q.offer(new int[] {i, j});
                seen[i][j] = true;
                long sum = 0;
                int cnt = 0;
                while (!q.isEmpty()) {
                    int[] cur = q.poll();
                    int x = cur[0], y = cur[1];
                    sum += grid[x][y];
                    cnt++;
                    for (int[] d : dirs) {
                        int ni = x + d[0], nj = y + d[1];
                        if (ni >= 0 && nj >= 0 && ni < m && nj < n && !seen[ni][nj] && grid[ni][nj] != -1) {
                            seen[ni][nj] = true;
                            q.offer(new int[] {ni, nj});
                        }
                    }
                }
                ans += (total - sum) * cnt;
            }
        }
        return ans;
    }
}
