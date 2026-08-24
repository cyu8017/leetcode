// LeetCode 1719 - Number Of Ways To Reconstruct A Tree
// https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

class Solution {
    fun checkWays(pairs: Array<IntArray>): Int {
        val graph = HashMap<Int, HashSet<Int>>()
        for ((a, b) in pairs) {
            graph.getOrPut(a) { HashSet() }.add(b)
            graph.getOrPut(b) { HashSet() }.add(a)
        }
        val n = graph.size
        val root = graph.entries.firstOrNull { it.value.size == n - 1 }?.key ?: return 0
        var ans = 1
        for ((node, neighbors) in graph) {
            if (node == root) {
                continue
            }
            var parent = -1
            var parentDegree = n + 1
            for (nei in neighbors) {
                val neiDegree = graph[nei]!!.size
                if (neiDegree >= neighbors.size && neiDegree < parentDegree) {
                    parent = nei
                    parentDegree = neiDegree
                }
            }
            if (parent == -1) {
                return 0
            }
            for (nei in neighbors) {
                if (nei != parent && nei !in graph[parent]!!) {
                    return 0
                }
            }
            if (graph[parent]!!.size == neighbors.size) {
                ans = 2
            }
        }
        return ans
    }
}
