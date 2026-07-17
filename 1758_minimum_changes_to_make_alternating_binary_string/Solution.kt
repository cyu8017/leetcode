// LeetCode 1758 - Minimum Changes To Make Alternating Binary String
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution {
    fun minOperations(s: String): Int {
        var alt1 = 0
        for (i in s.indices) {
            val expected = if (i and 1 == 0) '0' else '1'
            if (s[i] != expected) {
                alt1++
            }
        }
        return minOf(alt1, s.length - alt1)
    }
}
