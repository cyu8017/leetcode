// LeetCode 0091 - Decode Ways
// https://leetcode.com/problems/decode-ways/

class Solution {
    fun numDecodings(s: String): Int {
        if (s.isEmpty() || s[0] == '0') {
            return 0
        }

        var prev2 = 1
        var prev1 = 1

        for (i in 1 until s.length) {
            var current = 0
            if (s[i] != '0') {
                current += prev1
            }
            val two = s.substring(i - 1, i + 1).toInt()
            if (two in 10..26) {
                current += prev2
            }
            prev2 = prev1
            prev1 = current
        }

        return prev1
    }
}
