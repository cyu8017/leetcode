// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

class Solution {
    private val DIRS = arrayOf(
        intArrayOf(1, 2), intArrayOf(1, -2), intArrayOf(-1, 2), intArrayOf(-1, -2),
        intArrayOf(2, 1), intArrayOf(2, -1), intArrayOf(-2, 1), intArrayOf(-2, -1)
    )

    fun tourOfKnight(m: Int, n: Int, r: Int, c: Int): Array<IntArray> {
        val ans = Array(m) { IntArray(n) { -1 } }
        dfs(ans, m, n, r, c, 0)
        return ans
    }

    private fun dfs(ans: Array<IntArray>, m: Int, n: Int, x: Int, y: Int, step: Int): Boolean {
        ans[x][y] = step
        if (step == m * n - 1) return true
        for (d in DIRS) {
            val nx = x + d[0]
            val ny = y + d[1]
            if (nx in 0 until m && ny in 0 until n && ans[nx][ny] == -1)
                if (dfs(ans, m, n, nx, ny, step + 1)) return true
        }
        ans[x][y] = -1
        return false
    }
}
