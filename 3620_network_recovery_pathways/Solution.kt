// LeetCode 3620 - Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/

import java.util.PriorityQueue

class Solution {
    private lateinit var g: Array<ArrayList<IntArray>>
    private var kLimit = 0L
    private var n = 0

    private fun check(mid: Int): Boolean {
        val INF = Int.MAX_VALUE / 2
        val dist = IntArray(n) { INF }
        dist[0] = 0
        val pq = PriorityQueue<IntArray>(compareBy { it[0] })
        pq.offer(intArrayOf(0, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val d = cur[0]
            val u = cur[1]
            if (d.toLong() > kLimit) return false
            if (u == n - 1) return true
            if (dist[u] < d) continue
            for (e in g[u]) {
                val v = e[0]
                val w = e[1]
                if (w < mid) continue
                val nd = d + w
                if (nd < dist[v]) {
                    dist[v] = nd
                    pq.offer(intArrayOf(nd, v))
                }
            }
        }
        return false
    }

    fun findMaxPathScore(edges: Array<IntArray>, online: BooleanArray, k: Long): Int {
        this.kLimit = k
        n = online.size
        g = Array(n) { ArrayList() }
        var l = Int.MAX_VALUE
        var r = 0
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            if (!online[u] || !online[v]) continue
            g[u].add(intArrayOf(v, w))
            l = minOf(l, w)
            r = maxOf(r, w)
        }
        if (l == Int.MAX_VALUE) return -1
        while (l < r) {
            val mid = (l + r + 1) shr 1
            if (check(mid)) l = mid
            else r = mid - 1
        }
        return if (check(l)) l else -1
    }
}
