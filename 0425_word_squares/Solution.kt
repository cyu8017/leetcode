// LeetCode 0425 - Word Squares
// https://leetcode.com/problems/word-squares/

class Solution {
    fun wordSquares(words: Array<String>): List<List<String>> {
        val sortedWords = words.sorted()
        val length = sortedWords[0].length
        val prefixMap = mutableMapOf("" to sortedWords.toMutableList())
        for (word in sortedWords) {
            for (index in word.indices) {
                val prefix = word.substring(0, index + 1)
                prefixMap.getOrPut(prefix) { mutableListOf() }.add(word)
            }
        }

        val squares = mutableListOf<List<String>>()
        val current = mutableListOf<String>()

        fun dfs(row: Int) {
            if (row == length) {
                squares.add(current.toList())
                return
            }
            val prefix = buildString {
                for (word in current) {
                    append(word[row])
                }
            }
            for (candidate in prefixMap[prefix].orEmpty()) {
                current.add(candidate)
                dfs(row + 1)
                current.removeAt(current.lastIndex)
            }
        }

        dfs(0)
        return squares
    }
}
