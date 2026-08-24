
// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph(n: Int, edges: Array<IntArray>) {
    private val g: Array<MutableList<IntArray>> = Array(n) { ArrayList() }

    init {
        for (e in edges) g[e[0]].add(intArrayOf(e[1], e[2]))
    }

    fun addEdge(edge: IntArray) {
        g[edge[0]].add(intArrayOf(edge[1], edge[2]))
    }

    fun shortestPath(node1: Int, node2: Int): Int {
        val n = g.size
        val dist = IntArray(n) { 1 shl 30 }
        dist[node1] = 0
        val pq = java.util.PriorityQueue<IntArray>(compareBy { it[1] })
        pq.offer(intArrayOf(node1, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val u = cur[0]
            val d = cur[1]
            if (u == node2) return d
            if (d > dist[u]) continue
            for (e in g[u]) {
                val nd = d + e[1]
                if (nd < dist[e[0]]) {
                    dist[e[0]] = nd
                    pq.offer(intArrayOf(e[0], nd))
                }
            }
        }
        return -1
    }
}
