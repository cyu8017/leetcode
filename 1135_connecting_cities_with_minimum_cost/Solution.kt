// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

class Solution {
    fun minimumCost(n: Int, connections: Array<IntArray>): Int {
        val parent = IntArray(n + 1) { it }
        fun find(x: Int): Int {
            var cur = x
            while (parent[cur] != cur) {
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            }
            return cur
        }
        fun union(a: Int, b: Int): Boolean {
            val ra = find(a)
            val rb = find(b)
            if (ra == rb) return false
            parent[rb] = ra
            return true
        }
        connections.sortBy { it[2] }
        var cost = 0
        var edges = 0
        for (c in connections) {
            if (union(c[0], c[1])) {
                cost += c[2]
                edges++
                if (edges == n - 1) return cost
            }
        }
        return -1
    }
}
