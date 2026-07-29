// LeetCode 1003 - Check If Word Is Valid After Substitutions
// https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

class Solution {
    fun isValid(s: String): Boolean {
        val stack = StringBuilder()
        for (ch in s) {
            stack.append(ch)
            val n = stack.length
            if (n >= 3 && stack[n - 3] == 'a' && stack[n - 2] == 'b' && stack[n - 1] == 'c') {
                stack.setLength(n - 3)
            }
        }
        return stack.isEmpty()
    }
}
