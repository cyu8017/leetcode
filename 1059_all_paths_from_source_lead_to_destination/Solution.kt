// LeetCode 1059 - All Paths from Source Lead to Destination
// https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

class Solution {
    fun leadsToDestination(n: Int, edges: Array<IntArray>, source: Int, destination: Int): Boolean {
        val graph = Array(n) { mutableListOf<Int>() }
        for (e in edges) graph[e[0]].add(e[1])
        val state = IntArray(n)
        return dfs(source, destination, graph, state)
    }

    private fun dfs(node: Int, destination: Int, graph: Array<MutableList<Int>>, state: IntArray): Boolean {
        if (graph[node].isEmpty()) return node == destination
        if (state[node] == 1) return false
        if (state[node] == 2) return true
        state[node] = 1
        for (nxt in graph[node]) {
            if (!dfs(nxt, destination, graph, state)) return false
        }
        state[node] = 2
        return true
    }
}
