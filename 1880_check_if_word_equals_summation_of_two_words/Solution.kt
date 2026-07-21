// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution {
    private fun value(word: String): Int {
        var result = 0
        for (ch in word) {
            result = result * 10 + (ch - 'a')
        }
        return result
    }

    fun isSumEqual(firstWord: String, secondWord: String, targetWord: String): Boolean {
        return value(firstWord) + value(secondWord) == value(targetWord)
    }
}
