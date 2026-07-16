// LeetCode 0310 - Minimum Height Trees
// https://leetcode.com/problems/minimum-height-trees/

class Solution {
    fun findMinHeightTrees(n: Int, edges: Array<IntArray>): List<Int> {
        if (n <= 2) {
            return (0 until n).toList()
        }

        val graph = Array(n) { mutableListOf<Int>() }
        val degree = IntArray(n)
        for (edge in edges) {
            val left = edge[0]
            val right = edge[1]
            graph[left].add(right)
            graph[right].add(left)
            degree[left]++
            degree[right]++
        }

        var leaves = mutableListOf<Int>()
        for (node in 0 until n) {
            if (degree[node] == 1) {
                leaves.add(node)
            }
        }

        var remaining = n
        while (remaining > 2) {
            remaining -= leaves.size
            val newLeaves = mutableListOf<Int>()
            for (leaf in leaves) {
                for (neighbor in graph[leaf]) {
                    degree[neighbor]--
                    if (degree[neighbor] == 1) {
                        newLeaves.add(neighbor)
                    }
                }
            }
            leaves = newLeaves
        }
        return leaves
    }
}
