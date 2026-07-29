// LeetCode 1074 - Number of Submatrices That Sum to Target
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution {
    fun numSubmatrixSumTarget(matrix: Array<IntArray>, target: Int): Int {
        val rows = matrix.size
        val cols = matrix[0].size
        var ans = 0
        for (left in 0 until cols) {
            val rowSum = IntArray(rows)
            for (right in left until cols) {
                for (r in 0 until rows) rowSum[r] += matrix[r][right]
                var prefix = 0
                val seen = mutableMapOf(0 to 1)
                for (value in rowSum) {
                    prefix += value
                    ans += seen.getOrDefault(prefix - target, 0)
                    seen[prefix] = seen.getOrDefault(prefix, 0) + 1
                }
            }
        }
        return ans
    }
}
