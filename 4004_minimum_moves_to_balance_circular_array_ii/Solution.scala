// LeetCode 4004 - Minimum Moves to Balance Circular Array II
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

import scala.collection.mutable

object Solution {
  private val INF = 1000000000

  private class Edge(var to: Int, var cap: Int, var cost: Int, var rev: Int)

  private class MinCostMaxFlow(n: Int) {
    val graph: Array[mutable.ArrayBuffer[Edge]] = Array.fill(n)(mutable.ArrayBuffer.empty[Edge])

    def addEdge(u: Int, v: Int, cap: Int, cost: Int): Unit = {
      graph(u) += new Edge(v, cap, cost, graph(v).size)
      graph(v) += new Edge(u, 0, -cost, graph(u).size - 1)
    }

    def minCostFlow(source: Int, sink: Int, maxFlow: Int): Long = {
      var totalCost = 0L
      var currentFlow = 0
      while (currentFlow < maxFlow) {
        val dist = Array.fill(n)(INF)
        val parentNode = Array.fill(n)(-1)
        val parentEdge = Array.fill(n)(-1)
        val inQueue = new Array[Boolean](n)
        val q = mutable.ArrayDeque[Int]()
        q.append(source)
        dist(source) = 0
        inQueue(source) = true
        while (q.nonEmpty) {
          val u = q.removeHead()
          inQueue(u) = false
          var i = 0
          while (i < graph(u).size) {
            val e = graph(u)(i)
            if (e.cap > 0 && dist(e.to) > dist(u) + e.cost) {
              dist(e.to) = dist(u) + e.cost
              parentNode(e.to) = u
              parentEdge(e.to) = i
              if (!inQueue(e.to)) {
                inQueue(e.to) = true
                q.append(e.to)
              }
            }
            i += 1
          }
        }
        if (dist(sink) == INF) return -1
        var pushFlow = maxFlow - currentFlow
        var cur = sink
        while (cur != source) {
          val e = graph(parentNode(cur))(parentEdge(cur))
          if (e.cap < pushFlow) pushFlow = e.cap
          cur = parentNode(cur)
        }
        cur = sink
        while (cur != source) {
          val p = parentNode(cur)
          val idx = parentEdge(cur)
          val rev = graph(p)(idx).rev
          graph(p)(idx).cap -= pushFlow
          graph(cur)(rev).cap += pushFlow
          cur = parentNode(cur)
        }
        currentFlow += pushFlow
        totalCost += pushFlow.toLong * dist(sink)
      }
      totalCost
    }
  }

  def minMoves(balance: Array[Int]): Long = {
    var totalBalance = 0
    var totalDeficit = 0
    for (x <- balance) {
      totalBalance += x
      if (x < 0) totalDeficit += -x
    }
    if (totalBalance < 0) return -1
    if (totalDeficit == 0) return 0
    val n = balance.length
    val source = n
    val sink = n + 1
    val mcmf = new MinCostMaxFlow(n + 2)
    var i = 0
    while (i < n) {
      val x = balance(i)
      if (x > 0) mcmf.addEdge(source, i, x, 0)
      else if (x < 0) mcmf.addEdge(i, sink, -x, 0)
      mcmf.addEdge(i, (i + 1) % n, INF, 1)
      mcmf.addEdge(i, (i - 1 + n) % n, INF, 1)
      i += 1
    }
    mcmf.minCostFlow(source, sink, totalDeficit)
  }
}
