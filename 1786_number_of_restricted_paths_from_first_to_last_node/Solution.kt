// LeetCode 1786 - Number of Restricted Paths From First to Last Node
// https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

import java.util.PriorityQueue

class Solution {
    fun countRestrictedPaths(n: Int, edges: Array<IntArray>): Int {
        val adj = Array(n + 1) { mutableListOf<IntArray>() }
        for (e in edges) {
            adj[e[0]].add(intArrayOf(e[1], e[2]))
            adj[e[1]].add(intArrayOf(e[0], e[2]))
        }
        val dist = LongArray(n + 1) { Long.MAX_VALUE }
        dist[n] = 0
        val heap = PriorityQueue<LongArray>(compareBy { it[0] })
        heap.add(longArrayOf(0, n.toLong()))
        while (heap.isNotEmpty()) {
            val (d, uLong) = heap.poll()
            val u = uLong.toInt()
            if (d != dist[u]) {
                continue
            }
            for (vw in adj[u]) {
                val nd = d + vw[1]
                if (nd < dist[vw[0]]) {
                    dist[vw[0]] = nd
                    heap.add(longArrayOf(nd, vw[0].toLong()))
                }
            }
        }
        val order = (1..n).sortedBy { dist[it] }
        val mod = 1_000_000_007L
        val cnt = LongArray(n + 1)
        cnt[n] = 1
        for (u in order) {
            if (u == n) {
                continue
            }
            for (vw in adj[u]) {
                if (dist[u] > dist[vw[0]]) {
                    cnt[u] = (cnt[u] + cnt[vw[0]]) % mod
                }
            }
        }
        return cnt[1].toInt()
    }
}
