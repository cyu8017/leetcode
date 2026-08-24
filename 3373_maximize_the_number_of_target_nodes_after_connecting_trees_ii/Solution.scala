// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

object Solution {
  private def buildTree(n: Int, edges: Array[Array[Int]]): Array[scala.collection.mutable.ArrayBuffer[Int]] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    g
  }

  private def bipartiteCount(g: Array[scala.collection.mutable.ArrayBuffer[Int]], color: Array[Int]): Array[Int] = {
    java.util.Arrays.fill(color, -1)
    val q = scala.collection.mutable.Queue[Int]()
    q.enqueue(0)
    color(0) = 0
    val cnt = Array(1, 0)
    while (q.nonEmpty) {
      val u = q.dequeue()
      for (v <- g(u)) {
        if (color(v) == -1) {
          color(v) = color(u) ^ 1
          cnt(color(v)) += 1
          q.enqueue(v)
        }
      }
    }
    cnt
  }

  def maxTargetNodes(edges1: Array[Array[Int]], edges2: Array[Array[Int]]): Array[Int] = {
    val n = edges1.length + 1
    val m = edges2.length + 1
    val g1 = buildTree(n, edges1)
    val g2 = buildTree(m, edges2)
    val color1 = new Array[Int](n)
    val color2 = new Array[Int](m)
    val c1 = bipartiteCount(g1, color1)
    val c2 = bipartiteCount(g2, color2)
    val best2 = math.max(c2(0), c2(1))
    Array.tabulate(n)(i => c1(color1(i)) + best2)
  }
}
