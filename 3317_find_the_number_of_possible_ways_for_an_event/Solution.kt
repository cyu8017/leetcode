// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

class Solution {
    private fun modPow(a0: Long, e0: Long, mod: Int): Int {
        var a = a0 % mod
        var e = e0
        var r = 1L
        while (e > 0) {
            if ((e and 1L) != 0L) r = r * a % mod
            a = a * a % mod
            e = e shr 1
        }
        return r.toInt()
    }

    fun numberOfWays(n: Int, x: Int, y: Int): Int {
        val mod = 1_000_000_007
        val dp = Array(n + 1) { IntArray(x + 1) }
        dp[0][0] = 1
        for (i in 1..n) {
            for (j in 1..x) {
                if (j > i) break
                dp[i][j] = (dp[i - 1][j - 1] + (j.toLong() * dp[i - 1][j] % mod).toInt()) % mod
            }
        }
        val fact = IntArray(x + 1)
        fact[0] = 1
        for (i in 1..x) fact[i] = (fact[i - 1].toLong() * i % mod).toInt()
        var ans = 0
        var ypow = 1
        for (k in 1..x) {
            if (k > n) break
            ypow = (ypow.toLong() * y % mod).toInt()
            val perm = (fact[x].toLong() * modPow(fact[x - k].toLong(), (mod - 2).toLong(), mod) % mod).toInt()
            ans = (ans + (dp[n][k].toLong() * perm % mod * ypow % mod).toInt()) % mod
        }
        return ans
    }
}
