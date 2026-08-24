// LeetCode 0474 - Ones and Zeroes
// https://leetcode.com/problems/ones-and-zeroes/

class Solution {
    fun findMaxForm(strs: Array<String>, m: Int, n: Int): Int {
        val dp = Array(m + 1) { IntArray(n + 1) }
        for (string in strs) {
            val zeros = string.count { it == '0' }
            val ones = string.length - zeros
            for (zero in m downTo zeros) {
                for (one in n downTo ones) {
                    dp[zero][one] = maxOf(dp[zero][one], dp[zero - zeros][one - ones] + 1)
                }
            }
        }
        return dp[m][n]
    }
}
