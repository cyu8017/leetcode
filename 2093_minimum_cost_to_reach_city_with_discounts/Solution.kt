// LeetCode 2093 - Minimum Cost to Reach City With Discounts
// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

import java.util.PriorityQueue

class Solution {
    fun minimumCost(n: Int, highways: Array<IntArray>, discounts: Int): Int {
        val g = Array(n) { mutableListOf<IntArray>() }
        for (h in highways) {
            g[h[0]].add(intArrayOf(h[1], h[2]))
            g[h[1]].add(intArrayOf(h[0], h[2]))
        }
        val inf = 1 shl 30
        val dist = Array(n) { IntArray(discounts + 1) { inf } }
        val pq = PriorityQueue<IntArray>(compareBy { it[0] })
        dist[0][discounts] = 0
        pq.offer(intArrayOf(0, 0, discounts))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val cost = cur[0]
            val city = cur[1]
            val disc = cur[2]
            if (city == n - 1) return cost
            if (cost > dist[city][disc]) continue
            for (e in g[city]) {
                val v = e[0]
                val w = e[1]
                if (cost + w < dist[v][disc]) {
                    dist[v][disc] = cost + w
                    pq.offer(intArrayOf(dist[v][disc], v, disc))
                }
                if (disc > 0 && cost + w / 2 < dist[v][disc - 1]) {
                    dist[v][disc - 1] = cost + w / 2
                    pq.offer(intArrayOf(dist[v][disc - 1], v, disc - 1))
                }
            }
        }
        return -1
    }
}
