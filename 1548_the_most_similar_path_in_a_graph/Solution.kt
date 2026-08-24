// LeetCode 1548 - The Most Similar Path in a Graph
// https://leetcode.com/problems/the-most-similar-path-in-a-graph/

class Solution {
    fun mostSimilar(n: Int, roads: Array<IntArray>, names: Array<String>, targetPath: Array<String>): List<Int> {
        val graph = Array(n) { mutableListOf<Int>() }
        for (r in roads) {
            graph[r[0]].add(r[1])
            graph[r[1]].add(r[0])
        }
        var costs = IntArray(n)
        val parents = Array(targetPath.size) { IntArray(n) }
        for (node in 0 until n) {
            costs[node] = if (names[node] == targetPath[0]) 0 else 1
            parents[0][node] = -1
        }
        for (i in 1 until targetPath.size) {
            val nextCosts = IntArray(n)
            for (node in 0 until n) {
                var bestCost = Int.MAX_VALUE
                var bestPrev = -1
                for (previous in graph[node]) {
                    if (costs[previous] < bestCost) {
                        bestCost = costs[previous]
                        bestPrev = previous
                    }
                }
                nextCosts[node] = bestCost + if (names[node] == targetPath[i]) 0 else 1
                parents[i][node] = bestPrev
            }
            costs = nextCosts
        }
        var end = 0
        for (node in 1 until n) {
            if (costs[node] < costs[end]) end = node
        }
        val path = IntArray(targetPath.size)
        for (i in targetPath.size - 1 downTo 0) {
            path[i] = end
            end = parents[i][end]
        }
        return path.toList()
    }
}
