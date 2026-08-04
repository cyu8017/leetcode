// LeetCode 1976
// https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

import java.util.PriorityQueue

class Solution {
    fun countPaths(n: Int, roads: Array<IntArray>): Int {
        val mod = 1_000_000_007
        val g = Array(n) { mutableListOf<IntArray>() }
        for (r in roads) {
            g[r[0]].add(intArrayOf(r[1], r[2]))
            g[r[1]].add(intArrayOf(r[0], r[2]))
        }
        val dist = LongArray(n) { Long.MAX_VALUE }
        val ways = IntArray(n)
        dist[0] = 0
        ways[0] = 1
        val pq = PriorityQueue<LongArray>(compareBy { it[0] })
        pq.add(longArrayOf(0, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val d = cur[0]
            val u = cur[1].toInt()
            if (d > dist[u]) continue
            for (e in g[u]) {
                val v = e[0]
                val nd = d + e[1]
                if (nd < dist[v]) {
                    dist[v] = nd
                    ways[v] = ways[u]
                    pq.add(longArrayOf(nd, v.toLong()))
                } else if (nd == dist[v]) {
                    ways[v] = (ways[v] + ways[u]) % mod
                }
            }
        }
        return ways[n - 1]
    }
}
