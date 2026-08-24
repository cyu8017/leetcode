// LeetCode 3888 - Minimum Operations To Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

class Solution {
    private lateinit var grid: Array<IntArray>
    private var k = 0
    private var m = 0
    private var n = 0

    fun minOperations(grid: Array<IntArray>, k: Int): Long {
        this.grid = grid
        this.k = k
        m = grid.size
        n = grid[0].size
        var maxVal = grid[0][0]
        for (row in grid) for (x in row) maxVal = maxOf(maxVal, x)
        for (t in maxVal..maxVal + 1) {
            val res = check(t)
            if (res != -1L) return res
        }
        return -1
    }

    private fun check(target: Int): Long {
        val diff = Array(m + 2) { LongArray(n + 2) }
        var totalOps = 0L
        for (i in 1..m) {
            for (j in 1..n) {
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                val curVal = grid[i - 1][j - 1].toLong() + diff[i][j]
                if (curVal > target) return -1
                if (curVal < target) {
                    if (i + k - 1 > m || j + k - 1 > n) return -1
                    val needed = target - curVal
                    totalOps += needed
                    diff[i][j] += needed
                    diff[i + k][j] -= needed
                    diff[i][j + k] -= needed
                    diff[i + k][j + k] += needed
                }
            }
        }
        return totalOps
    }
}
