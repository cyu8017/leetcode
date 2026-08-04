// LeetCode 1253 - Reconstruct a 2 Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

class Solution {
    fun reconstructMatrix(upper: Int, lower: Int, colsum: IntArray): List<List<Int>> {
        var u = upper
        var l = lower
        val n = colsum.size
        val top = IntArray(n)
        val bottom = IntArray(n)
        for (i in 0 until n) {
            if (colsum[i] == 2) {
                top[i] = 1
                bottom[i] = 1
                u--
                l--
            }
        }
        if (u < 0 || l < 0) return emptyList()
        for (i in 0 until n) {
            if (colsum[i] == 1) {
                when {
                    u > 0 -> { top[i] = 1; u-- }
                    l > 0 -> { bottom[i] = 1; l-- }
                    else -> return emptyList()
                }
            }
        }
        if (u != 0 || l != 0) return emptyList()
        return listOf(top.toList(), bottom.toList())
    }
}
