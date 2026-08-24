// LeetCode 0651 - 4 Keys Keyboard
// https://leetcode.com/problems/4-keys-keyboard/


class Solution {
    fun maxA(n: Int): Int {
        val dp = IntArray(n + 1)
        for (i in 1..n) {
            dp[i] = dp[i - 1] + 1
            for (j in 2 until i) {
                dp[i] = maxOf(dp[i], dp[j - 2] * (i - j + 1))
            }
        }
        return dp[n]
    }
}
