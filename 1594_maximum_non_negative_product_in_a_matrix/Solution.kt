// LeetCode 1594 - Maximum Non Negative Product in a Matrix
// https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

class Solution {
    fun maxProductPath(grid: Array<IntArray>): Int {
        val mod = 1_000_000_007
        val m = grid.size
        val n = grid[0].size
        val high = Array(m) { LongArray(n) }
        val low = Array(m) { LongArray(n) }
        high[0][0] = grid[0][0].toLong()
        low[0][0] = grid[0][0].toLong()
        for (r in 0 until m) {
            for (c in 0 until n) {
                if (r == 0 && c == 0) continue
                val g = grid[r][c].toLong()
                var mx = Long.MIN_VALUE
                var mn = Long.MAX_VALUE
                if (r > 0) {
                    mx = maxOf(mx, high[r - 1][c] * g, low[r - 1][c] * g)
                    mn = minOf(mn, high[r - 1][c] * g, low[r - 1][c] * g)
                }
                if (c > 0) {
                    mx = maxOf(mx, high[r][c - 1] * g, low[r][c - 1] * g)
                    mn = minOf(mn, high[r][c - 1] * g, low[r][c - 1] * g)
                }
                high[r][c] = mx
                low[r][c] = mn
            }
        }
        if (high[m - 1][n - 1] < 0) return -1
        return (high[m - 1][n - 1] % mod).toInt()
    }
}
