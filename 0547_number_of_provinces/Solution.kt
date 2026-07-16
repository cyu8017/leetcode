// LeetCode 0547 - Number of Provinces
// https://leetcode.com/problems/number-of-provinces/

class Solution {
    fun findCircleNum(isConnected: Array<IntArray>): Int {
        val n = isConnected.size
        val parent = IntArray(n) { it }

        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (isConnected[i][j] == 1) {
                    union(parent, i, j)
                }
            }
        }

        return (0 until n).count { find(parent, it) == it }
    }

    private fun find(parent: IntArray, x: Int): Int {
        var node = x
        while (parent[node] != node) {
            parent[node] = parent[parent[node]]
            node = parent[node]
        }
        return node
    }

    private fun union(parent: IntArray, a: Int, b: Int) {
        val rootA = find(parent, a)
        val rootB = find(parent, b)
        if (rootA != rootB) {
            parent[rootB] = rootA
        }
    }
}
