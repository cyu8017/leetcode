// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

import java.util.PriorityQueue

class Solution {
    fun minTime(n: Int, edges: Array<IntArray>): Int {
        val g = Array(n) { ArrayList<IntArray>() }
        for (e in edges) g[e[0]].add(intArrayOf(e[1], e[2], e[3]))
        val Inf = 1e18.toLong()
        val dist = LongArray(n) { Inf }
        dist[0] = 0
        val pq = PriorityQueue<LongArray>(compareBy { it[0] })
        pq.offer(longArrayOf(0, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val t = cur[0]
            val u = cur[1].toInt()
            if (t != dist[u]) continue
            if (u == n - 1) return t.toInt()
            for (e in g[u]) {
                var nt = t
                if (nt > e[2]) continue
                if (nt < e[1]) nt = e[1].toLong()
                nt += 1
                if (nt < dist[e[0]]) {
                    dist[e[0]] = nt
                    pq.offer(longArrayOf(nt, e[0].toLong()))
                }
            }
        }
        return if (dist[n - 1] == Inf) -1 else dist[n - 1].toInt()
    }
}
