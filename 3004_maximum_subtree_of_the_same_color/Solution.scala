// LeetCode 3004 - Maximum Subtree of the Same Color
// https://leetcode.com/problems/maximum-subtree-of-the-same-color/

object Solution {
  def maximumSubtreeSize(edges: Array[Array[Int]], colors: Array[Int]): Int = {
    val n = edges.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val size = Array.ofDim[Int](n)
    var ans = 0
    def dfs(a: Int, fa: Int): Boolean = {
      size(a) = 1
      var ok = true
      for (b <- g(a) if b != fa) {
        val t = dfs(b, a)
        ok = ok && t && colors(a) == colors(b)
        size(a) += size(b)
      }
      if (ok) ans = math.max(ans, size(a))
      ok
    }
    dfs(0, -1)
    ans
  }
}
