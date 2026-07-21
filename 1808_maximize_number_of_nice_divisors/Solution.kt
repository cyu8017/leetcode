// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

class Solution {
    fun maxNiceDivisors(primeFactors: Int): Int {
        val mod = 1_000_000_007L
        if (primeFactors <= 3) return primeFactors
        return when (primeFactors % 3) {
            0 -> modPow(3, primeFactors / 3, mod).toInt()
            1 -> ((modPow(3, primeFactors / 3 - 1, mod) * 4) % mod).toInt()
            else -> ((modPow(3, primeFactors / 3, mod) * 2) % mod).toInt()
        }
    }

    private fun modPow(base: Long, exp: Int, mod: Long): Long {
        var b = base % mod
        var e = exp
        var result = 1L
        while (e > 0) {
            if (e and 1 == 1) result = result * b % mod
            b = b * b % mod
            e = e shr 1
        }
        return result
    }
}
