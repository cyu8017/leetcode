// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum_distance_excluding_one_maximum_weighted_edge/

import java.util.PriorityQueue

class Solution {
    fun minCostExcludingMax(n: Int, edges: Array<IntArray>): Long {
        val g = Array(n) { ArrayList<IntArray>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            g[u].add(intArrayOf(v, w))
            g[v].add(intArrayOf(u, w))
        }
        val INF = 4e18.toLong()
        val dist = Array(n) { LongArray(2) { INF } }
        dist[0][0] = 0
        val pq = PriorityQueue<LongArray>(compareBy { it[0] })
        pq.offer(longArrayOf(0, 0, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val c = cur[0]
            val u = cur[1].toInt()
            val used = cur[2].toInt()
            if (c > dist[u][used]) continue
            if (u == n - 1 && used == 1) return c
            for (e in g[u]) {
                val v = e[0]
                val w = e[1]
                var nxt = c + w
                if (nxt < dist[v][used]) {
                    dist[v][used] = nxt
                    pq.offer(longArrayOf(nxt, v.toLong(), used.toLong()))
                }
                if (used == 0) {
                    nxt = c
                    if (nxt < dist[v][1]) {
                        dist[v][1] = nxt
                        pq.offer(longArrayOf(nxt, v.toLong(), 1))
                    }
                }
            }
        }
        return dist[n - 1][1]
    }
}
