// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

object Solution {
  def maxOutput(n: Int, edges: Array[Array[Int]], price: Array[Int]): Long = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var ans = 0L
    def dfs(u: Int, p: Int): Long = {
      var maxChild = 0L
      g(u).foreach { v =>
        if (v != p) {
          val child = dfs(v, u)
          if (child > maxChild) maxChild = child
          if (child > ans) ans = child
        }
      }
      price(u).toLong + maxChild
    }
    dfs(0, -1)
    ans
  }
}
