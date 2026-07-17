// LeetCode 1778 - Shortest Path in a Hidden Grid
// https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    private static final int[][] DIRS = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

    private static class GridMaster {
        private final int[][] grid;
        private final int m;
        private final int n;
        private int r;
        private int c;

        GridMaster(int[][] grid) {
            this.grid = grid;
            this.m = grid.length;
            this.n = grid[0].length;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (grid[i][j] == -1) {
                        r = i;
                        c = j;
                    }
                }
            }
        }

        boolean canMove(int d) {
            int nr = r + DIRS[d][0];
            int nc = c + DIRS[d][1];
            return nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != 0;
        }

        void move(int d) {
            if (canMove(d)) {
                r += DIRS[d][0];
                c += DIRS[d][1];
            }
        }

        boolean isTarget() {
            return grid[r][c] == 2;
        }
    }

    private GridMaster master;
    private Set<Long> world;
    private Long target;

    public int findShortestPath(int[][] grid) {
        master = new GridMaster(grid);
        world = new HashSet<>();
        world.add(encode(0, 0));
        target = null;
        if (master.isTarget()) {
            return 0;
        }
        dfs(0, 0);
        if (target == null) {
            return -1;
        }
        Deque<long[]> queue = new ArrayDeque<>();
        queue.add(new long[] { 0, 0, 0 });
        Set<Long> seen = new HashSet<>();
        seen.add(encode(0, 0));
        while (!queue.isEmpty()) {
            long[] cur = queue.poll();
            int cr = (int) cur[0];
            int cc = (int) cur[1];
            int dist = (int) cur[2];
            if (encode(cr, cc).equals(target)) {
                return dist;
            }
            for (int[] dir : DIRS) {
                int nr = cr + dir[0];
                int nc = cc + dir[1];
                Long key = encode(nr, nc);
                if (world.contains(key) && !seen.contains(key)) {
                    seen.add(key);
                    queue.add(new long[] { nr, nc, dist + 1 });
                }
            }
        }
        return -1;
    }

    private void dfs(int r, int c) {
        for (int d = 0; d < 4; d++) {
            if (!master.canMove(d)) {
                continue;
            }
            master.move(d);
            int nr = r + DIRS[d][0];
            int nc = c + DIRS[d][1];
            Long key = encode(nr, nc);
            if (!world.contains(key)) {
                world.add(key);
                if (master.isTarget()) {
                    target = key;
                }
                dfs(nr, nc);
            }
            master.move(d ^ 1);
        }
    }

    private Long encode(int r, int c) {
        return ((long) r << 32) ^ (c & 0xffffffffL);
    }
}
