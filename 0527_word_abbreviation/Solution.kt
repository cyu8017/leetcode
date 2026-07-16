// LeetCode 0527 - Word Abbreviation
// https://leetcode.com/problems/word-abbreviation/

class Solution {
    fun wordsAbbreviation(words: Array<String>): Array<String> {
        val prefixes = IntArray(words.size) { 1 }
        var changed = true
        while (changed) {
            changed = false
            val groups = mutableMapOf<String, MutableList<Int>>()
            for ((index, word) in words.withIndex()) {
                val key = abbreviate(word, prefixes[index])
                groups.getOrPut(key) { mutableListOf() }.add(index)
            }
            for (indices in groups.values) {
                if (indices.size > 1) {
                    changed = true
                    for (index in indices) {
                        prefixes[index]++
                    }
                }
            }
        }
        return Array(words.size) { index -> abbreviate(words[index], prefixes[index]) }
    }

    private fun abbreviate(word: String, prefix: Int): String {
        if (prefix + 2 >= word.length) {
            return word
        }
        val middle = word.length - prefix - 1
        val candidate = word.substring(0, prefix) + middle + word.last()
        return if (candidate.length < word.length) candidate else word
    }
}
