// LeetCode 0856 - Score of Parentheses
// https://leetcode.com/problems/score-of-parentheses/

class Solution {
    fun scoreOfParentheses(s: String): Int {
        var stack = ArrayDeque<Int>()
        stack.push(0)
        for (ch in s.toCharArray()) {
            if (ch == '(') stack.push(0)
            else {
                var `val` = stack.pop()
                stack.push(stack.pop() + maxOf(2 * val, 1))
            }
        }
        return stack.peek()
    }
}
