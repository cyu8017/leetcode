// LeetCode 0126 - Word Ladder II
// https://leetcode.com/problems/word-ladder-ii/

class Solution {
    fun findLadders(beginWord: String, endWord: String, wordList: List<String>): List<List<String>> {
        val words = wordList.toHashSet()
        if (endWord !in words) return emptyList()
        val parents = mutableMapOf<String, MutableList<String>>()
        val visited = mutableSetOf(beginWord)
        val queue = ArrayDeque<String>()
        queue.addLast(beginWord)
        var found = false

        while (queue.isNotEmpty() && !found) {
            val levelVisited = mutableSetOf<String>()
            repeat(queue.size) {
                val word = queue.removeFirst()
                val chars = word.toCharArray()
                for (i in chars.indices) {
                    val original = chars[i]
                    for (c in 'a'..'z') {
                        chars[i] = c
                        val next = String(chars)
                        if (next !in words || next in visited) continue
                        if (levelVisited.add(next)) queue.addLast(next)
                        parents.getOrPut(next) { mutableListOf() }.add(word)
                        if (next == endWord) found = true
                    }
                    chars[i] = original
                }
            }
            visited.addAll(levelVisited)
        }

        val result = mutableListOf<List<String>>()
        fun build(word: String, path: MutableList<String>) {
            path.add(word)
            if (word == beginWord) result.add(path.asReversed().toList())
            else for (parent in parents[word].orEmpty()) build(parent, path)
            path.removeAt(path.lastIndex)
        }
        if (found) build(endWord, mutableListOf())
        return result
    }
}