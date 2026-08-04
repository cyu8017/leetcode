// LeetCode 1928
// https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

import java.util.PriorityQueue

class Solution {
    fun minCost(maxTime: Int, edges: Array<IntArray>, passingFee: IntArray): Int {
        val n = passingFee.size
        val graph = Array(n) { mutableListOf<IntArray>() }
        for (e in edges) {
            graph[e[0]].add(intArrayOf(e[1], e[2]))
            graph[e[1]].add(intArrayOf(e[0], e[2]))
        }
        val minTime = IntArray(n) { maxTime + 1 }
        val pq = PriorityQueue<IntArray>(compareBy { it[0] })
        pq.add(intArrayOf(passingFee[0], 0, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val cost = cur[0]
            val time = cur[1]
            val u = cur[2]
            if (time >= minTime[u]) continue
            minTime[u] = time
            if (u == n - 1) return cost
            for (edge in graph[u]) {
                val v = edge[0]
                val nt = time + edge[1]
                if (nt <= maxTime && nt < minTime[v]) {
                    pq.add(intArrayOf(cost + passingFee[v], nt, v))
                }
            }
        }
        return -1
    }
}
