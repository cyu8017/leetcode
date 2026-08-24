// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

import java.util.PriorityQueue

class Solution {
    fun networkDelayTime(times: Array<IntArray>, n: Int, k: Int): Int {
        val graph = Array(n + 1) { ArrayList<IntArray>() }
        for (edge in times) graph[edge[0]].add(intArrayOf(edge[1], edge[2]))
        val INF = Int.MAX_VALUE / 4
        val dist = IntArray(n + 1) { INF }
        dist[k] = 0
        val heap = PriorityQueue(compareBy<IntArray> { it[0] })
        heap.offer(intArrayOf(0, k))
        while (heap.isNotEmpty()) {
            val cur = heap.poll()
            val d = cur[0]
            val node = cur[1]
            if (d > dist[node]) continue
            for (e in graph[node]) {
                val nd = d + e[1]
                if (nd < dist[e[0]]) {
                    dist[e[0]] = nd
                    heap.offer(intArrayOf(nd, e[0]))
                }
            }
        }
        var ans = 0
        for (i in 1..n) ans = maxOf(ans, dist[i])
        return if (ans == INF) -1 else ans
    }
}
