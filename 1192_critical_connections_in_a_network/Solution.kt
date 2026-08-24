// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

class Solution {
    private var time = 0

    fun criticalConnections(n: Int, connections: List<List<Int>>): List<List<Int>> {
        val graph = Array(n) { mutableListOf<Int>() }
        for (e in connections) {
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        }
        val disc = IntArray(n) { -1 }
        val low = IntArray(n)
        val bridges = mutableListOf<List<Int>>()
        dfs(0, -1, graph, disc, low, bridges)
        return bridges.map { if (it[0] > it[1]) listOf(it[1], it[0]) else it }
    }

    private fun dfs(
        node: Int, parent: Int, graph: Array<MutableList<Int>>,
        disc: IntArray, low: IntArray, bridges: MutableList<List<Int>>
    ) {
        disc[node] = time
        low[node] = time
        time++
        for (nxt in graph[node]) {
            if (nxt == parent) continue
            if (disc[nxt] == -1) {
                dfs(nxt, node, graph, disc, low, bridges)
                low[node] = minOf(low[node], low[nxt])
                if (low[nxt] > disc[node]) bridges.add(listOf(node, nxt))
            } else {
                low[node] = minOf(low[node], disc[nxt])
            }
        }
    }
}
