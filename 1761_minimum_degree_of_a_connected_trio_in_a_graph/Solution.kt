// LeetCode 1761 - Minimum Degree of a Connected Trio in a Graph
// https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

class Solution {
    fun minTrioDegree(n: Int, edges: Array<IntArray>): Int {
        val adj = Array(n) { BooleanArray(n) }
        val degree = IntArray(n)
        for (e in edges) {
            val u = e[0] - 1
            val v = e[1] - 1
            adj[u][v] = true
            adj[v][u] = true
            degree[u]++
            degree[v]++
        }
        var best = Int.MAX_VALUE
        for (e in edges) {
            val u = e[0] - 1
            val v = e[1] - 1
            for (k in 0 until n) {
                if (adj[u][k] && adj[v][k]) {
                    best = minOf(best, degree[u] + degree[v] + degree[k] - 6)
                }
            }
        }
        return if (best == Int.MAX_VALUE) -1 else best
    }
}
