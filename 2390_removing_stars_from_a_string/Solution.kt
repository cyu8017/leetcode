// LeetCode 2390 - Removing Stars From a String
// https://leetcode.com/problems/removing-stars-from-a-string/

class Solution {
    fun removeStars(s: String): String {
        val stack = StringBuilder()
        for (c in s) {
            if (c == '*') stack.deleteCharAt(stack.lastIndex)
            else stack.append(c)
        }
        return stack.toString()
    }
}
