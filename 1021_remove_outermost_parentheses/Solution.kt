// LeetCode 1021 - Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/

class Solution {
    fun removeOuterParentheses(s: String): String {
        val ans = StringBuilder()
        var depth = 0
        for (ch in s) {
            if (ch == '(') {
                if (depth > 0) ans.append(ch)
                depth++
            } else {
                depth--
                if (depth > 0) ans.append(ch)
            }
        }
        return ans.toString()
    }
}
