// LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

class Solution {
    fun numberOfSets(n: Int, k: Int): Int {
        val MOD = 1_000_000_007L
        fun comb(nn: Int, rr: Int): Long {
            if (rr < 0 || rr > nn) return 0L
            var num = 1L
            var den = 1L
            val r = minOf(rr, nn - rr)
            for (i in 0 until r) {
                num = num * (nn - i) % MOD
                den = den * (i + 1) % MOD
            }
            return num * modInverse(den, MOD) % MOD
        }
        return comb(n + k - 1, 2 * k).toInt()
    }

    private fun modInverse(a: Long, mod: Long): Long {
        var x = a % mod
        var y = mod - 2
        var res = 1L
        while (y > 0) {
            if (y and 1L == 1L) res = res * x % mod
            x = x * x % mod
            y = y shr 1
        }
        return res
    }
}
