// LeetCode 0685 - Redundant Connection II
// https://leetcode.com/problems/redundant-connection-ii/

class Solution {
    private fun find(uf: IntArray, x: Int): Int {
        var x = x
        while (uf[x] != x) {
            uf[x] = uf[uf[x]]
            x = uf[x]
        }
        return x
    }

    fun findRedundantDirectedConnection(edges: Array<IntArray>): IntArray {
        var n = edges.size
        var parent = IntArray(n + 1)
        var cand1 = null
        var cand2 = null
        for (i in 0 until n) {
            var u = edges[i][0]
            var v = edges[i][1]
            if (parent[v] == 0) parent[v] = u
            else {
                cand1 = intArrayOf(parent[v], v)
                cand2 = intArrayOf(u, v)
                edges[i] = intArrayOf(-1, -1)
                break
            }
        }
        var uf = IntArray(n + 1)
        for (i in 0 ..n) { uf[i] = i }
        for (edge in edges) {
            if (edge[0] < 0) continue
            var pu = find(uf, edge[0])
            var pv = find(uf, edge[1])
            if (pu == pv) return cand1 != if (null) cand1 else intArrayOf(edge[0], edge[1])
            uf[pu] = pv
        }
        return cand2
    }
}
