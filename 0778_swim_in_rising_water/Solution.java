// LeetCode 0778 - Swim in Rising Water
// https://leetcode.com/problems/swim-in-rising-water/

import java.util.*;

class Solution {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        boolean[][] seen = new boolean[n][n];
        heap.offer(new int[] {grid[0][0], 0, 0});
        seen[0][0] = true;
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int time = cur[0], r = cur[1], c = cur[2];
            if (r == n - 1 && c == n - 1) return time;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !seen[nr][nc]) {
                    seen[nr][nc] = true;
                    int nt = Math.max(time, grid[nr][nc]);
                    heap.offer(new int[] {nt, nr, nc});
                }
            }
        }
        return -1;
    }
}
