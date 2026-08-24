// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/


class Solution {
    private lateinit var g: Array<MutableList<IntArray>>
    private lateinit var up: Array<IntArray>
    private lateinit var depth: IntArray
    private lateinit var cnt: Array<IntArray>
    private val LOG = 15

    fun minOperationsQueries(n: Int, edges: Array<IntArray>, queries: Array<IntArray>): IntArray {
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(intArrayOf(e[1], e[2]))
            g[e[1]].add(intArrayOf(e[0], e[2]))
        }
        up = Array(LOG) { IntArray(n) }
        depth = IntArray(n)
        cnt = Array(n) { IntArray(27) }
        dfs(0, 0)
        for (j in 1 until LOG) {
            for (i in 0 until n) up[j][i] = up[j - 1][up[j - 1][i]]
        }
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val a = queries[i][0]
            val b = queries[i][1]
            val c = lca(a, b)
            val total = depth[a] + depth[b] - 2 * depth[c]
            var best = 0
            for (w in 1..26) {
                val f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w]
                best = maxOf(best, f)
            }
            ans[i] = total - best
        }
        return ans
    }

    private fun dfs(u: Int, p: Int) {
        up[0][u] = p
        for (e in g[u]) {
            val v = e[0]
            val w = e[1]
            if (v == p) continue
            depth[v] = depth[u] + 1
            System.arraycopy(cnt[u], 0, cnt[v], 0, 27)
            cnt[v][w]++
            dfs(v, u)
        }
    }

    private fun lca(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        if (depth[a] < depth[b]) {
            val t = a; a = b; b = t
        }
        var diff = depth[a] - depth[b]
        for (j in 0 until LOG) if ((diff and (1 shl j)) != 0) a = up[j][a]
        if (a == b) return a
        for (j in LOG - 1 downTo 0) {
            if (up[j][a] != up[j][b]) {
                a = up[j][a]
                b = up[j][b]
            }
        }
        return up[0][a]
    }
}
