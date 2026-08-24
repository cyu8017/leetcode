// LeetCode 0524 - Longest Word in Dictionary through Deleting
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

class Solution {
    fun findLongestWord(s: String, dictionary: List<String>): String {
        var best = ""
        for (word in dictionary) {
            if (isSubsequence(word, s) && (word.length > best.length || (word.length == best.length && word < best))) {
                best = word
            }
        }
        return best
    }

    private fun isSubsequence(word: String, source: String): Boolean {
        var index = 0
        for (char in source) {
            if (index < word.length && word[index] == char) {
                index++
            }
        }
        return index == word.length
    }
}
