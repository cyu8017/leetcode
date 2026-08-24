// LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
// https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

object Solution {
  def getAncestors(n: Int, edges: Array[Array[Int]]): List[List[Int]] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val indeg = Array.fill(n)(0)
    edges.foreach { e =>
      g(e(0)) += e(1)
      indeg(e(1)) += 1
    }
    val anc = Array.fill(n)(scala.collection.mutable.SortedSet.empty[Int])
    val q = scala.collection.mutable.Queue[Int]()
    var i = 0
    while (i < n) {
      if (indeg(i) == 0) q.enqueue(i)
      i += 1
    }
    while (q.nonEmpty) {
      val u = q.dequeue()
      g(u).foreach { v =>
        anc(v) += u
        anc(v) ++= anc(u)
        indeg(v) -= 1
        if (indeg(v) == 0) q.enqueue(v)
      }
    }
    (0 until n).map(i => anc(i).toList).toList
  }
}
