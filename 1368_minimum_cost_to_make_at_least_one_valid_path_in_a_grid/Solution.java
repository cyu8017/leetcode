// LeetCode 1368 - Minimum Cost To Make At Least One Valid Path In A Grid
// https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

import java.util.*;

class Solution {
    public int minCost(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++) Arrays.fill(dist[i], Integer.MAX_VALUE / 4);
        dist[0][0] = 0;
        Deque<int[]> q = new ArrayDeque<>();
        q.addFirst(new int[]{0, 0});
        int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!q.isEmpty()) {
            int[] cur = q.pollFirst();
            int r = cur[0], c = cur[1];
            for (int k = 0; k < 4; k++) {
                int x = r + dirs[k][0], y = c + dirs[k][1];
                if (x >= 0 && x < m && y >= 0 && y < n) {
                    int w = (k + 1 != grid[r][c]) ? 1 : 0;
                    int nd = dist[r][c] + w;
                    if (nd < dist[x][y]) {
                        dist[x][y] = nd;
                        if (w == 0) q.addFirst(new int[]{x, y});
                        else q.addLast(new int[]{x, y});
                    }
                }
            }
        }
        return dist[m - 1][n - 1];
    }
}
