// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

class Solution {
    fun shortestPathWithHops(n: Int, edges: Array<IntArray>, s: Int, d: Int, k: Int): Int {
        val g = Array(n) { ArrayList<IntArray>() }
        for (e in edges) {
            g[e[0]].add(intArrayOf(e[1], e[2]))
            g[e[1]].add(intArrayOf(e[0], e[2]))
        }
        val dist = Array(n) { IntArray(k + 1) { Int.MAX_VALUE / 4 } }
        dist[s][0] = 0
        val pq = java.util.PriorityQueue<IntArray>(compareBy { it[2] })
        pq.offer(intArrayOf(s, 0, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val u = cur[0]
            val hops = cur[1]
            val cd = cur[2]
            if (u == d) return cd
            if (cd > dist[u][hops]) continue
            for (e in g[u]) {
                val to = e[0]
                val w = e[1]
                if (cd + w < dist[to][hops]) {
                    dist[to][hops] = cd + w
                    pq.offer(intArrayOf(to, hops, dist[to][hops]))
                }
                if (hops < k && cd < dist[to][hops + 1]) {
                    dist[to][hops + 1] = cd
                    pq.offer(intArrayOf(to, hops + 1, cd))
                }
            }
        }
        return -1
    }
}
