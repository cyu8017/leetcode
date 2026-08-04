// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution {
    fun removeDuplicates(s: String, k: Int): String {
        val stack = ArrayDeque<IntArray>()
        for (ch in s) {
            if (stack.isNotEmpty() && stack.last()[0] == ch.code) stack.last()[1]++
            else stack.addLast(intArrayOf(ch.code, 1))
            if (stack.last()[1] == k) stack.removeLast()
        }
        val sb = StringBuilder()
        for (p in stack) repeat(p[1]) { sb.append(p[0].toChar()) }
        return sb.toString()
    }
}
