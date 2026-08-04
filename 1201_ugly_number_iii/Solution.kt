// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

class Solution {
    fun nthUglyNumber(n: Int, a: Int, b: Int, c: Int): Int {
        val ab = lcm(a.toLong(), b.toLong())
        val ac = lcm(a.toLong(), c.toLong())
        val bc = lcm(b.toLong(), c.toLong())
        val abc = lcm(ab, c.toLong())
        var lo = 1L
        var hi = 2_000_000_000L
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (count(mid, a.toLong(), b.toLong(), c.toLong(), ab, ac, bc, abc) >= n) hi = mid
            else lo = mid + 1
        }
        return lo.toInt()
    }

    private fun count(x: Long, a: Long, b: Long, c: Long, ab: Long, ac: Long, bc: Long, abc: Long): Long {
        return x / a + x / b + x / c - x / ab - x / ac - x / bc + x / abc
    }

    private fun gcd(x: Long, y: Long): Long = if (y == 0L) x else gcd(y, x % y)
    private fun lcm(x: Long, y: Long): Long = x / gcd(x, y) * y
}
