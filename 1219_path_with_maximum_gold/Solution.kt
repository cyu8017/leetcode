// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

class Solution {
    fun getMaximumGold(grid: Array<IntArray>): Int {
        var ans = 0
        for (r in grid.indices) {
            for (c in grid[0].indices) {
                if (grid[r][c] != 0) ans = maxOf(ans, dfs(grid, r, c))
            }
        }
        return ans
    }

    private fun dfs(grid: Array<IntArray>, r: Int, c: Int): Int {
        val gold = grid[r][c]
        grid[r][c] = 0
        var best = 0
        for ((dr, dc) in arrayOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)) {
            val nr = r + dr
            val nc = c + dc
            if (nr in grid.indices && nc in grid[0].indices && grid[nr][nc] != 0) {
                best = maxOf(best, dfs(grid, nr, nc))
            }
        }
        grid[r][c] = gold
        return gold + best
    }
}
