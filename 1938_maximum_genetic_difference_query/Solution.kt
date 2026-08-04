// LeetCode 1938
// https://leetcode.com/problems/maximum-genetic-difference-query/

class Solution {
    private class TrieNode {
        val child = arrayOfNulls<TrieNode>(2)
        var cnt = 0
    }

    fun maxGeneticDifference(parents: IntArray, queries: Array<IntArray>): IntArray {
        val n = parents.size
        val children = Array(n) { mutableListOf<Int>() }
        var root = 0
        for (i in parents.indices) {
            if (parents[i] == -1) root = i else children[parents[i]].add(i)
        }
        val qmap = Array(n) { mutableListOf<IntArray>() }
        for (i in queries.indices) qmap[queries[i][0]].add(intArrayOf(i, queries[i][1]))
        val ans = IntArray(queries.size)
        val trieRoot = TrieNode()
        val bits = 17

        fun trieUpdate(num: Int, delta: Int) {
            var node = trieRoot
            for (b in bits downTo 0) {
                val bit = (num shr b) and 1
                if (node.child[bit] == null) node.child[bit] = TrieNode()
                node = node.child[bit]!!
                node.cnt += delta
            }
        }

        fun trieMaxXor(num: Int): Int {
            var node = trieRoot
            var res = 0
            for (b in bits downTo 0) {
                val bit = (num shr b) and 1
                val want = 1 - bit
                if (node.child[want] != null && node.child[want]!!.cnt > 0) {
                    res = res or (1 shl b)
                    node = node.child[want]!!
                } else {
                    node = node.child[bit]!!
                }
            }
            return res
        }

        fun dfs(u: Int) {
            trieUpdate(u, 1)
            for (q in qmap[u]) ans[q[0]] = trieMaxXor(q[1])
            for (v in children[u]) dfs(v)
            trieUpdate(u, -1)
        }
        dfs(root)
        return ans
    }
}
