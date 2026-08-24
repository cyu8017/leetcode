// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

object Solution {
  def minScore(n: Int, roads: Array[Array[Int]]): Int = {
    val g = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    roads.foreach { r =>
      g(r(0)) += ((r(1), r(2)))
      g(r(1)) += ((r(0), r(2)))
    }
    val vis = new Array[Boolean](n + 1)
    var ans = 1 << 30
    val q = scala.collection.mutable.Queue[Int]()
    q.enqueue(1)
    vis(1) = true
    while (q.nonEmpty) {
      val u = q.dequeue()
      g(u).foreach { case (v, w) =>
        if (w < ans) ans = w
        if (!vis(v)) {
          vis(v) = true
          q.enqueue(v)
        }
      }
    }
    ans
  }
}
