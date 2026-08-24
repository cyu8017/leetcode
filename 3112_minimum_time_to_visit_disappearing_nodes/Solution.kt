// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

class Solution {
    fun minimumTime(n: Int, edges: Array<IntArray>, disappear: IntArray): IntArray {
        val g = Array(n) { ArrayList<IntArray>() }
        for (e in edges) {
            g[e[0]].add(intArrayOf(e[1], e[2]))
            g[e[1]].add(intArrayOf(e[0], e[2]))
        }
        val INF = 1 shl 30
        val dist = IntArray(n) { INF }
        dist[0] = 0
        val pq = java.util.PriorityQueue<IntArray>(compareBy { it[0] })
        pq.offer(intArrayOf(0, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val du = cur[0]
            val u = cur[1]
            if (du > dist[u]) continue
            for (e in g[u]) {
                val v = e[0]
                val w = e[1]
                if (dist[v] > dist[u] + w && dist[u] + w < disappear[v]) {
                    dist[v] = dist[u] + w
                    pq.offer(intArrayOf(dist[v], v))
                }
            }
        }
        return IntArray(n) { i -> if (dist[i] < disappear[i]) dist[i] else -1 }
    }
}
