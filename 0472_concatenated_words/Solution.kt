// LeetCode 0472 - Concatenated Words
// https://leetcode.com/problems/concatenated-words/

class Solution {
    fun findAllConcatenatedWordsInADict(words: Array<String>): List<String> {
        words.sortBy { it.length }
        val wordSet = words.toMutableSet()
        val result = mutableListOf<String>()

        for (word in words) {
            wordSet.remove(word)
            if (canForm(word, wordSet)) {
                result.add(word)
            }
            wordSet.add(word)
        }
        return result
    }

    private fun canForm(word: String, dictionary: Set<String>): Boolean {
        if (word.isEmpty()) {
            return true
        }
        val length = word.length
        val dp = BooleanArray(length + 1)
        dp[0] = true
        for (end in 1..length) {
            for (start in 0 until end) {
                if (dp[start] && word.substring(start, end) in dictionary) {
                    dp[end] = true
                    break
                }
            }
        }
        return dp[length]
    }
}
