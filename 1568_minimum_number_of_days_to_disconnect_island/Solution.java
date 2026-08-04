// LeetCode 1568 - Minimum Number of Days to Disconnect Island
// https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

import java.util.*;

class Solution {
    public int minDays(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        if (islands(grid, m, n) != 1) {
            return 0;
        }
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    grid[r][c] = 0;
                    if (islands(grid, m, n) != 1) {
                        grid[r][c] = 1;
                        return 1;
                    }
                    grid[r][c] = 1;
                }
            }
        }
        return 2;
    }

    private int islands(int[][] grid, int m, int n) {
        boolean[][] seen = new boolean[m][n];
        int count = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1 && !seen[r][c]) {
                    count++;
                    ArrayDeque<int[]> stack = new ArrayDeque<>();
                    stack.push(new int[] {r, c});
                    seen[r][c] = true;
                    while (!stack.isEmpty()) {
                        int[] cur = stack.pop();
                        for (int[] d : dirs) {
                            int nx = cur[0] + d[0];
                            int ny = cur[1] + d[1];
                            if (nx >= 0 && nx < m && ny >= 0 && ny < n
                                    && grid[nx][ny] == 1 && !seen[nx][ny]) {
                                seen[nx][ny] = true;
                                stack.push(new int[] {nx, ny});
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
}
