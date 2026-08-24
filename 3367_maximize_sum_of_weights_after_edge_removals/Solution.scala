// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

object Solution {
  def maximizeSumOfWeights(edges: Array[Array[Int]], k: Int): Long = {
    val n = edges.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    for (e <- edges) {
      g(e(0)) += ((e(1), e(2)))
      g(e(1)) += ((e(0), e(2)))
    }
    def dfs(u: Int, p: Int): Array[Long] = {
      var base = 0L
      val gains = scala.collection.mutable.ArrayBuffer.empty[Long]
      for ((to, w) <- g(u)) {
        if (to != p) {
          val child = dfs(to, u)
          base += child(1)
          val gain = child(0) + w - child(1)
          if (gain > 0) gains += gain
        }
      }
      val sorted = gains.sorted.reverse
      var withP = base
      var without = base
      var i = 0
      while (i < sorted.length && i < k - 1) {
        withP += sorted(i)
        i += 1
      }
      i = 0
      while (i < sorted.length && i < k) {
        without += sorted(i)
        i += 1
      }
      Array(withP, without)
    }
    dfs(0, -1)(1)
  }
}
