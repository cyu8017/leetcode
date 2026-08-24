// LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

import kotlin.math.abs

class Solution {
    fun numberOfWays(startPos: Int, endPos: Int, k: Int): Int {
        val mod = 1_000_000_007
        val diff = abs(endPos - startPos)
        if (diff > k || (k - diff) % 2 != 0) return 0
        val r = (k + diff) / 2
        return comb(k, r, mod)
    }

    private fun comb(n: Int, r: Int, mod: Int): Int {
        if (r < 0 || r > n) return 0
        var num = 1L
        var den = 1L
        for (i in 0 until r) {
            num = num * (n - i) % mod
            den = den * (i + 1) % mod
        }
        return (num * modInverse(den.toInt(), mod) % mod).toInt()
    }

    private fun modInverse(a: Int, mod: Int): Int = modPow(a, mod - 2, mod)

    private fun modPow(a: Int, e0: Int, mod: Int): Int {
        var e = e0
        var res = 1L
        var base = (a % mod).toLong()
        while (e > 0) {
            if ((e and 1) != 0) res = res * base % mod
            base = base * base % mod
            e = e shr 1
        }
        return res.toInt()
    }
}
