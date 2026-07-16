// LeetCode 0208 - Implement Trie (Prefix Tree)\n// https://leetcode.com/problems/\n\nclass Trie {
    private class TrieNode { val children = mutableMapOf<Char, TrieNode>(); var isWord = false }
    private val root = TrieNode()

    fun insert(word: String) {
        var node = root
        for (c in word) node = node.children.getOrPut(c) { TrieNode() }
        node.isWord = true
    }

    fun search(word: String): Boolean = find(word)?.isWord == true
    fun startsWith(prefix: String): Boolean = find(prefix) != null

    private fun find(text: String): TrieNode? {
        var node = root
        for (c in text) node = node.children[c] ?: return null
        return node
    }
}
