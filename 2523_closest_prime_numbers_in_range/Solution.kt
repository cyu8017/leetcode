// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution {
    fun closestPrimes(left: Int, right: Int): IntArray {
        val isPrime = BooleanArray(right + 1) { true }
        if (right >= 0) isPrime[0] = false
        if (right >= 1) isPrime[1] = false
        var i = 2
        while (i * i <= right) {
            if (isPrime[i]) {
                var j = i * i
                while (j <= right) {
                    isPrime[j] = false
                    j += i
                }
            }
            i += 1
        }
        val primes = ArrayList<Int>()
        for (x in left..right) if (isPrime[x]) primes.add(x)
        if (primes.size < 2) return intArrayOf(-1, -1)
        var bestDiff = Int.MAX_VALUE
        var best = intArrayOf(-1, -1)
        for (j in 0 until primes.size - 1) {
            val d = primes[j + 1] - primes[j]
            if (d < bestDiff) {
                bestDiff = d
                best = intArrayOf(primes[j], primes[j + 1])
            }
        }
        return best
    }
}
