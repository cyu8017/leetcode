// LeetCode 3918 - Sum Of Primes Between Number And Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

class Solution {
    companion object {
        private var ready = false
        private lateinit var isPrime: BooleanArray

        private fun initPrimes() {
            if (ready) return
            isPrime = BooleanArray(1001) { true }
            isPrime[0] = false
            isPrime[1] = false
            var i = 2
            while (i * i <= 1000) {
                if (isPrime[i]) {
                    var j = i * i
                    while (j <= 1000) {
                        isPrime[j] = false
                        j += i
                    }
                }
                i++
            }
            ready = true
        }
    }

    fun sumOfPrimesInRange(n: Int): Int {
        initPrimes()
        var r = 0
        var x = n
        while (x > 0) {
            r = r * 10 + x % 10
            x /= 10
        }
        val low = minOf(n, r)
        val high = maxOf(n, r)
        var ans = 0
        for (v in low..high) {
            if (isPrime[v]) ans += v
        }
        return ans
    }
}
