// LeetCode 3770 - Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest_prime_from_consecutive_prime_sum/

class Solution {
    companion object {
        private const val MX = 500000
        private val S = ArrayList<Int>()

        init {
            val isPrime = BooleanArray(MX + 1) { true }
            isPrime[0] = false
            isPrime[1] = false
            val primes = ArrayList<Int>()
            for (i in 2..MX) {
                if (isPrime[i]) {
                    primes.add(i)
                    if (i.toLong() * i <= MX) {
                        var j = i * i
                        while (j <= MX) {
                            isPrime[j] = false
                            j += i
                        }
                    }
                }
            }
            S.add(0)
            var t = 0
            for (x in primes) {
                t += x
                if (t > MX) break
                if (isPrime[t]) S.add(t)
            }
        }
    }

    fun largestPrime(n: Int): Int {
        var lo = 0
        var hi = S.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (S[mid] <= n) lo = mid + 1 else hi = mid
        }
        return S[lo - 1]
    }
}
