// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

class Solution {
    fun sortSentence(s: String): String {
        val tokens = s.split(" ")
        val ordered = Array(tokens.size) { "" }
        for (token in tokens) {
            val position = token.last().digitToInt() - 1
            ordered[position] = token.dropLast(1)
        }
        return ordered.joinToString(" ")
    }
}
