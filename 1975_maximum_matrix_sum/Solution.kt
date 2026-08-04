// LeetCode 1975
// https://leetcode.com/problems/maximum-matrix-sum/

class Solution {
    fun maxMatrixSum(matrix: Array<IntArray>): Long {
        var total = 0L
        var neg = 0
        var mn = Long.MAX_VALUE
        for (row in matrix) for (x in row) {
            if (x < 0) neg++
            val ax = kotlin.math.abs(x).toLong()
            total += ax
            mn = minOf(mn, ax)
        }
        return if (neg % 2 == 0) total else total - 2 * mn
    }
}
