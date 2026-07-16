// LeetCode 0032 - Longest Valid Parentheses
// https://leetcode.com/problems/longest-valid-parentheses/

class Solution {
    fun longestValidParentheses(s: String): Int {
        val stack = ArrayDeque<Int>()
        stack.addLast(-1)
        var best = 0

        for (i in s.indices) {
            if (s[i] == '(') {
                stack.addLast(i)
            } else {
                stack.removeLast()
                if (stack.isEmpty()) {
                    stack.addLast(i)
                } else {
                    best = maxOf(best, i - stack.last())
                }
            }
        }

        return best
    }
}
