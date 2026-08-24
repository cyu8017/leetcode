// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

class Solution {
    lateinit var graph: Array<ArrayList<Int>>
    lateinit var cost: IntArray
    var ans = 0

    fun minIncrease(n: Int, edges: Array<IntArray>, cost: IntArray): Int {
        graph = Array(n) { ArrayList() }
        for (e in edges) {
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        }
        this.cost = cost
        ans = 0
        dfs(0, -1)
        return ans
    }

    fun dfs(u: Int, p: Int): Long {
        if (graph[u].size == 1 && p != -1) return cost[u].toLong()
        val childVals = ArrayList<Long>()
        for (v in graph[u]) {
            if (v == p) continue
            childVals.add(dfs(v, u))
        }
        if (childVals.isEmpty()) return cost[u].toLong()
        var mx = 0L
        for (c in childVals) mx = maxOf(mx, c)
        for (c in childVals) if (c < mx) ans++
        return mx + cost[u]
    }
}
