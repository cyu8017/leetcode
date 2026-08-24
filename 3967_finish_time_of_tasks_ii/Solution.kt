// LeetCode 3967 - Finish Time of Tasks II
// https://leetcode.com/problems/finish-time-of-tasks-ii/

class Solution {
    private class Edge(val to: Int, val reverse: Int)

    private fun combine(minimum: Long, maximum: Long, count: Int, base: Int): Long {
        if (count == 0) return base.toLong()
        return 2 * maximum - minimum + base
    }

    fun minFinishTime(n: Int, edges: Array<IntArray>, baseTime: IntArray): Long {
        val graph = Array(n) { ArrayList<Edge>() }
        for (edge in edges) {
            val u = edge[0]
            val v = edge[1]
            val iu = graph[u].size
            val iv = graph[v].size
            graph[u].add(Edge(v, iv))
            graph[v].add(Edge(u, iu))
        }
        val parent = IntArray(n) { -2 }
        val parentEdge = IntArray(n)
        parent[0] = -1
        val order = ArrayList<Int>()
        order.add(0)
        var oi = 0
        while (oi < order.size) {
            val u = order[oi]
            for (edge in graph[u]) {
                if (parent[edge.to] == -2) {
                    parent[edge.to] = u
                    parentEdge[edge.to] = edge.reverse
                    order.add(edge.to)
                }
            }
            oi++
        }
        val incoming = Array(n) { LongArray(graph[it].size) }
        for (idx in n - 1 downTo 1) {
            val u = order[idx]
            var minimum = 1L shl 62
            var maximum = -1L
            var count = 0
            for (edgeIndex in incoming[u].indices) {
                if (edgeIndex == parentEdge[u]) continue
                val value = incoming[u][edgeIndex]
                minimum = minOf(minimum, value)
                maximum = maxOf(maximum, value)
                count++
            }
            val value = combine(minimum, maximum, count, baseTime[u])
            val parentNode = parent[u]
            val reverseIndex = graph[u][parentEdge[u]].reverse
            incoming[parentNode][reverseIndex] = value
        }
        var answer = 1L shl 62
        for (u in order) {
            var min1 = 1L shl 62
            var min2 = 1L shl 62
            var minIndex = -1
            var max1 = -1L
            var max2 = -1L
            var maxIndex = -1
            for (i in incoming[u].indices) {
                val value = incoming[u][i]
                if (value < min1) {
                    min2 = min1
                    min1 = value
                    minIndex = i
                } else if (value < min2) min2 = value
                if (value > max1) {
                    max2 = max1
                    max1 = value
                    maxIndex = i
                } else if (value > max2) max2 = value
            }
            val rootValue = combine(min1, max1, graph[u].size, baseTime[u])
            answer = minOf(answer, rootValue)
            for (i in graph[u].indices) {
                val edge = graph[u][i]
                if (edge.to == parent[u]) continue
                if (graph[u].size == 1) {
                    incoming[edge.to][edge.reverse] = baseTime[u].toLong()
                    continue
                }
                var minimum = min1
                var maximum = max1
                if (i == minIndex) minimum = min2
                if (i == maxIndex) maximum = max2
                incoming[edge.to][edge.reverse] = combine(minimum, maximum, graph[u].size - 1, baseTime[u])
            }
        }
        return answer
    }
}
