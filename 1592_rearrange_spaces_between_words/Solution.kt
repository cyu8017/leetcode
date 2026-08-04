// LeetCode 1592 - Rearrange Spaces Between Words
// https://leetcode.com/problems/rearrange-spaces-between-words/

class Solution {
    fun reorderSpaces(text: String): String {
        val words = text.trim().split(Regex("\\s+")).filter { it.isNotEmpty() }
        var spaces = 0
        for (ch in text) if (ch == ' ') spaces++
        if (words.size <= 1) {
            return (if (words.isEmpty()) "" else words[0]) + " ".repeat(spaces)
        }
        val between = spaces / (words.size - 1)
        val trailing = spaces % (words.size - 1)
        val sb = StringBuilder()
        for (i in words.indices) {
            if (i > 0) sb.append(" ".repeat(between))
            sb.append(words[i])
        }
        sb.append(" ".repeat(trailing))
        return sb.toString()
    }
}
