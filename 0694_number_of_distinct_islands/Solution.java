// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

import java.util.*;

class Solution {
    private void dfs(int[][] grid, int r, int c, int br, int bc, List<String> path) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] == 0) return;
        grid[r][c] = 0;
        path.add((r - br) + "," + (c - bc));
        dfs(grid, r + 1, c, br, bc, path);
        dfs(grid, r - 1, c, br, bc, path);
        dfs(grid, r, c + 1, br, bc, path);
        dfs(grid, r, c - 1, br, bc, path);
    }

    public int numDistinctIslands(int[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        Set<String> shapes = new HashSet<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    List<String> path = new ArrayList<>();
                    dfs(grid, i, j, i, j, path);
                    shapes.add(String.join(";", path));
                }
            }
        }
        return shapes.size();
    }
}
