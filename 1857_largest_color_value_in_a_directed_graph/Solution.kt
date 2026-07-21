// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

class Solution {
    fun largestPathValue(colors: String, edges: Array<IntArray>): Int {
        val n = colors.length
        val indegree = IntArray(n)
        val adjacency = Array(n) { mutableListOf<Int>() }
        for (edge in edges) {
            adjacency[edge[0]].add(edge[1])
            indegree[edge[1]]++
        }
        val queue = ArrayDeque<Int>()
        for (node in 0 until n) {
            if (indegree[node] == 0) queue.addLast(node)
        }
        val dp = Array(n) { IntArray(26) }
        for (node in 0 until n) {
            dp[node][colors[node] - 'a'] = 1
        }
        var processed = 0
        var answer = 0
        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            processed++
            answer = maxOf(answer, dp[node].maxOrNull()!!)
            for (neighbor in adjacency[node]) {
                val neighborColor = colors[neighbor] - 'a'
                for (colorIndex in 0 until 26) {
                    var candidate = dp[node][colorIndex]
                    if (colorIndex == neighborColor) candidate++
                    if (candidate > dp[neighbor][colorIndex]) {
                        dp[neighbor][colorIndex] = candidate
                    }
                }
                indegree[neighbor]--
                if (indegree[neighbor] == 0) queue.addLast(neighbor)
            }
        }
        return if (processed == n) answer else -1
    }
}
