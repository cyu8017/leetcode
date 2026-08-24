// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution {
    fun shortestAlternatingPaths(n: Int, redEdges: Array<IntArray>, blueEdges: Array<IntArray>): IntArray {
        val graph = Array(2) { Array(n) { mutableListOf<Int>() } }
        for (e in redEdges) graph[0][e[0]].add(e[1])
        for (e in blueEdges) graph[1][e[0]].add(e[1])
        val ans = IntArray(n) { -1 }
        val queue = ArrayDeque<IntArray>()
        queue.add(intArrayOf(0, 0, 0))
        queue.add(intArrayOf(0, 1, 0))
        val seen = Array(n) { BooleanArray(2) }
        seen[0][0] = true
        seen[0][1] = true
        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            val node = cur[0]
            val color = cur[1]
            val dist = cur[2]
            if (ans[node] == -1) ans[node] = dist
            val nextColor = 1 - color
            for (nxt in graph[color][node]) {
                if (!seen[nxt][nextColor]) {
                    seen[nxt][nextColor] = true
                    queue.add(intArrayOf(nxt, nextColor, dist + 1))
                }
            }
        }
        return ans
    }
}
