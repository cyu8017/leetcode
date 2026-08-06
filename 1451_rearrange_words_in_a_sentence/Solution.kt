// LeetCode 1451 - Rearrange Words in a Sentence
// https://leetcode.com/problems/rearrange-words-in-a-sentence/

class Solution {
    fun arrangeWords(text: String): String {
        val words = text.lowercase().split(" ").sortedBy { it.length }
        return words.joinToString(" ").replaceFirstChar { it.uppercaseChar() }
    }
}
