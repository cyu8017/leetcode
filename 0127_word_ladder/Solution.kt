// LeetCode 0127 - Word Ladder
// https://leetcode.com/problems/word-ladder/

class Solution {
    fun ladderLength(beginWord: String, endWord: String, wordList: List<String>): Int {
        val words = wordList.toHashSet()
        if (endWord !in words) return 0
        val queue = ArrayDeque<String>()
        val visited = mutableSetOf(beginWord)
        queue.addLast(beginWord)
        var steps = 1
        while (queue.isNotEmpty()) {
            repeat(queue.size) {
                val word = queue.removeFirst()
                if (word == endWord) return steps
                val chars = word.toCharArray()
                for (i in chars.indices) {
                    val original = chars[i]
                    for (c in 'a'..'z') {
                        chars[i] = c
                        val next = String(chars)
                        if (next in words && visited.add(next)) queue.addLast(next)
                    }
                    chars[i] = original
                }
            }
            steps++
        }
        return 0
    }
}