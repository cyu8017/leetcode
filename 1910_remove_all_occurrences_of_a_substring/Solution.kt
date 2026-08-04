// LeetCode 1910 - Remove All Occurrences Of A Substring
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

class Solution {
    fun removeOccurrences(s: String, part: String): String {
        val stack = StringBuilder()
        val m = part.length
        for (ch in s) {
            stack.append(ch)
            if (stack.length >= m && stack.substring(stack.length - m) == part) {
                stack.delete(stack.length - m, stack.length)
            }
        }
        return stack.toString()
    }
}
