// LeetCode 1388 - Pizza With 3n Slices
// https://leetcode.com/problems/pizza-with-3n-slices/

class Solution {
    fun maxSizeSlices(slices: IntArray): Int {
        val k = slices.size / 3
        fun line(a: IntArray): Int {
            val dp = Array(a.size + 2) { IntArray(k + 1) }
            for (i in a.indices) {
                val x = a[i]
                val ii = i + 2
                for (j in 1..k) {
                    dp[ii][j] = maxOf(dp[ii - 1][j], dp[ii - 2][j - 1] + x)
                }
            }
            return dp[a.size + 1][k]
        }
        return maxOf(line(slices.copyOfRange(0, slices.size - 1)), line(slices.copyOfRange(1, slices.size)))
    }
}
