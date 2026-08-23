// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

import java.util.*;

class Solution {
    public int numDistinctIslands2(int[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int m = grid.length, n = grid[0].length;
        Set<String> shapes = new HashSet<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    List<int[]> cells = new ArrayList<>();
                    dfs(grid, i, j, m, n, cells);
                    shapes.add(canonical(cells));
                }
            }
        }
        return shapes.size();
    }

    private void dfs(int[][] grid, int r, int c, int m, int n, List<int[]> cells) {
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) return;
        grid[r][c] = 0;
        cells.add(new int[] {r, c});
        dfs(grid, r + 1, c, m, n, cells);
        dfs(grid, r - 1, c, m, n, cells);
        dfs(grid, r, c + 1, m, n, cells);
        dfs(grid, r, c - 1, m, n, cells);
    }

    private String canonical(List<int[]> cells) {
        int[][] transforms = {
            {1, 0, 0, 1}, {1, 0, 0, -1}, {-1, 0, 0, 1}, {-1, 0, 0, -1},
            {0, 1, 1, 0}, {0, 1, -1, 0}, {0, -1, 1, 0}, {0, -1, -1, 0}
        };
        // Actually use (ax+by, cx+dy) with pairs: (x,y),(x,-y),(-x,y),(-x,-y),(y,x),(y,-x),(-y,x),(-y,-x)
        String best = null;
        int[][] signs = {
            {1, 1, 0}, {1, -1, 0}, {-1, 1, 0}, {-1, -1, 0},
            {1, 1, 1}, {1, -1, 1}, {-1, 1, 1}, {-1, -1, 1}
        };
        for (int[] s : signs) {
            List<int[]> pts = new ArrayList<>();
            for (int[] p : cells) {
                int x = p[0], y = p[1];
                int nx, ny;
                if (s[2] == 0) { nx = s[0] * x; ny = s[1] * y; }
                else { nx = s[0] * y; ny = s[1] * x; }
                pts.add(new int[] {nx, ny});
            }
            int minX = Integer.MAX_VALUE, minY = Integer.MAX_VALUE;
            for (int[] p : pts) {
                minX = Math.min(minX, p[0]);
                minY = Math.min(minY, p[1]);
            }
            for (int[] p : pts) { p[0] -= minX; p[1] -= minY; }
            pts.sort((a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
            StringBuilder sb = new StringBuilder();
            for (int[] p : pts) {
                if (sb.length() > 0) sb.append(';');
                sb.append(p[0]).append(',').append(p[1]);
            }
            String key = sb.toString();
            if (best == null || key.compareTo(best) < 0) best = key;
        }
        return best;
    }
}
