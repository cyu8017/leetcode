public class Solution {
    public int NumIslands(char[][] grid) {
        if (grid == null || grid.Length == 0) return 0;
        var count = 0;
        for (var row = 0; row < grid.Length; row++) {
            for (var col = 0; col < grid[0].Length; col++) {
                if (grid[row][col] == '1') {
                    count++;
                    Dfs(grid, row, col);
                }
            }
        }
        return count;
    }

    private void Dfs(char[][] grid, int row, int col) {
        if (row < 0 || row >= grid.Length || col < 0 || col >= grid[0].Length || grid[row][col] != '1') return;
        grid[row][col] = '0';
        Dfs(grid, row + 1, col);
        Dfs(grid, row - 1, col);
        Dfs(grid, row, col + 1);
        Dfs(grid, row, col - 1);
    }
}
