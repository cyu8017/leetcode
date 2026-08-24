// LeetCode 3786 - Total Sum Of Interaction Cost In Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

object Solution {
  def interactionCost(n: Int, edges: Array[Array[Int]], group: Array[Int]): Long = {
    val g = Array.fill(n)(new java.util.ArrayList[Integer]())
    edges.foreach { e =>
      g(e(0)).add(e(1))
      g(e(1)).add(e(0))
    }
    val total = new Array[Int](21)
    group.foreach(x => total(x) += 1)
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
    val count = Array.ofDim[Int](n, 21)
    var ans = 0L
    i = n - 1
    while (i >= 0) {
      val u = order.get(i)
      count(u)(group(u)) += 1
      val it = g(u).iterator()
      while (it.hasNext) {
        val v = it.next()
        if (parent(v) == u) {
          var c = 1
          while (c <= 20) {
            val x = count(v)(c)
            ans += x.toLong * (total(c) - x)
            count(u)(c) += x
            c += 1
          }
        }
      }
      i -= 1
    }
    ans
  }
}
