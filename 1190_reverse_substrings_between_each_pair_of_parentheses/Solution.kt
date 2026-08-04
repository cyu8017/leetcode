// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution {
    fun reverseParentheses(s: String): String {
        val stack = ArrayDeque<Char>()
        for (ch in s) {
            if (ch == ')') {
                val chunk = mutableListOf<Char>()
                while (stack.isNotEmpty() && stack.last() != '(') chunk.add(stack.removeLast())
                stack.removeLast()
                for (c in chunk) stack.addLast(c)
            } else stack.addLast(ch)
        }
        return stack.joinToString("")
    }
}
