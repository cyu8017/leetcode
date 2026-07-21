// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

class Solution {
    fun minSwaps(s: String): Int {
        val zeros = s.count { it == '0' }
        val ones = s.length - zeros
        if (kotlin.math.abs(zeros - ones) > 1) return -1
        fun mismatches(start: Char): Int {
            var count = 0
            var expect = start
            for (ch in s) {
                if (ch != expect) count++
                expect = if (expect == '0') '1' else '0'
            }
            return count / 2
        }
        return when {
            zeros == ones -> minOf(mismatches('0'), mismatches('1'))
            zeros > ones -> mismatches('0')
            else -> mismatches('1')
        }
    }
}
