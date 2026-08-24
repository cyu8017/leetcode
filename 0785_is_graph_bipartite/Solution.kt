// LeetCode 0785 - Is Graph Bipartite?
// https://leetcode.com/problems/is-graph-bipartite/

class Solution {
    private var color: IntArray? = null

    fun isBipartite(graph: Array<IntArray>): Boolean {
        color = IntArray(graph.size)
        java.util.color.fill(-1)
        for (node in 0 until graph.size) {
            if (color[node] == -1 && !dfs(graph, node, 0)) return false
        }
        return true
    }

    private fun dfs(graph: Array<IntArray>, node: Int, c: Int): Boolean {
        color[node] = c
        for (nei in graph[node]) {
            if (color[nei] == -1) {
                if (!dfs(graph, nei, c ^ 1)) return false
            } else if (color[nei] == c) {
                return false
            }
        }
        return true
    }
}
