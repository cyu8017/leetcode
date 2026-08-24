// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

class Solution {
    fun closedIsland(grid: Array<IntArray>): Int {
        var answer = 0
        for (r in grid.indices) {
            for (c in grid[0].indices) {
                if (grid[r][c] == 0 && flood(grid, r, c)) answer++
            }
        }
        return answer
    }

    private fun flood(grid: Array<IntArray>, sr: Int, sc: Int): Boolean {
        val m = grid.size
        val n = grid[0].size
        var closed = true
        val stackR = IntArray(m * n)
        val stackC = IntArray(m * n)
        var top = 0
        stackR[0] = sr
        stackC[0] = sc
        grid[sr][sc] = 1
        while (top >= 0) {
            val r = stackR[top]
            val c = stackC[top]
            top--
            if (r == 0 || r == m - 1 || c == 0 || c == n - 1) closed = false
            for ((dr, dc) in arrayOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)) {
                val nr = r + dr
                val nc = c + dc
                if (nr in 0 until m && nc in 0 until n && grid[nr][nc] == 0) {
                    grid[nr][nc] = 1
                    top++
                    stackR[top] = nr
                    stackC[top] = nc
                }
            }
        }
        return closed
    }
}
