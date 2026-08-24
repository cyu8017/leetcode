// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

import java.util.PriorityQueue

class Solution {
    fun minCost(n: Int, edges: Array<IntArray>): Int {
        val g = Array(n) { ArrayList<IntArray>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            g[u].add(intArrayOf(v, w))
            g[v].add(intArrayOf(u, w * 2))
        }
        val inf = Int.MAX_VALUE / 2
        val dist = IntArray(n) { inf }
        dist[0] = 0
        val pq = PriorityQueue<IntArray>(compareBy { it[0] })
        pq.offer(intArrayOf(0, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val d = cur[0]
            val u = cur[1]
            if (d > dist[u]) continue
            if (u == n - 1) return d
            for (e in g[u]) {
                val v = e[0]
                val w = e[1]
                val nd = d + w
                if (nd < dist[v]) {
                    dist[v] = nd
                    pq.offer(intArrayOf(nd, v))
                }
            }
        }
        return -1
    }
}
