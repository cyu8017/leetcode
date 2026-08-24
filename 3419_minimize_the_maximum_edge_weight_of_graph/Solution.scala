// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

object Solution {
  def minMaxWeight(n: Int, edges: Array[Array[Int]], threshold: Int): Int = {
    var lo = 1
    var hi = 1000001
    var ans = -1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(n, edges, mid)) {
        ans = mid
        hi = mid
      } else lo = mid + 1
    }
    ans
  }

  private def ok(n: Int, edges: Array[Array[Int]], mid: Int): Boolean = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      if (e(2) <= mid) g(e(1)) += e(0)
    }
    val vis = Array.fill(n)(false)
    val q = new java.util.ArrayDeque[Integer]()
    q.offer(0)
    vis(0) = true
    var cnt = 1
    while (!q.isEmpty) {
      val u = q.poll()
      g(u).foreach { v =>
        if (!vis(v)) {
          vis(v) = true
          cnt += 1
          q.offer(v)
        }
      }
    }
    cnt == n
  }
}
