// LeetCode 1451 - Rearrange Words in a Sentence
// https://leetcode.com/problems/rearrange-words-in-a-sentence/

class Solution {
    fun arrangeWords(text: String): String {
        val words = text.lowercase().split(" ").toMutableList()
        words.sortBy { it.length }
        val joined = words.joinToString(" ")
        return joined.replaceFirstChar { it.uppercaseChar() }
    }
}
