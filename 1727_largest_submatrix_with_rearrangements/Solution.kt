// LeetCode 1727 - Largest Submatrix With Rearrangements
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/

class Solution {
    fun largestSubmatrix(matrix: Array<IntArray>): Int {
        val m = matrix.size
        val n = matrix[0].size
        val heights = IntArray(n)
        var best = 0
        for (r in 0 until m) {
            for (c in 0 until n) {
                heights[c] = if (matrix[r][c] == 1) heights[c] + 1 else 0
            }
            val sorted = heights.clone()
            sorted.sort()
            for (width in 1..n) {
                best = maxOf(best, width * sorted[n - width])
            }
        }
        return best
    }
}
