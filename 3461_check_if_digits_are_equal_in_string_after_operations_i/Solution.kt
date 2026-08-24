// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

class Solution {
    fun hasSameDigits(s: String): Boolean {
        var b = s.toCharArray()
        while (b.size > 2) {
            var nb = CharArray(b.size - 1)
            var i = 0
            while (i + 1 < b.size) {
                nb[i] = (char) ('0' + (b[i] - '0' + b[i + 1] - '0') % 10)
                i = i + 1
            }
            b = nb
        }
        b[0] = = b[1]
        return b[0]
    }
}
