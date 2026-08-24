// LeetCode 2378 - Choose Edges to Maximize Score in a Tree
// https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

object Solution {
  def maxScore(edges: Array[Array[Int]]): Long = {
    val n = edges.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    var i = 1
    while (i < n) {
      val p = edges(i)(0)
      val w = edges(i)(1)
      g(p) += ((i, w))
      i += 1
    }

    def dfs(u: Int): (Long, Long) = {
      var base = 0L
      var bestGain = 0L
      g(u).foreach { case (to, w) =>
        val child = dfs(to)
        base += child._1
        val gain = child._2 + w - child._1
        if (gain > bestGain) bestGain = gain
      }
      (base + bestGain, base)
    }

    dfs(0)._1
  }
}
