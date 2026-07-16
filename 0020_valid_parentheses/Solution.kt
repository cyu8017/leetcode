// LeetCode 0020 - Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

class Solution {
    fun isValid(s: String): Boolean {
        val stack = ArrayDeque<Char>()
        val pairs = mapOf(')' to '(', ']' to '[', '}' to '{')

        for (ch in s) {
            when (ch) {
                '(', '[', '{' -> stack.addLast(ch)
                else -> {
                    if (stack.isEmpty() || stack.removeLast() != pairs[ch]) {
                        return false
                    }
                }
            }
        }

        return stack.isEmpty()
    }
}
