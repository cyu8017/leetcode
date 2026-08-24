// LeetCode 0065 - Valid Number
// https://leetcode.com/problems/valid-number/

class Solution {
    fun isNumber(s: String): Boolean {
        var seenDigit = false
        var seenDot = false
        var seenExp = false

        for (i in s.indices) {
            when (val ch = s[i]) {
                in '0'..'9' -> seenDigit = true
                '+', '-' -> {
                    if (i > 0 && s[i - 1] != 'e' && s[i - 1] != 'E') {
                        return false
                    }
                }
                'e', 'E' -> {
                    if (seenExp || !seenDigit) {
                        return false
                    }
                    seenExp = true
                    seenDigit = false
                    seenDot = false
                }
                '.' -> {
                    if (seenDot || seenExp) {
                        return false
                    }
                    seenDot = true
                }
                else -> return false
            }
        }

        return seenDigit
    }
}
