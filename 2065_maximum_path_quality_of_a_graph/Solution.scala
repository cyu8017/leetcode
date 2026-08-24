// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

object Solution {
  def maximalPathQuality(values: Array[Int], edges: Array[Array[Int]], maxTime: Int): Int = {
    val n = values.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    edges.foreach { e =>
      g(e(0)) += ((e(1), e(2)))
      g(e(1)) += ((e(0), e(2)))
    }
    var ans = 0
    val vis = Array.ofDim[Int](n)
    def dfs(u: Int, time: Int, quality: Int): Unit = {
      if (time > maxTime) return
      val first = vis(u) == 0
      val q2 = if (first) quality + values(u) else quality
      vis(u) += 1
      if (u == 0) ans = math.max(ans, q2)
      g(u).foreach { case (v, w) => dfs(v, time + w, q2) }
      vis(u) -= 1
    }
    dfs(0, 0, 0)
    ans
  }
}
