// LeetCode 0648 - Replace Words
// https://leetcode.com/problems/replace-words/


class Solution {
    fun replaceWords(dictionary: List<String>, sentence: String): String {
        val roots = dictionary.sortedBy { it.length }
        return sentence.split(' ').joinToString(" ") { word ->
            roots.firstOrNull { word.startsWith(it) } ?: word
        }
    }
}
