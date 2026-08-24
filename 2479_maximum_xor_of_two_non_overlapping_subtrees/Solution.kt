// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

class Solution {
    private class Trie {
        val child = arrayOfNulls<Trie>(2)
    }

    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var values: IntArray
    private lateinit var sum: LongArray
    private lateinit var root: Trie
    private var ans = 0L

    private fun dfsSum(u: Int, p: Int): Long {
        var s = values[u].toLong()
        for (v in g[u]) if (v != p) s += dfsSum(v, u)
        sum[u] = s
        return s
    }

    private fun insert(x: Long) {
        var cur = root
        for (b in 46 downTo 0) {
            val bit = ((x shr b) and 1L).toInt()
            if (cur.child[bit] == null) cur.child[bit] = Trie()
            cur = cur.child[bit]!!
        }
    }

    private fun query(x: Long): Long {
        var cur = root
        if (cur.child[0] == null && cur.child[1] == null) return 0
        var res = 0L
        for (b in 46 downTo 0) {
            val bit = ((x shr b) and 1L).toInt()
            val want = bit xor 1
            if (cur.child[want] != null) {
                res = res or (1L shl b)
                cur = cur.child[want]!!
            } else if (cur.child[bit] != null) {
                cur = cur.child[bit]!!
            } else {
                return res
            }
        }
        return res
    }

    private fun dfs(u: Int, p: Int) {
        for (v in g[u]) {
            if (v == p) continue
            val xorv = query(sum[v])
            if (xorv > ans) ans = xorv
            dfs(v, u)
            insert(sum[v])
        }
    }

    fun maxXor(n: Int, edges: Array<IntArray>, values: IntArray): Long {
        this.values = values
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        sum = LongArray(n)
        dfsSum(0, -1)
        root = Trie()
        ans = 0
        dfs(0, -1)
        return ans
    }
}
