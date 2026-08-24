// LeetCode 1557 - Minimum Number of Vertices to Reach All Nodes
// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution {
    fun findSmallestSetOfVertices(n: Int, edges: Array<IntArray>): List<Int> {
        val incoming = BooleanArray(n)
        for (e in edges) incoming[e[1]] = true
        val ans = mutableListOf<Int>()
        for (v in 0 until n) {
            if (!incoming[v]) ans.add(v)
        }
        return ans
    }
}
