// LeetCode 0261 - Graph Valid Tree
// https://leetcode.com/problems/graph-valid-tree/

class Solution {
    fun validTree(n: Int, edges: Array<IntArray>): Boolean {
        if (edges.size != n - 1) {
            return false
        }
        val parent = IntArray(n) { it }

        fun find(node: Int): Int {
            if (parent[node] != node) {
                parent[node] = find(parent[node])
            }
            return parent[node]
        }

        for (edge in edges) {
            val rootLeft = find(edge[0])
            val rootRight = find(edge[1])
            if (rootLeft == rootRight) {
                return false
            }
            parent[rootLeft] = rootRight
        }
        return true
    }
}
