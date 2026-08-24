// LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution {
    fun smallestValue(n: Int): Int {
        var cur = n
        while (true) {
            val s = sumPrimeFactors(cur)
            if (s == cur) return cur
            cur = s
        }
    }

    private fun sumPrimeFactors(x0: Int): Int {
        var x = x0
        var s = 0
        var i = 2
        while (i * i <= x) {
            while (x % i == 0) {
                s += i
                x /= i
            }
            i++
        }
        if (x > 1) s += x
        return s
    }
}
