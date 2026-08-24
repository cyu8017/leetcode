// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

class Solution {
    private val MOD = 1_000_000_007

    fun numberOfWays(s: String, t: String, k: Long): Int {
        val n = s.length
        val ss = s + s
        if (ss.substring(0, 2 * n - 1).indexOf(t) < 0) return 0
        var cnt = 0
        for (i in 0 until n) if (ss.substring(i, i + n) == t) cnt++
        val same = s == t
        val pk = modPow((n - 1).toLong(), k)
        val invn = modPow(n.toLong(), (MOD - 2).toLong())
        val sign = if (k % 2 == 1L) MOD - 1 else 1
        val waysSame = ((1L * pk + 1L * ((n - 1) % MOD) * sign % MOD) % MOD * invn % MOD).toInt()
        val waysDiff = ((1L * pk - sign + MOD) % MOD * invn % MOD).toInt()
        if (same) return waysSame
        return (1L * waysDiff * cnt % MOD).toInt()
    }

    private fun modPow(a0: Long, b0: Long): Int {
        var a = a0 % MOD
        var b = b0
        var res = 1L
        while (b > 0) {
            if ((b and 1L) != 0L) res = res * a % MOD
            a = a * a % MOD
            b = b shr 1
        }
        return res.toInt()
    }
}
