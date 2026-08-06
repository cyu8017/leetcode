// LeetCode 1466 - Reorder Routes to Make All Paths Lead to the City Zero
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution {
    fun minReorder(n: Int, connections: Array<IntArray>): Int {
        val graph = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (edge in connections) {
            graph[edge[0]].add(edge[1] to 1)
            graph[edge[1]].add(edge[0] to 0)
        }
        var ans = 0
        val stack = ArrayDeque(listOf(0))
        val seen = mutableSetOf(0)
        while (stack.isNotEmpty()) {
            val node = stack.removeLast()
            for ((nei, cost) in graph[node]) {
                if (nei !in seen) {
                    seen.add(nei)
                    stack.add(nei)
                    ans += cost
                }
            }
        }
        return ans
    }
}
