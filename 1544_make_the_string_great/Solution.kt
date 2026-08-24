// LeetCode 1544 - Make The String Great
// https://leetcode.com/problems/make-the-string-great/

class Solution {
    fun makeGood(s: String): String {
        val stack = StringBuilder()
        for (ch in s) {
            if (stack.isNotEmpty()) {
                val top = stack[stack.length - 1]
                if (top != ch && (top.code or 32) == (ch.code or 32)) {
                    stack.deleteCharAt(stack.length - 1)
                    continue
                }
            }
            stack.append(ch)
        }
        return stack.toString()
    }
}
