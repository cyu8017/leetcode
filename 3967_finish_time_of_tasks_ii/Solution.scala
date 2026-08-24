// LeetCode 3967 - Finish Time of Tasks II
// https://leetcode.com/problems/finish-time-of-tasks-ii/

import scala.collection.mutable

object Solution {
  private class Edge(val to: Int, val reverse: Int)

  private def combine(minimum: Long, maximum: Long, count: Int, base: Int): Long = {
    if (count == 0) base
    else 2 * maximum - minimum + base
  }

  def minFinishTime(n: Int, edges: Array[Array[Int]], baseTime: Array[Int]): Long = {
    val graph = Array.fill(n)(mutable.ArrayBuffer.empty[Edge])
    for (edge <- edges) {
      val u = edge(0)
      val v = edge(1)
      val iu = graph(u).size
      val iv = graph(v).size
      graph(u) += new Edge(v, iv)
      graph(v) += new Edge(u, iu)
    }
    val parent = Array.fill(n)(-2)
    val parentEdge = new Array[Int](n)
    parent(0) = -1
    val order = mutable.ArrayBuffer(0)
    var i = 0
    while (i < order.size) {
      val u = order(i)
      for (edge <- graph(u)) {
        if (parent(edge.to) == -2) {
          parent(edge.to) = u
          parentEdge(edge.to) = edge.reverse
          order += edge.to
        }
      }
      i += 1
    }
    val incoming = Array.tabulate(n)(i => new Array[Long](graph(i).size))
    var oi = n - 1
    while (oi > 0) {
      val u = order(oi)
      var minimum = 1L << 62
      var maximum = -1L
      var count = 0
      var edgeIndex = 0
      while (edgeIndex < incoming(u).length) {
        if (edgeIndex != parentEdge(u)) {
          val value = incoming(u)(edgeIndex)
          minimum = math.min(minimum, value)
          maximum = math.max(maximum, value)
          count += 1
        }
        edgeIndex += 1
      }
      val value = combine(minimum, maximum, count, baseTime(u))
      val parentNode = parent(u)
      val reverseIndex = graph(u)(parentEdge(u)).reverse
      incoming(parentNode)(reverseIndex) = value
      oi -= 1
    }
    var answer = 1L << 62
    for (u <- order) {
      var min1 = 1L << 62
      var min2 = 1L << 62
      var minIndex = -1
      var max1 = -1L
      var max2 = -1L
      var maxIndex = -1
      i = 0
      while (i < incoming(u).length) {
        val value = incoming(u)(i)
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
        i += 1
      }
      val rootValue = combine(min1, max1, graph(u).size, baseTime(u))
      answer = math.min(answer, rootValue)
      i = 0
      while (i < graph(u).size) {
        val edge = graph(u)(i)
        if (edge.to != parent(u)) {
          if (graph(u).size == 1) incoming(edge.to)(edge.reverse) = baseTime(u)
          else {
            var minimum = min1
            var maximum = max1
            if (i == minIndex) minimum = min2
            if (i == maxIndex) maximum = max2
            incoming(edge.to)(edge.reverse) = combine(minimum, maximum, graph(u).size - 1, baseTime(u))
          }
        }
        i += 1
      }
    }
    answer
  }
}
