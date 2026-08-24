// LeetCode 3977 - Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

class Solution {
    fun minTimeMaxPower(n: Int, edges: Array<IntArray>, power: Int, cost: IntArray, source: Int, target: Int): LongArray {
        val INF = 1L shl 62
        val g = Array(n) { ArrayList<IntArray>() }
        for (e in edges) g[e[0]].add(intArrayOf(e[1], e[2]))
        val dist = Array(n) { LongArray(power + 1) { INF } }
        val pq = java.util.PriorityQueue<LongArray>(Comparator { a, b ->
            if (a[0] != b[0]) a[0].compareTo(b[0]) else a[1].compareTo(b[1])
        })
        pq.offer(longArrayOf(0, -power.toLong(), source.toLong()))
        dist[source][power] = 0
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val d = cur[0]
            var p = (-cur[1]).toInt()
            val u = cur[2].toInt()
            if (u == target) return longArrayOf(d, p.toLong())
            if (d > dist[u][p] || p < cost[u]) continue
            p -= cost[u]
            for (e in g[u]) {
                val v = e[0]
                val t = e[1]
                val nd = d + t
                if (nd < dist[v][p]) {
                    dist[v][p] = nd
                    pq.offer(longArrayOf(nd, -p.toLong(), v.toLong()))
                }
            }
        }
        return longArrayOf(-1, -1)
    }
}
