// LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
// https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

class Solution {
    private fun modPow(a: Long, e: Long, mod: Int): Long {
        if (a < 0) a = 0
        var r = 1
        a %= mod
        while (e > 0) {
            if ((e & 1) != 0) r = r * a % mod
            a = a * a % mod
            e >>= 1
        }
        return r
    }

    private fun comb(n: Int, k: Int, mod: Int): Int {
        if (k < 0 || k > n) return 0
        var num = 1
        var den = 1
        for (i in 0 until k) {
            num = num * (n - i) % mod
            den = den * (i + 1) % mod
        }
        return (num * modPow(den, mod - 2, mod) % mod)
    }

    fun countGoodArrays(n: Int, m: Int, k: Int): Int {
        val mod = 1_000_000_007
        return (comb(n - 1, k, mod) * m % mod * modPow(m - 1, n - 1 - k, mod) % mod)
    }
}
