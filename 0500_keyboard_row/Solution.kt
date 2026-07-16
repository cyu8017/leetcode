// LeetCode 0500 - Keyboard Row
// https://leetcode.com/problems/keyboard-row/

class Solution {
    fun findWords(words: Array<String>): Array<String> {
        val rows = listOf(
            "qwertyuiop".toSet(),
            "asdfghjkl".toSet(),
            "zxcvbnm".toSet(),
        )
        return words.filter { word ->
            val letters = word.filter { it.isLetter() }.map { it.lowercaseChar() }.toSet()
            rows.any { row -> row.containsAll(letters) }
        }.toTypedArray()
    }
}
