// LeetCode 2392 - Build a Matrix With Conditions
// https://leetcode.com/problems/build-a-matrix-with-conditions/

object Solution {
  def buildMatrix(k: Int, rowConditions: Array[Array[Int]], colConditions: Array[Array[Int]]): Array[Array[Int]] = {
    val rowOrder = topo(k, rowConditions)
    val colOrder = topo(k, colConditions)
    if (rowOrder == null || colOrder == null) return Array.empty[Array[Int]]
    val rowPos = Array.fill(k + 1)(0)
    val colPos = Array.fill(k + 1)(0)
    var i = 0
    while (i < k) {
      rowPos(rowOrder(i)) = i
      colPos(colOrder(i)) = i
      i += 1
    }
    val ans = Array.ofDim[Int](k, k)
    var v = 1
    while (v <= k) {
      ans(rowPos(v))(colPos(v)) = v
      v += 1
    }
    ans
  }

  private def topo(k: Int, conds: Array[Array[Int]]): Array[Int] = {
    val g = Array.fill(k + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val indeg = Array.fill(k + 1)(0)
    conds.foreach { c =>
      g(c(0)) += c(1)
      indeg(c(1)) += 1
    }
    val q = scala.collection.mutable.Queue.empty[Int]
    var i = 1
    while (i <= k) {
      if (indeg(i) == 0) q.enqueue(i)
      i += 1
    }
    val order = Array.fill(k)(0)
    var idx = 0
    while (q.nonEmpty) {
      val u = q.dequeue()
      order(idx) = u
      idx += 1
      g(u).foreach { v =>
        indeg(v) -= 1
        if (indeg(v) == 0) q.enqueue(v)
      }
    }
    if (idx != k) null else order
  }
}
