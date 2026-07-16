// LeetCode 0288 - Unique Word Abbreviation
// https://leetcode.com/problems/unique-word-abbreviation/

class ValidWordAbbr(dictionary: Array<String>) {
    private val groups = buildMap {
        for (word in dictionary) {
            val key = abbreviate(word)
            getOrPut(key) { mutableSetOf() }.add(word)
        }
    }

    fun isUnique(word: String): Boolean {
        val key = abbreviate(word)
        val words = groups[key] ?: emptySet()
        return words.isEmpty() || (words.size == 1 && word in words)
    }

    companion object {
        private fun abbreviate(word: String): String {
            if (word.length <= 2) {
                return word
            }
            return "${word.first()}${word.length - 2}${word.last()}"
        }
    }
}
