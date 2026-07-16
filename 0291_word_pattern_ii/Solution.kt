// LeetCode 0291 - Word Pattern II
// https://leetcode.com/problems/word-pattern-ii/

class Solution {
    fun wordPatternMatch(pattern: String, s: String): Boolean {
        return backtrack(pattern, s, 0, 0, mutableMapOf(), mutableMapOf())
    }

    private fun backtrack(
        pattern: String,
        s: String,
        patternIndex: Int,
        stringIndex: Int,
        charToWord: MutableMap<Char, String>,
        wordToChar: MutableMap<String, Char>,
    ): Boolean {
        if (patternIndex == pattern.length) {
            return stringIndex == s.length
        }
        val ch = pattern[patternIndex]
        charToWord[ch]?.let { word ->
            if (!s.startsWith(word, stringIndex)) {
                return false
            }
            return backtrack(pattern, s, patternIndex + 1, stringIndex + word.length, charToWord, wordToChar)
        }
        for (end in stringIndex + 1..s.length) {
            val word = s.substring(stringIndex, end)
            if (word in wordToChar) {
                continue
            }
            charToWord[ch] = word
            wordToChar[word] = ch
            if (backtrack(pattern, s, patternIndex + 1, end, charToWord, wordToChar)) {
                return true
            }
            charToWord.remove(ch)
            wordToChar.remove(word)
        }
        return false
    }
}
