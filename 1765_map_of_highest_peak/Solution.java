// LeetCode 1765 - Map of Highest Peak
// https://leetcode.com/problems/map-of-highest-peak/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int[][] highestPeak(int[][] isWater) {
        int m = isWater.length;
        int n = isWater[0].length;
        int[][] dist = new int[m][n];
        for (int[] row : dist) {
            java.util.Arrays.fill(row, -1);
        }
        Deque<int[]> queue = new ArrayDeque<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (isWater[i][j] == 1) {
                    dist[i][j] = 0;
                    queue.offer(new int[] { i, j });
                }
            }
        }
        int[][] dirs = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int i = cell[0];
            int j = cell[1];
            for (int[] d : dirs) {
                int x = i + d[0];
                int y = j + d[1];
                if (x >= 0 && x < m && y >= 0 && y < n && dist[x][y] == -1) {
                    dist[x][y] = dist[i][j] + 1;
                    queue.offer(new int[] { x, y });
                }
            }
        }
        return dist;
    }
}
