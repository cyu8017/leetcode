// LeetCode 1730 - Shortest Path to Get Food
// https://leetcode.com/problems/shortest-path-to-get-food/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int getFood(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        Deque<int[]> queue = new ArrayDeque<>();
        boolean[][] seen = new boolean[rows][cols];
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '*') {
                    queue.offer(new int[] { r, c, 0 });
                    seen[r][c] = true;
                }
            }
        }
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] entry = queue.poll();
            int r = entry[0];
            int c = entry[1];
            int d = entry[2];
            if (grid[r][c] == '#') {
                return d;
            }
            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !seen[nr][nc] && grid[nr][nc] != 'X') {
                    seen[nr][nc] = true;
                    queue.offer(new int[] { nr, nc, d + 1 });
                }
            }
        }
        return -1;
    }
}
