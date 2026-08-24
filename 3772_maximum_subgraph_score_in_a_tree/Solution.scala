// LeetCode 3772 - Maximum Subgraph Score In A Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

object Solution {
  def maxSubgraphScore(n: Int, edges: Array[Array[Int]], good: Array[Int]): Array[Int] = {
    val g = Array.fill(n)(new java.util.ArrayList[Integer]())
    edges.foreach { e =>
      g(e(0)).add(e(1))
      g(e(1)).add(e(0))
    }
    val parent = Array.fill(n)(-2)
    parent(0) = -1
    val order = new java.util.ArrayList[Integer]()
    order.add(0)
    var i = 0
    while (i < order.size()) {
      val u = order.get(i)
      val it = g(u).iterator()
      while (it.hasNext) {
        val v = it.next()
        if (parent(v) == -2) {
          parent(v) = u
          order.add(v)
        }
      }
      i += 1
    }
    val down = new Array[Int](n)
    i = n - 1
    while (i >= 0) {
      val u = order.get(i)
      down(u) = 2 * good(u) - 1
      val it = g(u).iterator()
      while (it.hasNext) {
        val v = it.next()
        if (parent(v) == u && down(v) > 0) down(u) += down(v)
      }
      i -= 1
    }
    val ans = down.clone()
    i = 0
    while (i < order.size()) {
      val u = order.get(i)
      val it = g(u).iterator()
      while (it.hasNext) {
        val v = it.next()
        if (parent(v) == u) {
          var outside = ans(u)
          if (down(v) > 0) outside -= down(v)
          ans(v) = down(v)
          if (outside > 0) ans(v) += outside
        }
      }
      i += 1
    }
    ans
  }
}
