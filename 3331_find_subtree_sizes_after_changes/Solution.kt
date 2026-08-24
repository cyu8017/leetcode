// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var ng: Array<ArrayList<Int>>
    private lateinit var s: String
    private lateinit var newParent: IntArray
    private lateinit var last: IntArray
    private lateinit var ans: IntArray

    private fun dfs1(u: Int) {
        val c = s[u] - 'a'
        val prev = last[c]
        if (prev != -1) newParent[u] = prev
        last[c] = u
        for (v in g[u]) dfs1(v)
        last[c] = prev
    }

    private fun dfs2(u: Int): Int {
        var sz = 1
        for (v in ng[u]) sz += dfs2(v)
        ans[u] = sz
        return sz
    }

    fun findSubtreeSizes(parent: IntArray, s: String): IntArray {
        val n = parent.size
        this.s = s
        g = Array(n) { ArrayList() }
        for (i in 1 until n) g[parent[i]].add(i)
        newParent = parent.clone()
        last = IntArray(26) { -1 }
        dfs1(0)
        ng = Array(n) { ArrayList() }
        for (i in 1 until n) ng[newParent[i]].add(i)
        ans = IntArray(n)
        dfs2(0)
        return ans
    }
}
