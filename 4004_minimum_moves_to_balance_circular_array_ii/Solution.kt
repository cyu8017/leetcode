// LeetCode 4004 - Minimum Moves to Balance Circular Array II
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

class Solution {
    companion object {
        private const val INF = 1000000000
    }

    private class Edge(val to: Int, var cap: Int, val cost: Int, val rev: Int)

    private class MinCostMaxFlow(val n: Int) {
        val graph = Array(n) { ArrayList<Edge>() }

        fun addEdge(u: Int, v: Int, cap: Int, cost: Int) {
            graph[u].add(Edge(v, cap, cost, graph[v].size))
            graph[v].add(Edge(u, 0, -cost, graph[u].size - 1))
        }

        fun minCostFlow(source: Int, sink: Int, maxFlow: Int): Long {
            var totalCost = 0L
            var currentFlow = 0
            while (currentFlow < maxFlow) {
                val dist = IntArray(n) { INF }
                val parentNode = IntArray(n) { -1 }
                val parentEdge = IntArray(n) { -1 }
                val inQueue = BooleanArray(n)
                val q = ArrayDeque<Int>()
                q.add(source)
                dist[source] = 0
                inQueue[source] = true
                while (q.isNotEmpty()) {
                    val u = q.removeFirst()
                    inQueue[u] = false
                    for (i in graph[u].indices) {
                        val e = graph[u][i]
                        if (e.cap > 0 && dist[e.to] > dist[u] + e.cost) {
                            dist[e.to] = dist[u] + e.cost
                            parentNode[e.to] = u
                            parentEdge[e.to] = i
                            if (!inQueue[e.to]) {
                                inQueue[e.to] = true
                                q.add(e.to)
                            }
                        }
                    }
                }
                if (dist[sink] == INF) return -1
                var pushFlow = maxFlow - currentFlow
                var cur = sink
                while (cur != source) {
                    val e = graph[parentNode[cur]][parentEdge[cur]]
                    if (e.cap < pushFlow) pushFlow = e.cap
                    cur = parentNode[cur]
                }
                cur = sink
                while (cur != source) {
                    val p = parentNode[cur]
                    val idx = parentEdge[cur]
                    val rev = graph[p][idx].rev
                    graph[p][idx].cap -= pushFlow
                    graph[cur][rev].cap += pushFlow
                    cur = parentNode[cur]
                }
                currentFlow += pushFlow
                totalCost += pushFlow.toLong() * dist[sink]
            }
            return totalCost
        }
    }

    fun minMoves(balance: IntArray): Long {
        var totalBalance = 0
        var totalDeficit = 0
        for (x in balance) {
            totalBalance += x
            if (x < 0) totalDeficit += -x
        }
        if (totalBalance < 0) return -1
        if (totalDeficit == 0) return 0
        val n = balance.size
        val source = n
        val sink = n + 1
        val mcmf = MinCostMaxFlow(n + 2)
        for (i in 0 until n) {
            val x = balance[i]
            if (x > 0) mcmf.addEdge(source, i, x, 0)
            else if (x < 0) mcmf.addEdge(i, sink, -x, 0)
            mcmf.addEdge(i, (i + 1) % n, INF, 1)
            mcmf.addEdge(i, (i - 1 + n) % n, INF, 1)
        }
        return mcmf.minCostFlow(source, sink, totalDeficit)
    }
}
