// LeetCode 1735 - Count Ways to Make Array With Product
// https://leetcode.com/problems/count-ways-to-make-array-with-product/

class Solution {
    private val mod = 1_000_000_007L

    fun waysToFillArray(queries: Array<IntArray>): IntArray {
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val n = queries[i][0].toLong()
            var value = queries[i][1].toLong()
            var ways = 1L
            var d = 2L
            while (d * d <= value) {
                if (value % d == 0L) {
                    var exp = 0L
                    while (value % d == 0L) {
                        value /= d
                        exp++
                    }
                    ways = ways * combMod(n + exp - 1, exp) % mod
                }
                d += if (d == 2L) 1 else 2
            }
            if (value > 1) {
                ways = ways * (n % mod) % mod
            }
            ans[i] = ways.toInt()
        }
        return ans
    }

    private fun combMod(a: Long, b: Long): Long {
        var num = 1L
        var den = 1L
        for (i in 1..b) {
            num = num * ((a - b + i) % mod) % mod
            den = den * (i % mod) % mod
        }
        return num * powMod(den, mod - 2) % mod
    }

    private fun powMod(base: Long, exp: Long): Long {
        var result = 1L
        var b = base % mod
        var e = exp
        while (e > 0) {
            if (e and 1L == 1L) {
                result = result * b % mod
            }
            b = b * b % mod
            e = e shr 1
        }
        return result
    }
}
