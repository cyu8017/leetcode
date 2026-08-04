// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution {
    fun minRemoveToMakeValid(s: String): String {
        val chars = s.toCharArray()
        val opens = ArrayDeque<Int>()
        for (i in chars.indices) {
            when (chars[i]) {
                '(' -> opens.addLast(i)
                ')' -> {
                    if (opens.isEmpty()) chars[i] = 0.toChar()
                    else opens.removeLast()
                }
            }
        }
        while (opens.isNotEmpty()) chars[opens.removeLast()] = 0.toChar()
        return chars.filter { it.code != 0 }.joinToString("")
    }
}
