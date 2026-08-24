// LeetCode 0013 - Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

class Solution {
    fun romanToInt(s: String): Int {
        val values = mapOf(
            'I' to 1, 'V' to 5, 'X' to 10, 'L' to 50,
            'C' to 100, 'D' to 500, 'M' to 1000,
        )
        var total = 0
        var prev = 0

        for (i in s.length - 1 downTo 0) {
            val curr = values[s[i]] ?: 0
            if (curr < prev) {
                total -= curr
            } else {
                total += curr
            }
            prev = curr
        }

        return total
    }
}
