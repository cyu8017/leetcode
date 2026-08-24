// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution {
    fun findMaxFish(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var best = 0
        for (i in 0 until m)
            for (j in 0 until n)
                if (grid[i][j] > 0) best = maxOf(best, dfs(grid, i, j))
        return best
    }

    private fun dfs(grid: Array<IntArray>, r: Int, c: Int): Int {
        val m = grid.size
        val n = grid[0].size
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) return 0
        val fish = grid[r][c]
        grid[r][c] = 0
        return fish + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1)
    }
}
