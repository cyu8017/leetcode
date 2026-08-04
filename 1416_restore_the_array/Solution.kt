// LeetCode 1416 - Restore The Array
// https://leetcode.com/problems/restore-the-array/

class Solution {
    fun numberOfArrays(s: String, k: Int): Int {
        val mod = 1_000_000_007
        val n = s.length
        val dp = IntArray(n + 1)
        dp[n] = 1
        for (i in n - 1 downTo 0) {
            if (s[i] == '0') continue
            var value = 0L
            for (j in i until n) {
                value = value * 10 + (s[j] - '0')
                if (value > k) break
                dp[i] = (dp[i] + dp[j + 1]) % mod
            }
        }
        return dp[0]
    }
}
