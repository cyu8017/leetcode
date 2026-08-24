// LeetCode 0030 - Substring with Concatenation of All Words
// https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution {
    fun findSubstring(s: String, words: Array<String>): List<Int> {
        if (words.isEmpty() || s.isEmpty()) {
            return emptyList()
        }

        val wordLen = words[0].length
        val wordCount = words.size
        val need = words.groupingBy { it }.eachCount().toMutableMap()
        val result = mutableListOf<Int>()

        for (start in 0 until wordLen) {
            var left = start
            val counts = mutableMapOf<String, Int>()
            var used = 0

            var right = start
            while (right <= s.length - wordLen) {
                val word = s.substring(right, right + wordLen)
                if (word !in need) {
                    counts.clear()
                    used = 0
                    left = right + wordLen
                    right += wordLen
                    continue
                }

                counts[word] = counts.getOrDefault(word, 0) + 1
                used++

                while (counts.getValue(word) > need.getValue(word)) {
                    val leftWord = s.substring(left, left + wordLen)
                    counts[leftWord] = counts.getValue(leftWord) - 1
                    used--
                    left += wordLen
                }

                if (used == wordCount) {
                    result.add(left)
                }

                right += wordLen
            }
        }

        return result.sorted()
    }
}
