// LeetCode 2116 - Check if a Parentheses String Can Be Valid
// https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

class Solution {
    fun canBeValid(s: String, locked: String): Boolean {
        var n: Int = s.length
        if (n % 2 != 0) return false
        var bal: Int = 0
        for (i in 0 until n) {
            if (locked[i] == '0' || s[i] == '(') bal++
            else bal--
            if (bal < 0) return false
        }
        bal = 0
        for (i in n - 1 downTo 0) {
            if (locked[i] == '0' || s[i] == ')') bal++
            else bal--
            if (bal < 0) return false
        }
        return true
    }
}
