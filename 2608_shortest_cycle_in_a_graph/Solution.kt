// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

class Solution {
    fun findShortestCycle(n: Int, edges: Array<IntArray>): Int {
        val g = Array(n) { ArrayList<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        val INF = 1_000_000_000
        var ans = INF
        for (start in 0 until n) {
            val dist = IntArray(n) { -1 }
            val parent = IntArray(n) { -1 }
            val q = ArrayDeque<Int>()
            q.add(start)
            dist[start] = 0
            while (q.isNotEmpty()) {
                val u = q.removeFirst()
                for (v in g[u]) {
                    if (dist[v] < 0) {
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.add(v)
                    } else if (parent[u] != v) {
                        val c = dist[u] + dist[v] + 1
                        if (c < ans) ans = c
                    }
                }
            }
        }
        return if (ans == INF) -1 else ans
    }
}
