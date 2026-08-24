// LeetCode 3136 - Valid Word
// https://leetcode.com/problems/valid-word/

class Solution {
    fun isValid(word: String): Boolean {
        if (word.length < 3) return false
        var hasVowel = false
        var hasConsonant = false
        var vs = BooleanArray(26)
        for (c in "aeiou".toCharArray()) { vs[c - 'a'] = true }
        for (i in 0 until word.length) {
            var c = word[i]
            if (c.isLetter()) {
                var lower = c.lowercaseChar()
                if (vs[lower - 'a']) hasVowel = true
                else hasConsonant = true
            } else if (!c.isDigit()) {
                return false
            }
        }
        return hasVowel && hasConsonant
    }
}
