// LeetCode 1032 - Stream of Characters
// https://leetcode.com/problems/stream-of-characters/

class StreamChecker(words: Array<String>) {
    private class TrieNode {
        val children = arrayOfNulls<TrieNode>(26)
        var isWord = false
    }

    private val root = TrieNode()
    private val stream = StringBuilder()

    init {
        for (word in words) {
            var node = root
            for (i in word.length - 1 downTo 0) {
                val idx = word[i] - 'a'
                if (node.children[idx] == null) node.children[idx] = TrieNode()
                node = node.children[idx]!!
            }
            node.isWord = true
        }
    }

    fun query(letter: Char): Boolean {
        stream.append(letter)
        var node = root
        for (i in stream.length - 1 downTo 0) {
            if (node.isWord) return true
            val idx = stream[i] - 'a'
            val next = node.children[idx] ?: return false
            node = next
        }
        return node.isWord
    }
}
