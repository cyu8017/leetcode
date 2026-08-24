// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

import java.util.PriorityQueue

class Solution {
    fun minCost(n: Int, roads: Array<IntArray>, appleCost: IntArray, k: Int): LongArray {
        val g = Array(n + 1) { ArrayList<IntArray>() }
        for (r in roads) {
            g[r[0]].add(intArrayOf(r[1], r[2]))
            g[r[1]].add(intArrayOf(r[0], r[2]))
        }
        val ans = LongArray(n)
        val INF = 1L shl 60
        for (start in 1..n) {
            val dist = LongArray(n + 1) { INF }
            dist[start] = 0
            val pq = PriorityQueue(compareBy<LongArray> { it[0] })
            pq.offer(longArrayOf(0, start.toLong()))
            while (pq.isNotEmpty()) {
                val cur = pq.poll()
                val d = cur[0]
                val u = cur[1].toInt()
                if (d != dist[u]) continue
                for (e in g[u]) {
                    val v = e[0]
                    val w = e[1]
                    val nd = d + w
                    if (nd < dist[v]) {
                        dist[v] = nd
                        pq.offer(longArrayOf(nd, v.toLong()))
                    }
                }
            }
            var best = INF
            for (city in 1..n) {
                val cost = dist[city] * (k + 1) + appleCost[city - 1]
                if (cost < best) best = cost
            }
            ans[start - 1] = best
        }
        return ans
    }
}
