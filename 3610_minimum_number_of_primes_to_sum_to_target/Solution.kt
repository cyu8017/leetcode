// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

class Solution {
    companion object {
        val primes = ArrayList<Int>()
        fun ensurePrimes() {
            if (primes.isNotEmpty()) return
            var x = 2
            while (primes.size < 1000) {
                var isPrime = true
                for (p in primes) {
                    if (p * p > x) break
                    if (x % p == 0) { isPrime = false; break }
                }
                if (isPrime) primes.add(x)
                x++
            }
        }
    }

    fun minNumberOfPrimes(n: Int, m: Int): Int {
        ensurePrimes()
        val Inf = Int.MAX_VALUE / 2
        val f = IntArray(n + 1) { Inf }
        f[0] = 0
        for (pi in 0 until m) {
            val x = primes[pi]
            for (i in x..n) {
                if (f[i - x] + 1 < f[i]) f[i] = f[i - x] + 1
            }
        }
        return if (f[n] < Inf) f[n] else -1
    }
}
