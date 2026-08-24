// LeetCode 0980 - Unique Paths III
// https://leetcode.com/problems/unique-paths-iii/

class Solution {
    private var ans = 0
    private var m = 0
    private var n = 0
    private lateinit var grid: Array<IntArray>

    fun uniquePathsIII(grid: Array<IntArray>): Int {
        this.grid = grid
        m = grid.size
        n = grid[0].size
        var empty = 0
        var sr = 0
        var sc = 0
        ans = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] != -1) empty++
                if (grid[i][j] == 1) {
                    sr = i
                    sc = j
                }
            }
        }
        dfs(sr, sc, empty)
        return ans
    }

    private fun dfs(r: Int, c: Int, remain: Int) {
        if (grid[r][c] == 2) {
            if (remain == 1) ans++
            return
        }
        val temp = grid[r][c]
        grid[r][c] = -1
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        for (d in dirs) {
            val nr = r + d[0]
            val nc = c + d[1]
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != -1) {
                dfs(nr, nc, remain - 1)
            }
        }
        grid[r][c] = temp
    }
}
