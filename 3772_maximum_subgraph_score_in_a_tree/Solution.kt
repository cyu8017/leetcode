// LeetCode 3772 - Maximum Subgraph Score In A Tree
// https://leetcode.com/problems/maximum_subgraph_score_in_a_tree/

class Solution {
    fun maxSubgraphScore(n: Int, edges: Array<IntArray>, good: IntArray): IntArray {
        val g = Array(n) { ArrayList<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        val parent = IntArray(n) { -2 }
        parent[0] = -1
        val order = ArrayList<Int>()
        order.add(0)
        var i = 0
        while (i < order.size) {
            val u = order[i++]
            for (v in g[u]) {
                if (parent[v] == -2) {
                    parent[v] = u
                    order.add(v)
                }
            }
        }
        val down = IntArray(n)
        for (idx in n - 1 downTo 0) {
            val u = order[idx]
            down[u] = 2 * good[u] - 1
            for (v in g[u]) {
                if (parent[v] == u && down[v] > 0) down[u] += down[v]
            }
        }
        val ans = down.copyOf()
        for (u in order) {
            for (v in g[u]) {
                if (parent[v] == u) {
                    var outside = ans[u]
                    if (down[v] > 0) outside -= down[v]
                    ans[v] = down[v]
                    if (outside > 0) ans[v] += outside
                }
            }
        }
        return ans
    }
}
