// LeetCode 0212 - Word Search II
// https://leetcode.com/problems/word-search-ii/

class Solution {
    private class TrieNode {
        val children = mutableMapOf<Char, TrieNode>()
        var word: String? = null
    }

    private lateinit var board: Array<CharArray>
    private var rows = 0
    private var cols = 0
    private val result = linkedSetOf<String>()

    fun findWords(board: Array<CharArray>, words: Array<String>): List<String> {
        this.board = board
        rows = board.size
        cols = board[0].size

        val root = TrieNode()
        for (word in words) {
            var node = root
            for (c in word) {
                node = node.children.getOrPut(c) { TrieNode() }
            }
            node.word = word
        }

        for (row in 0 until rows) {
            for (col in 0 until cols) {
                dfs(row, col, root)
            }
        }
        return result.toList()
    }

    private fun dfs(row: Int, col: Int, node: TrieNode) {
        val c = board[row][col]
        val next = node.children[c] ?: return
        next.word?.let {
            result.add(it)
            next.word = null
        }
        board[row][col] = '#'
        if (row + 1 < rows && board[row + 1][col] != '#') dfs(row + 1, col, next)
        if (row - 1 >= 0 && board[row - 1][col] != '#') dfs(row - 1, col, next)
        if (col + 1 < cols && board[row][col + 1] != '#') dfs(row, col + 1, next)
        if (col - 1 >= 0 && board[row][col - 1] != '#') dfs(row, col - 1, next)
        board[row][col] = c
        if (next.children.isEmpty()) {
            node.children.remove(c)
        }
    }
}
