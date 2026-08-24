// LeetCode 2556 - Disconnect Path in a Binary Matrix by at Most One Flip
// https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

class Solution {
    private var grid: Array<IntArray>? = null
    private var m: Int = 0
    private var n: Int = 0

    fun isPossibleToCutPath(grid: Array<IntArray>): Boolean {
        this.grid = grid
        m = grid.size
        n = grid[0].size
        if (!dfs(0, 0)) return true
        grid[0][0] = 1
        return !dfs(0, 0)
    }

    private fun dfs(r: Int, c: Int): Boolean {
        if (r == m - 1 && c == n - 1) return true
        if (r >= m || c >= n || grid[r][c] == 0) return false
        if (!(r == 0 && c == 0)) grid[r][c] = 0
        return dfs(r + 1, c) || dfs(r, c + 1)
    }
}
