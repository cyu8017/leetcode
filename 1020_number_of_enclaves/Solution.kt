// LeetCode 1020 - Number of Enclaves
// https://leetcode.com/problems/number-of-enclaves/

class Solution {
    fun numEnclaves(grid: Array<IntArray>): Int {
        val m = grid.size; val n = grid[0].size
        for (i in 0 until m) {
            dfs(grid, i, 0); dfs(grid, i, n - 1)
        }
        for (j in 0 until n) {
            dfs(grid, 0, j); dfs(grid, m - 1, j)
        }
        var ans = 0
        for (row in grid) for (x in row) ans += x
        return ans
    }

    private fun dfs(grid: Array<IntArray>, r: Int, c: Int) {
        if (r < 0 || r >= grid.size || c < 0 || c >= grid[0].size || grid[r][c] != 1) return
        grid[r][c] = 0
        dfs(grid, r + 1, c); dfs(grid, r - 1, c); dfs(grid, r, c + 1); dfs(grid, r, c - 1)
    }
}
