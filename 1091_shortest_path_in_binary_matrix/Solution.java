// LeetCode 1091 - Shortest Path in Binary Matrix
// https://leetcode.com/problems/shortest-path-in-binary-matrix/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) {
            return -1;
        }
        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] { 0, 0, 1 });
        grid[0][0] = 1;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0], c = cur[1], dist = cur[2];
            if (r == n - 1 && c == n - 1) {
                return dist;
            }
            for (int dr = -1; dr <= 1; dr++) {
                for (int dc = -1; dc <= 1; dc++) {
                    if (dr == 0 && dc == 0) {
                        continue;
                    }
                    int nr = r + dr, nc = c + dc;
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                        grid[nr][nc] = 1;
                        queue.offer(new int[] { nr, nc, dist + 1 });
                    }
                }
            }
        }
        return -1;
    }
}
