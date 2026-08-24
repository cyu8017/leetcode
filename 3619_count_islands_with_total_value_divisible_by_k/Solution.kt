// LeetCode 3619 - Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

class Solution {
    private lateinit var grid: Array<IntArray>
    private var m = 0
    private var n = 0
    private val dirs = intArrayOf(-1, 0, 1, 0, -1)

    private fun dfs(i: Int, j: Int): Long {
        var s = grid[i][j].toLong()
        grid[i][j] = 0
        for (d in 0 until 4) {
            val x = i + dirs[d]
            val y = j + dirs[d + 1]
            if (x in 0 until m && y in 0 until n && grid[x][y] > 0) s += dfs(x, y)
        }
        return s
    }

    fun countIslands(grid: Array<IntArray>, k: Int): Int {
        this.grid = grid
        m = grid.size
        n = grid[0].size
        var ans = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] > 0 && dfs(i, j) % k == 0L) ans++
            }
        }
        return ans
    }
}
