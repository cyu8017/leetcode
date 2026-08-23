// LeetCode 1102 - Path With Maximum Minimum Value
// https://leetcode.com/problems/path-with-maximum-minimum-value/

import java.util.*;

class Solution {
    public int maximumMinimumPath(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        heap.offer(new int[]{grid[0][0], 0, 0});
        boolean[][] seen = new boolean[m][n];
        seen[0][0] = true;
        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};
        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int val = cur[0], r = cur[1], c = cur[2];
            if (r == m - 1 && c == n - 1) return val;
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen[nr][nc]) {
                    seen[nr][nc] = true;
                    heap.offer(new int[]{Math.min(val, grid[nr][nc]), nr, nc});
                }
            }
        }
        return grid[0][0];
    }
}
