// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

class Solution {
    private fun find(parent: IntArray, x: Int): Int {
        var x = x
        while (parent[x] != x) {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
    }

    fun findRedundantConnection(edges: Array<IntArray>): IntArray {
        var parent = IntArray(edges.size + 1)
        for (i in 0 until parent.size) { parent[i] = i }
        for (edge in edges) {
            var u = edge[0]
            var v = edge[1]
            var pu = find(parent, u)
            var pv = find(parent, v)
            if (pu == pv) return intArrayOf(u, v)
            parent[pu] = pv
        }
        return IntArray(0)
    }
}
