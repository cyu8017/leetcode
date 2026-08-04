// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

import java.util.*;

class Solution {
    public int maxDistance(int[][] grid) {
        int n = grid.length;
        Queue<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++)
                if (grid[r][c] == 1) queue.offer(new int[]{r, c});
        if (queue.isEmpty() || queue.size() == n * n) return -1;
        int dist = -1;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!queue.isEmpty()) {
            dist++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cur = queue.poll();
                for (int[] d : dirs) {
                    int nr = cur[0] + d[0], nc = cur[1] + d[1];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                        grid[nr][nc] = 1;
                        queue.offer(new int[]{nr, nc});
                    }
                }
            }
        }
        return dist;
    }
}
