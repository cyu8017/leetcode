// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

class Solution {
    private val INF = 2_000_000_000

    fun modifiedGraphEdges(n: Int, edges: Array<IntArray>, source: Int, destination: Int, target: Int): Array<IntArray> {
        var d = dijkstra(n, edges, source, true)
        if (d[destination] < target) return emptyArray()
        var matched = d[destination] == target
        for (i in edges.indices) {
            if (edges[i][2] != -1) continue
            if (matched) {
                edges[i][2] = INF
                continue
            }
            edges[i][2] = 1
            d = dijkstra(n, edges, source, false)
            if (d[destination] <= target) {
                edges[i][2] += target - d[destination]
                matched = true
            }
        }
        d = dijkstra(n, edges, source, false)
        if (d[destination] != target) return emptyArray()
        return edges
    }

    private fun dijkstra(n: Int, edges: Array<IntArray>, source: Int, ignoreNeg: Boolean): IntArray {
        val dist = IntArray(n) { INF }
        dist[source] = 0
        val pq = java.util.PriorityQueue<IntArray>(compareBy { it[1] })
        pq.offer(intArrayOf(source, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val u = cur[0]
            val d = cur[1]
            if (d != dist[u]) continue
            for (e in edges) {
                val a = e[0]
                val b = e[1]
                var w = e[2]
                if (a != u && b != u) continue
                val to = if (a == u) b else a
                if (w == -1) {
                    if (ignoreNeg) continue
                    w = 1
                }
                if (d + w < dist[to]) {
                    dist[to] = d + w
                    pq.offer(intArrayOf(to, dist[to]))
                }
            }
        }
        return dist
    }
}
