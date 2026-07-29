// LeetCode 1047 - Remove All Adjacent Duplicates In String
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution {
    fun removeDuplicates(s: String): String {
        val stack = StringBuilder()
        for (ch in s) {
            val n = stack.length
            if (n > 0 && stack[n - 1] == ch) stack.setLength(n - 1)
            else stack.append(ch)
        }
        return stack.toString()
    }
}
