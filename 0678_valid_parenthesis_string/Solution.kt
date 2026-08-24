// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/


class Solution {
    fun checkValidString(s: String): Boolean {
        var low = 0
        var high = 0
        for (ch in s) {
            when (ch) {
                '(' -> {
                    low++
                    high++
                }
                ')' -> {
                    low = maxOf(low - 1, 0)
                    high--
                    if (high < 0) return false
                }
                else -> {
                    low = maxOf(low - 1, 0)
                    high++
                }
            }
        }
        return low == 0
    }
}
