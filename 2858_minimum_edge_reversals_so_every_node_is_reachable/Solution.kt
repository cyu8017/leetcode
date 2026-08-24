// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/


class Solution {
    private lateinit var g: Array<MutableList<IntArray>>
    private lateinit var ans: IntArray

    fun minEdgeReversals(n: Int, edges: Array<IntArray>): IntArray {
        g = Array(n) { ArrayList() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            g[u].add(intArrayOf(v, 0))
            g[v].add(intArrayOf(u, 1))
        }
        ans = IntArray(n)
        dfs1(0, -1)
        dfs2(0, -1)
        return ans
    }

    private fun dfs1(u: Int, p: Int) {
        for (e in g[u]) {
            val v = e[0]
            val ww = e[1]
            if (v == p) continue
            ans[0] += ww
            dfs1(v, u)
        }
    }

    private fun dfs2(u: Int, p: Int) {
        for (e in g[u]) {
            val v = e[0]
            val ww = e[1]
            if (v == p) continue
            ans[v] = if (ww == 0) ans[u] + 1 else ans[u] - 1
            dfs2(v, u)
        }
    }
}
