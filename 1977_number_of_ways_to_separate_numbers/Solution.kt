// LeetCode 1977
// https://leetcode.com/problems/number-of-ways-to-separate-numbers/

class Solution {
    fun numberOfCombinations(num: String): Int {
        val mod = 1_000_000_007
        val n = num.length
        if (num[0] == '0') return 0
        val lcp = Array(n + 1) { IntArray(n + 1) }
        for (i in n - 1 downTo 0) for (j in n - 1 downTo 0) {
            if (num[i] == num[j]) lcp[i][j] = lcp[i + 1][j + 1] + 1
        }
        fun le(a: Int, b: Int, length: Int): Boolean {
            val common = lcp[a][b]
            if (common >= length) return true
            return num[a + common] < num[b + common]
        }
        val dp = Array(n + 1) { IntArray(n + 1) }
        val pref = Array(n + 1) { IntArray(n + 1) }
        for (i in 1..n) {
            for (l in 1..i) {
                val start = i - l
                if (num[start] == '0') {
                    dp[i][l] = 0
                } else if (start == 0) {
                    dp[i][l] = 1
                } else {
                    var ways = if (l > 1) pref[start][minOf(l - 1, start)] else 0
                    if (start >= l && le(start - l, start, l)) {
                        ways = (ways + dp[start][l]) % mod
                    }
                    dp[i][l] = ways
                }
            }
            for (l in 1..n) {
                pref[i][l] = (pref[i][l - 1] + if (l <= i) dp[i][l] else 0) % mod
            }
        }
        return pref[n][n]
    }
}
