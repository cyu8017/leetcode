// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

class Solution {
    companion object { const val LOG = 17 }
    lateinit var parent: Array<IntArray>
    lateinit var depth: IntArray
    lateinit var dist: IntArray
    lateinit var g: Array<ArrayList<IntArray>>

    fun dfs(u: Int, p: Int) {
        parent[0][u] = p
        for (e in g[u]) {
            val to = e[0]
            val w = e[1]
            if (to == p) continue
            depth[to] = depth[u] + 1
            dist[to] = dist[u] + w
            dfs(to, u)
        }
    }

    fun lca(u0: Int, v0: Int): Int {
        var u = u0
        var v = v0
        if (depth[u] < depth[v]) {
            val t = u; u = v; v = t
        }
        for (k in LOG - 1 downTo 0) {
            if (parent[k][u] != -1 && depth[parent[k][u]] >= depth[v]) u = parent[k][u]
        }
        if (u == v) return u
        for (k in LOG - 1 downTo 0) {
            if (parent[k][u] != -1 && parent[k][u] != parent[k][v]) {
                u = parent[k][u]
                v = parent[k][v]
            }
        }
        return parent[0][u]
    }

    fun path(u: Int, v: Int): Int {
        val a = lca(u, v)
        return dist[u] + dist[v] - 2 * dist[a]
    }

    fun minimumWeight(edges: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val n = edges.size + 1
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(intArrayOf(e[1], e[2]))
            g[e[1]].add(intArrayOf(e[0], e[2]))
        }
        parent = Array(LOG) { IntArray(n) { -1 } }
        depth = IntArray(n)
        dist = IntArray(n)
        dfs(0, -1)
        for (k in 1 until LOG) {
            for (v in 0 until n) {
                if (parent[k - 1][v] != -1) parent[k][v] = parent[k - 1][parent[k - 1][v]]
            }
        }
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val a = queries[i][0]
            val b = queries[i][1]
            val c = queries[i][2]
            ans[i] = (path(a, b) + path(b, c) + path(a, c)) / 2
        }
        return ans
    }
}
