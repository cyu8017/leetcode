// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

object Solution {
  def findMedian(n: Int, edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- edges) {
      g(e(0)).add(Array(e(1), e(2)))
      g(e(1)).add(Array(e(0), e(2)))
    }
    val ans = new Array[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val u = queries(qi)(0)
      val v = queries(qi)(1)
      val parent = Array.fill(n)(-2)
      val pw = new Array[Int](n)
      parent(u) = -1
      val q = new java.util.ArrayDeque[Integer]()
      q.add(u)
      while (!q.isEmpty) {
        val x = q.poll()
        if (x == v) { /* found */ }
        else {
          val it = g(x).iterator()
          while (it.hasNext) {
            val e = it.next()
            if (parent(e(0)) == -2) {
              parent(e(0)) = x
              pw(e(0)) = e(1)
              q.add(e(0))
            }
          }
        }
      }
      val nodes = new java.util.ArrayList[Integer]()
      nodes.add(v)
      val weights = new java.util.ArrayList[Integer]()
      var cur = v
      while (cur != u) {
        weights.add(pw(cur))
        cur = parent(cur)
        nodes.add(cur)
      }
      java.util.Collections.reverse(nodes)
      java.util.Collections.reverse(weights)
      var total = 0
      val wit = weights.iterator()
      while (wit.hasNext) total += wit.next()
      val need = (total + 1) / 2
      var sum = 0
      var med = u
      var i = 0
      while (i < weights.size()) {
        sum += weights.get(i)
        med = nodes.get(i + 1)
        if (sum >= need) i = weights.size()
        else i += 1
      }
      ans(qi) = med
      qi += 1
    }
    ans
  }
}
