// LeetCode 3928 - Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

class Solution {
    private class Edge(val to: Int, val empty: Int, val full: Int)

    fun minCostToBuyApples(n: Int, prices: IntArray, roads: Array<IntArray>): LongArray {
        val g = Array(n) { ArrayList<Edge>() }
        for (road in roads) {
            val empty = road[2]
            val full = road[2] * road[3]
            g[road[0]].add(Edge(road[1], empty, full))
            g[road[1]].add(Edge(road[0], empty, full))
        }
        val inf = 1L shl 62
        val answer = LongArray(n)
        for (source in 0 until n) {
            val emptyDist = dijkstra(n, g, source, false, inf)
            val fullDist = dijkstra(n, g, source, true, inf)
            var best = prices[source].toLong()
            for (shop in 0 until n) {
                if (emptyDist[shop] == inf || fullDist[shop] == inf) continue
                val total = emptyDist[shop] + fullDist[shop] + prices[shop]
                if (total < best) best = total
            }
            answer[source] = best
        }
        return answer
    }

    private fun dijkstra(n: Int, g: Array<ArrayList<Edge>>, source: Int, carrying: Boolean, inf: Long): LongArray {
        val dist = LongArray(n) { inf }
        dist[source] = 0
        val pq = java.util.PriorityQueue<LongArray>(compareBy { it[0] })
        pq.offer(longArrayOf(0, source.toLong()))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val d = cur[0]
            val node = cur[1].toInt()
            if (d != dist[node]) continue
            for (e in g[node]) {
                val weight = if (carrying) e.full else e.empty
                val next = d + weight
                if (next < dist[e.to]) {
                    dist[e.to] = next
                    pq.offer(longArrayOf(next, e.to.toLong()))
                }
            }
        }
        return dist
    }
}
