// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

class Solution {
    private fun dfs(grid: Array<IntArray>, r: Int, c: Int): Int {
        if (r < 0 || r >= grid.size || c < 0 || c >= grid[0].size || grid[r][c] == 0) return 0
        grid[r][c] = 0
        return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1)
    }

    fun maxAreaOfIsland(grid: Array<IntArray>): Int {
        var best = 0
        for (i in grid.indices) {
            for (j in grid[0].indices) {
                best = maxOf(best, dfs(grid, i, j))
            }
        }
        return best
    }
}
