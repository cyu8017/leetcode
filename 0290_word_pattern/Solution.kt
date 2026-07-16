// LeetCode 0290 - Word Pattern
// https://leetcode.com/problems/word-pattern/

class Solution {
    fun wordPattern(pattern: String, s: String): Boolean {
        val words = s.split(" ")
        if (pattern.length != words.size) {
            return false
        }
        val charToWord = HashMap<Char, String>()
        val wordToChar = HashMap<String, Char>()
        for (index in pattern.indices) {
            val ch = pattern[index]
            val word = words[index]
            if (ch in charToWord) {
                if (charToWord[ch] != word) {
                    return false
                }
            } else {
                if (word in wordToChar) {
                    return false
                }
                charToWord[ch] = word
                wordToChar[word] = ch
            }
        }
        return true
    }
}
