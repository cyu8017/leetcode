// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

class Trie {
    private class TrieNode {
        val children = HashMap<Char, TrieNode>()
        var wordCount = 0
        var prefixCount = 0
    }

    private val root = TrieNode()

    fun insert(word: String) {
        var node = root
        for (ch in word) {
            node = node.children.getOrPut(ch) { TrieNode() }
            node.prefixCount++
        }
        node.wordCount++
    }

    fun countWordsEqualTo(word: String): Int {
        val node = find(word) ?: return 0
        return node.wordCount
    }

    fun countWordsStartingWith(prefix: String): Int {
        val node = find(prefix) ?: return 0
        return node.prefixCount
    }

    fun erase(word: String) {
        var node = root
        for (ch in word) {
            node = node.children[ch]!!
            node.prefixCount--
        }
        node.wordCount--
    }

    private fun find(text: String): TrieNode? {
        var node = root
        for (ch in text) {
            node = node.children[ch] ?: return null
        }
        return node
    }
}
