// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

class Solution {
    companion object {
        const val MOD = 1_000_000_007
        const val LOG = 17
    }
    lateinit var depth: IntArray
    lateinit var parent: Array<IntArray>
    lateinit var graph: Array<ArrayList<Int>>

    fun dfs(u: Int, p: Int) {
        parent[0][u] = p
        for (v in graph[u]) {
            if (v != p) {
                depth[v] = depth[u] + 1
                dfs(v, u)
            }
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

    fun modPow(exp0: Int): Int {
        var exp = exp0
        var base = 2L
        var res = 1L
        while (exp > 0) {
            if ((exp and 1) != 0) res = res * base % MOD
            base = base * base % MOD
            exp = exp shr 1
        }
        return res.toInt()
    }

    fun assignEdgeWeights(edges: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val n = edges.size + 1
        depth = IntArray(n + 1)
        graph = Array(n + 1) { ArrayList() }
        parent = Array(LOG) { IntArray(n + 1) { -1 } }
        for (e in edges) {
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        }
        dfs(1, -1)
        for (k in 1 until LOG) {
            for (v in 1..n) {
                if (parent[k - 1][v] != -1) parent[k][v] = parent[k - 1][parent[k - 1][v]]
            }
        }
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val u = queries[i][0]
            val v = queries[i][1]
            if (u == v) { ans[i] = 0; continue }
            val a = lca(u, v)
            val d = depth[u] + depth[v] - 2 * depth[a]
            ans[i] = modPow(d - 1)
        }
        return ans
    }
}
