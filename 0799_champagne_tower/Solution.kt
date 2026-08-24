// LeetCode 0799 - Champagne Tower
// https://leetcode.com/problems/champagne-tower/

class Solution {
    fun champagneTower(poured: Int, query_row: Int, query_glass: Int): Double {
        var row = doubleArrayOf(poured.toDouble())
        for (r in 0 until query_row) {
            val nextRow = DoubleArray(r + 2)
            for (i in row.indices) {
                val overflow = (row[i] - 1.0) / 2.0
                if (overflow > 0) {
                    nextRow[i] += overflow
                    nextRow[i + 1] += overflow
                }
            }
            row = nextRow
        }
        return minOf(1.0, row[query_glass])
    }
}
