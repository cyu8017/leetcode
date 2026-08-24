// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

class Solution {
    private fun isPrime(c: Char): Boolean =
        c == '2' || c == '3' || c == '5' || c == '7'

    fun beautifulPartitions(s: String, k: Int, minLength: Int): Int {
        val mod = 1_000_000_007
        val n = s.length
        if (!isPrime(s[0]) || isPrime(s[n - 1])) return 0
        val dp = Array(k + 1) { IntArray(n + 1) }
        dp[0][0] = 1
        for (p in 1..k) {
            var pref = 0
            var j = 0
            for (i in 1..n) {
                while (j <= i - minLength) {
                    if (j == 0 || (isPrime(s[j]) && !isPrime(s[j - 1]))) {
                        pref = (pref + dp[p - 1][j]) % mod
                    }
                    j++
                }
                if (!isPrime(s[i - 1])) dp[p][i] = pref
            }
        }
        return dp[k][n]
    }
}
