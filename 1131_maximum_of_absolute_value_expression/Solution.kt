// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

class Solution {
    fun maxAbsValExpr(arr1: IntArray, arr2: IntArray): Int {
        val n = arr1.size
        var ans = 0
        for ((p, q) in listOf(1 to 1, 1 to -1, -1 to 1, -1 to -1)) {
            var best = p * arr1[0] + q * arr2[0]
            for (i in 1 until n) {
                val cur = p * arr1[i] + q * arr2[i] + i
                ans = maxOf(ans, cur - best)
                best = minOf(best, p * arr1[i] + q * arr2[i] + i)
            }
        }
        return ans
    }
}
