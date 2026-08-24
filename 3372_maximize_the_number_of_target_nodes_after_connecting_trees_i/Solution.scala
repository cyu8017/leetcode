// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

object Solution {
  private def buildTree(n: Int, edges: Array[Array[Int]]): Array[scala.collection.mutable.ArrayBuffer[Int]] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    g
  }

  private def countWithin(g: Array[scala.collection.mutable.ArrayBuffer[Int]], start: Int, k: Int): Int = {
    if (k < 0) return 0
    val n = g.length
    val vis = new Array[Boolean](n)
    val q = scala.collection.mutable.Queue[(Int, Int)]()
    q.enqueue((start, 0))
    vis(start) = true
    var cnt = 0
    while (q.nonEmpty) {
      val (u, d) = q.dequeue()
      cnt += 1
      if (d != k) {
        for (v <- g(u)) {
          if (!vis(v)) {
            vis(v) = true
            q.enqueue((v, d + 1))
          }
        }
      }
    }
    cnt
  }

  def maxTargetNodes(edges1: Array[Array[Int]], edges2: Array[Array[Int]], k: Int): Array[Int] = {
    val n = edges1.length + 1
    val m = edges2.length + 1
    val g1 = buildTree(n, edges1)
    val g2 = buildTree(m, edges2)
    val cnt1 = Array.tabulate(n)(i => countWithin(g1, i, k))
    var best2 = 0
    if (k > 0) {
      var i = 0
      while (i < m) {
        val c = countWithin(g2, i, k - 1)
        if (c > best2) best2 = c
        i += 1
      }
    }
    Array.tabulate(n)(i => cnt1(i) + best2)
  }
}
