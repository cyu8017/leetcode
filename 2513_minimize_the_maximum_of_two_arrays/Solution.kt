// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution {
    fun minimizeSet(divisor1: Int, divisor2: Int, uniqueCnt1: Int, uniqueCnt2: Int): Int {
        val lcm = 1L * divisor1 / gcd(divisor1, divisor2) * divisor2
        fun ok(x: Long): Boolean {
            val a = x - x / divisor1
            val b = x - x / divisor2
            val both = x - x / lcm
            return a >= uniqueCnt1 && b >= uniqueCnt2 && both >= uniqueCnt1 + uniqueCnt2
        }
        var lo = 1L
        var hi = 1L shl 62
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (ok(mid)) hi = mid else lo = mid + 1
        }
        return lo.toInt()
    }

    private fun gcd(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }
}
