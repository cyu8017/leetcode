class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        if (grid.isEmpty()) return 0
        fun dfs(row: Int, col: Int) {
            if (row !in grid.indices || col !in grid[0].indices || grid[row][col] != '1') return
            grid[row][col] = '0'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        }
        var count = 0
        for (row in grid.indices) {
            for (col in grid[0].indices) {
                if (grid[row][col] == '1') {
                    count++
                    dfs(row, col)
                }
            }
        }
        return count
    }
}
