// LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

class Solution {
    fun maxEqualRowsAfterFlips(matrix: Array<IntArray>): Int {
        val patterns = mutableMapOf<String, Int>()
        var best = 0
        for (row in matrix) {
            val base = row[0]
            val key = buildString {
                for (x in row) append(x xor base)
            }
            val count = patterns.merge(key, 1) { a, b -> a + b }!!
            best = maxOf(best, count)
        }
        return best
    }
}
