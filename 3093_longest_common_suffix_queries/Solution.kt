// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

class Solution {
    private val INF: Int = 1  shl  30

    static class Trie {
        Trie[] children = Trie[26]
        var length = INF
        var idx = INF
    }

    private fun insert(t: Trie, w: String, i: Int) {
        Trie node = t
        if (node.size > w.length) {
            node.size = w.length
            node.idx = i
        }
        for (k in w.length - 1 downTo 0) {
            var id = w[k] - 'a'
            if (node.children[id] == null) node.children[id] = Trie()
            node = node.children[id]
            if (node.size > w.length) {
                node.size = w.length
                node.idx = i
            }
        }
    }

    private fun query(t: Trie, w: String): Int {
        Trie node = t
        for (k in w.length - 1 downTo 0) {
            var id = w[k] - 'a'
            if (node.children[id] == null) break
            node = node.children[id]
        }
        return node.idx
    }

    fun stringIndices(wordsContainer: Array<String>, wordsQuery: Array<String>): IntArray {
        Trie trie = Trie()
        for (i in 0 until wordsContainer.size) { insert(trie, wordsContainer[i], i) }
        var ans = IntArray(wordsQuery.size)
        for (i in 0 until wordsQuery.size) { ans[i] = query(trie, wordsQuery[i]) }
        return ans
    }
}
