// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

class Solution {
    private fun modPow(a: Long, e: Long, mod: Int): Long {
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

    fun distanceSum(m: Int, n: Int, k: Int): Int {
        val mod = 1_000_000_007
        if (k < 2) return 0
        var totalCells = m * n
        var pairChoose = comb(totalCells - 2, k - 2, mod)
        var sumDist = 0
        for (d in 1 until m) { sumDist += d * (m - d) * n * n }
        for (d in 1 until n) { sumDist += d * (n - d) * m * m }
        return (sumDist % mod * pairChoose % mod)
    }
}
