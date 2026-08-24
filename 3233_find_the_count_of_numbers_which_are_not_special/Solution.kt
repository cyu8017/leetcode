// LeetCode 3233 - Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

class Solution {
    private val M: Int = 31623
    private var primes: BooleanArray? = null
    private var inited: Boolean = false

    private fun initPrimes() {
        if (inited) return
        primes = BooleanArray(M + 1)
        for (i in 0 ..M) { primes[i] = true }
        primes[0] = primes[1] = false
        for (i in 2 ..M) {
            if (primes[i]) {
                run {
                    var j = i * 2
                    while (j <= M) {
                        primes[j] = false
                        j += i
                    }
                }
            }
        }
        inited = true
    }

    fun nonSpecialCount(l: Int, r: Int): Int {
        initPrimes()
        var lo = kotlin.math.ceil(kotlin.math.sqrt(l))
        var hi = kotlin.math.floor(kotlin.math.sqrt(r))
        var cnt = 0
        for (i in lo ..hi) {
            if (primes[i]) cnt++
        }
        return r - l + 1 - cnt
    }
}
