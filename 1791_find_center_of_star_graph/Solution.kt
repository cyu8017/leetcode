// LeetCode 1791 - Find Center of Star Graph
// https://leetcode.com/problems/find-center-of-star-graph/

class Solution {
    fun findCenter(edges: Array<IntArray>): Int {
        val (a, b) = edges[0][0] to edges[0][1]
        val (c, d) = edges[1][0] to edges[1][1]
        return if (a == c || a == d) a else b
    }
}
