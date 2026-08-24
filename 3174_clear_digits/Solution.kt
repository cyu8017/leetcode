// LeetCode 3174 - Clear Digits
// https://leetcode.com/problems/clear-digits/

class Solution {
    fun clearDigits(s: String): String {
        var stk = StringBuilder()
        for (i in 0 until s.length) {
            var c = s[i]
            if (c >= '0' && c <= '9') {
                stk.deleteCharAt(stk.length - 1)
            } else {
                stk.append(c)
            }
        }
        return stk.toString()
    }
}
