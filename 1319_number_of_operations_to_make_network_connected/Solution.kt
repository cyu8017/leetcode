// LeetCode 1319 - Number of Operations to Make Network Connected
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/

class Solution {
    fun makeConnected(n: Int, connections: Array<IntArray>): Int {
        if (connections.size < n - 1) return -1
        val parent = IntArray(n) { it }
        fun find(x0: Int): Int {
            var x = x0
            while (x != parent[x]) {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        for (edge in connections) {
            val ra = find(edge[0])
            val rb = find(edge[1])
            if (ra != rb) parent[ra] = rb
        }
        return (0 until n).map { find(it) }.toSet().size - 1
    }
}
