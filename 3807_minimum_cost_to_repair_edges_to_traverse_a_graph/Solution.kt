// LeetCode 3807 - Minimum Cost To Repair Edges To Traverse A Graph
// https://leetcode.com/problems/minimum_cost_to_repair_edges_to_traverse_a_graph/

class Solution {
    private lateinit var edges: Array<IntArray>
    private var n = 0
    private var k = 0

    fun minCost(n: Int, edges: Array<IntArray>, k: Int): Int {
        this.n = n
        this.k = k
        this.edges = edges
        edges.sortBy { it[2] }
        val m = edges.size
        if (m == 0) return -1
        var l = 0
        var r = m - 1
        while (l < r) {
            val mid = (l + r) shr 1
            if (check(mid)) r = mid else l = mid + 1
        }
        if (check(l)) return edges[l][2]
        return -1
    }

    private fun check(idx: Int): Boolean {
        val g = Array(n) { ArrayList<Int>() }
        for (i in 0..idx) {
            g[edges[i][0]].add(edges[i][1])
            g[edges[i][1]].add(edges[i][0])
        }
        var q = ArrayList<Int>()
        q.add(0)
        val vis = BooleanArray(n)
        vis[0] = true
        var dist = 0
        while (q.isNotEmpty()) {
            val nq = ArrayList<Int>()
            for (u in q) {
                if (u == n - 1) return dist <= k
                for (v in g[u]) {
                    if (!vis[v]) {
                        vis[v] = true
                        nq.add(v)
                    }
                }
            }
            q = nq
            dist++
        }
        return false
    }
}
