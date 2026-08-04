// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

import java.util.*;

class Solution {
    public int shortestPath(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        if (k >= m + n - 2) return m + n - 2;
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        HashMap<Long, Integer> best = new HashMap<>();
        queue.add(new int[] {0, 0, k, 0});
        best.put(key(0, 0), k);
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            if (cur[0] == m - 1 && cur[1] == n - 1) return cur[3];
            for (int[] d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int nxt = cur[2] - grid[nr][nc];
                if (nxt < 0) continue;
                long cell = key(nr, nc);
                if (best.containsKey(cell) && nxt <= best.get(cell)) continue;
                best.put(cell, nxt);
                queue.add(new int[] {nr, nc, nxt, cur[3] + 1});
            }
        }
        return -1;
    }

    private long key(int r, int c) {
        return ((long) r << 32) | (c & 0xffffffffL);
    }
}
