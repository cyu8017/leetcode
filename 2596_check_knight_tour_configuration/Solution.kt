// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/

class Solution {
    fun checkValidGrid(grid: Array<IntArray>): Boolean {
        val n = grid.size
        if (grid[0][0] != 0) return false
        val pos = Array(n * n) { IntArray(2) }
        for (i in 0 until n) {
            for (j in 0 until n) {
                pos[grid[i][j]] = intArrayOf(i, j)
            }
        }
        val dirs = arrayOf(
            intArrayOf(1, 2), intArrayOf(1, -2), intArrayOf(-1, 2), intArrayOf(-1, -2),
            intArrayOf(2, 1), intArrayOf(2, -1), intArrayOf(-2, 1), intArrayOf(-2, -1)
        )
        for (v in 0 until n * n - 1) {
            val r = pos[v][0]
            val c = pos[v][1]
            var ok = false
            for (d in dirs) {
                if (r + d[0] == pos[v + 1][0] && c + d[1] == pos[v + 1][1]) {
                    ok = true
                    break
                }
            }
            if (!ok) return false
        }
        return true
    }
}
