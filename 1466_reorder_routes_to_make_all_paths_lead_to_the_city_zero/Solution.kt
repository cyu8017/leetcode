// LeetCode 1466 - Reorder Routes to Make All Paths Lead to the City Zero
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution {
    fun minReorder(n: Int, connections: Array<IntArray>): Int {
        val graph = Array(n) { mutableListOf<IntArray>() }
        for (e in connections) {
            graph[e[0]].add(intArrayOf(e[1], 1))
            graph[e[1]].add(intArrayOf(e[0], 0))
        }
        var ans = 0
        val stack = ArrayDeque<Int>()
        val seen = BooleanArray(n)
        stack.add(0)
        seen[0] = true
        while (stack.isNotEmpty()) {
            val node = stack.removeLast()
            for (edge in graph[node]) {
                val nei = edge[0]
                val cost = edge[1]
                if (!seen[nei]) {
                    seen[nei] = true
                    stack.add(nei)
                    ans += cost
                }
            }
        }
        return ans
    }
}
