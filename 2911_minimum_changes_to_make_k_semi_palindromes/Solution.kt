// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/


class Solution {
    private lateinit var s: String

    fun minimumChanges(s: String, k: Int): Int {
        this.s = s
        val n = s.length
        val cost = Array(n) { IntArray(n) { 1 shl 20 } }
        for (i in 0 until n) {
            for (j in i + 1 until n) cost[i][j] = semiCost(i, j)
        }
        val dp = Array(k + 1) { IntArray(n + 1) { 1 shl 20 } }
        dp[0][0] = 0
        for (p in 1..k) {
            for (i in 1..n) {
                for (t in 0 until i - 1) {
                    val cand = dp[p - 1][t] + cost[t][i - 1]
                    if (cand < dp[p][i]) dp[p][i] = cand
                }
            }
        }
        return dp[k][n]
    }

    private fun semiCost(l: Int, r: Int): Int {
        val length = r - l + 1
        var best = 1 shl 20
        for (d in 1 until length) {
            if (length % d != 0) continue
            var chg = 0
            for (start in 0 until d) {
                val chars = StringBuilder()
                var i = l + start
                while (i <= r) {
                    chars.append(s[i])
                    i += d
                }
                var a = 0
                var b = chars.length - 1
                while (a < b) {
                    if (chars[a] != chars[b]) chg++
                    a++
                    b--
                }
            }
            if (chg < best) best = chg
        }
        return best
    }
}
