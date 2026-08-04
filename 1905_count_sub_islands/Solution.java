// LeetCode 1905 - Count Sub Islands
// https://leetcode.com/problems/count-sub-islands/

class Solution {
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        int rows = grid2.length, cols = grid2[0].length, ans = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid2[r][c] == 1 && dfs(grid1, grid2, r, c)) ans++;
            }
        }
        return ans;
    }

    private boolean dfs(int[][] grid1, int[][] grid2, int r, int c) {
        int rows = grid2.length, cols = grid2[0].length;
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid2[r][c] == 0) return true;
        grid2[r][c] = 0;
        boolean ok = grid1[r][c] == 1;
        ok &= dfs(grid1, grid2, r + 1, c);
        ok &= dfs(grid1, grid2, r - 1, c);
        ok &= dfs(grid1, grid2, r, c + 1);
        ok &= dfs(grid1, grid2, r, c - 1);
        return ok;
    }
}
