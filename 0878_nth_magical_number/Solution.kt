// LeetCode 0878 - Nth Magical Number
// https://leetcode.com/problems/nth-magical-number/

class Solution {
    fun nthMagicalNumber(n: Int, a: Int, b: Int): Int {
        val MOD = 1_000_000_007
        var lcm = a / gcd(a, b) * b
        var lo = 1, hi = n * minOf(a, b)
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (mid / a + mid / b - mid / lcm >= n) hi = mid
            else lo = mid + 1
        }
        return (lo % MOD)
    }

    private fun gcd(x: Long, y: Long): Long {
        var x = x
        var y = y
        while (y != 0) {
            var t = x % y
            x = y
            y = t
        }
        return x
    }
}
