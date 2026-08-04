// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

class Solution {
    fun numPrimeArrangements(n: Int): Int {
        val MOD = 1_000_000_007L
        var primes = 0
        for (i in 1..n) if (isPrime(i)) primes++
        return ((fact(primes, MOD) * fact(n - primes, MOD)) % MOD).toInt()
    }

    private fun isPrime(x: Int): Boolean {
        if (x < 2) return false
        var d = 2
        while (d * d <= x) {
            if (x % d == 0) return false
            d++
        }
        return true
    }

    private fun fact(n: Int, MOD: Long): Long {
        var ans = 1L
        for (i in 2..n) ans = ans * i % MOD
        return ans
    }
}
