// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

object Solution {
  def shortestAlternatingPaths(n: Int, redEdges: Array[Array[Int]], blueEdges: Array[Array[Int]]): Array[Int] = {
    val red = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    val blue = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    for (e <- redEdges) red(e(0)) += e(1)
    for (e <- blueEdges) blue(e(0)) += e(1)
    val ans = Array.fill(n)(-1)
    val seen = Array.fill(n, 2)(false)
    val q = scala.collection.mutable.Queue[(Int, Int, Int)]()
    q.enqueue((0, 0, -1))
    seen(0)(0) = true
    seen(0)(1) = true
    ans(0) = 0
    while (q.nonEmpty) {
      val (node, dist, color) = q.dequeue()
      if (color != 0) {
        for (nei <- red(node) if !seen(nei)(0)) {
          seen(nei)(0) = true
          if (ans(nei) == -1) ans(nei) = dist + 1
          q.enqueue((nei, dist + 1, 0))
        }
      }
      if (color != 1) {
        for (nei <- blue(node) if !seen(nei)(1)) {
          seen(nei)(1) = true
          if (ans(nei) == -1) ans(nei) = dist + 1
          q.enqueue((nei, dist + 1, 1))
        }
      }
    }
    ans
  }
}
