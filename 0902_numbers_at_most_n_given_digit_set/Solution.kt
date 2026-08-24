// LeetCode 0902 - Numbers At Most N Given Digit Set
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

class Solution {
    private lateinit var digits: Array<String>
    private var k = 0

    fun atMostNGivenDigitSet(digits: Array<String>, n: Int): Int {
        this.digits = digits
        this.k = digits.size
        val s = n.toString()
        val m = s.length
        var ans = 0
        for (i in 1 until m) ans += ipow(k, i)
        ans += countUpTo(s)
        return ans
    }

    private fun ipow(bas: Int, exp: Int): Int {
        var exp = exp
        var r = 1
        while (exp-- > 0) r *= bas
        return r
    }

    private fun countUpTo(t: String): Int {
        if (t.isEmpty()) return 0
        var first = 0
        for (d in digits) if (d[0] < t[0]) first++
        var ways = first * ipow(k, t.length - 1)
        var found = false
        for (d in digits) {
            if (d[0] == t[0]) { found = true; break }
        }
        if (found) ways += countUpTo(t.substring(1))
        return ways
    }
}
