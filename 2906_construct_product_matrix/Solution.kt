// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/


class Solution {
    fun constructProductMatrix(grid: Array<IntArray>): Array<IntArray> {
        val mod = 12345
        val m = grid.size
        val n = grid[0].size
        val ans = Array(m) { IntArray(n) }
        var pref = 1
        for (i in 0 until m) {
            for (j in 0 until n) {
                ans[i][j] = pref
                pref = (1L * pref * (grid[i][j] % mod) % mod).toInt()
            }
        }
        var suf = 1
        for (i in m - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                ans[i][j] = (1L * ans[i][j] * suf % mod).toInt()
                suf = (1L * suf * (grid[i][j] % mod) % mod).toInt()
            }
        }
        return ans
    }
}
