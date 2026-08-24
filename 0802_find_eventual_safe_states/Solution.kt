// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

class Solution {
    fun eventualSafeNodes(graph: Array<IntArray>): MutableList<Int> {
        var n = graph.size
        var color = IntArray(n)
        var ans = ArrayList<Int>()
        for (i in 0 until n) { if (dfs(graph, color, i)) ans.add(i) }
        return ans
    }

    private fun dfs(graph: Array<IntArray>, color: IntArray, node: Int): Boolean {
        if (color[node] != 0) return color[node] == 2
        color[node] = 1
        for (nei in graph[node]) {
            if (!dfs(graph, color, nei)) return false
        }
        color[node] = 2
        return true
    }
}
