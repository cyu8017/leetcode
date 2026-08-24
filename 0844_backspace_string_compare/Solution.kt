// LeetCode 0844 - Backspace String Compare
// https://leetcode.com/problems/backspace-string-compare/

class Solution {
    fun backspaceCompare(s: String, t: String): Boolean {
        return build((s) == build(t))
    }

    private fun build(text: String): String {
        var stack = StringBuilder()
        for (ch in text.toCharArray()) {
            if (ch == '#') {
                if (stack.length > 0) stack.deleteCharAt(stack.length() - 1)
            } else {
                stack.append(ch)
            }
        }
        return stack.toString()
    }
}
