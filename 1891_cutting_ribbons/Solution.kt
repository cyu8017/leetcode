// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

class Solution {
    fun maxLength(ribbons: IntArray, k: Int): Int {
        fun can(length: Int): Boolean {
            var count = 0L
            for (ribbon in ribbons) {
                count += ribbon / length
                if (count >= k) return true
            }
            return count >= k
        }
        var lo = 1
        var hi = ribbons.maxOrNull()!!
        while (lo < hi) {
            val mid = (lo + hi + 1) ushr 1
            if (can(mid)) lo = mid else hi = mid - 1
        }
        return if (can(lo)) lo else 0
    }
}
