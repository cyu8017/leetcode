// LeetCode 1443 - Minimum Time to Collect All Apples in a Tree
// https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

class Solution {
    fun minTime(n: Int, edges: Array<IntArray>, hasApple: List<Boolean>): Int {
        val graph = Array(n) { mutableListOf<Int>() }
        for (edge in edges) {
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        }
        fun visit(node: Int, parent: Int): Int {
            var cost = 0
            for (child in graph[node]) {
                if (child != parent) {
                    val childCost = visit(child, node)
                    if (childCost > 0 || hasApple[child]) cost += childCost + 2
                }
            }
            return cost
        }
        return visit(0, -1)
    }
}
