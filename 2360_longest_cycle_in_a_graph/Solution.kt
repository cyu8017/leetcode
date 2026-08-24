// LeetCode 2360 - Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution {
    fun longestCycle(edges: IntArray): Int {
        val n = edges.size
        val vis = BooleanArray(n)
        var ans = -1
        for (i in 0 until n) {
            if (vis[i]) continue
            val dist = HashMap<Int, Int>()
            var cur = i
            var step = 0
            while (cur != -1 && !vis[cur]) {
                vis[cur] = true
                dist[cur] = step
                cur = edges[cur]
                step++
            }
            if (cur != -1 && cur in dist) {
                ans = maxOf(ans, step - dist[cur]!!)
            }
        }
        return ans
    }
}
