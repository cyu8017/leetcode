// LeetCode 1631 - Path With Minimum Effort
// https://leetcode.com/problems/path-with-minimum-effort/

import java.util.*;

class Solution {
    public int minimumEffortPath(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        int[][] dist = new int[m][n];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        dist[0][0] = 0;
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.offer(new int[] {0, 0, 0});
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int effort = cur[0], i = cur[1], j = cur[2];
            if (i == m - 1 && j == n - 1) return effort;
            if (effort != dist[i][j]) continue;
            for (int[] d : dirs) {
                int x = i + d[0], y = j + d[1];
                if (x >= 0 && x < m && y >= 0 && y < n) {
                    int nd = Math.max(effort, Math.abs(heights[i][j] - heights[x][y]));
                    if (nd < dist[x][y]) {
                        dist[x][y] = nd;
                        heap.offer(new int[] {nd, x, y});
                    }
                }
            }
        }
        return 0;
    }
}
