// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

object Solution {
  def maxWeight(n: Int, edges: Array[Array[Int]], k: Int, t: Int): Int = {
    val graph = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- edges) graph(e(0)).add(Array(e(1), e(2)))
    val dp = Array.fill(n, k + 1)(new java.util.HashSet[Integer]())
    var u = 0
    while (u < n) { dp(u)(0).add(0); u += 1 }
    var i = 0
    while (i < k) {
      u = 0
      while (u < n) {
        val it = dp(u)(i).iterator()
        while (it.hasNext) {
          val sum = it.next().intValue()
          val eit = graph(u).iterator()
          while (eit.hasNext) {
            val e = eit.next()
            val ns = sum + e(1)
            if (ns < t) dp(e(0))(i + 1).add(ns)
          }
        }
        u += 1
      }
      i += 1
    }
    var ans = -1
    u = 0
    while (u < n) {
      val it = dp(u)(k).iterator()
      while (it.hasNext) {
        val sum = it.next().intValue()
        if (sum > ans) ans = sum
      }
      u += 1
    }
    ans
  }
}
