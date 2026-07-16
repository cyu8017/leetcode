// LeetCode 0211 - Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary {
    private class TrieNode {
        val children = mutableMapOf<Char, TrieNode>()
        var isWord = false
    }

    private val root = TrieNode()

    fun addWord(word: String) {
        var node = root
        for (c in word) {
            node = node.children.getOrPut(c) { TrieNode() }
        }
        node.isWord = true
    }

    fun search(word: String): Boolean = dfs(root, word, 0)

    private fun dfs(node: TrieNode, word: String, index: Int): Boolean {
        if (index == word.length) return node.isWord
        val c = word[index]
        if (c == '.') {
            for (child in node.children.values) {
                if (dfs(child, word, index + 1)) return true
            }
            return false
        }
        val next = node.children[c] ?: return false
        return dfs(next, word, index + 1)
    }
}
